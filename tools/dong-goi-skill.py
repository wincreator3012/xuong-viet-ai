#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ĐÓNG GÓI SKILL của Xưởng viết AI, hai chế độ.

Trong xưởng đã dựng (mặc định): gói skill RIÊNG của người dùng, ghi vào <thư mục bài>/_skill/
    python3 tools/dong-goi-skill.py
  - mỗi skill thành <tên>.zip (một thư mục gốc cùng tên, đúng yêu cầu tải lên Claude) và một thư mục cùng tên để xem;
  - tên mang tiền tố "xuong-viet-" (viet-nguyen-ban thành xuong-viet-nguyen-ban, tap-viet thành xuong-viet-tap-viet),
    để không trùng skill khác trong tài khoản;
  - ngay dưới mục "Cấu hình cá nhân" chèn khối "Đã thiết lập": tên, xưng hô, thư mục làm việc, kho tư liệu;
  - chụp tệp riêng vào references/ theo "chup" trong skills/<tên>/kem.json: giọng văn (mọi gói), bài học giọng (gói viết
    nguyên bản), hồ sơ người viết (gói tập viết); --chi-giong-van chỉ chụp giọng văn;
  - không bao giờ đưa tệp nào trong kho tư liệu hay thư mục bài vào gói.

Ở bản vẽ (người bảo trì): gói CHUNG cho người chỉ dùng khung chat, ghi vào dong-goi/
    python3 tools/dong-goi-skill.py --chung
  - <tên>.zip với tên gốc, không có phần riêng của ai;
  - dong-goi/tep-cho-du-an/: SKILL.md thành <tên>.md, references/x.md thành <tên>--x.md, để tải lên ChatGPT Projects,
    Gemini Gems, Claude Projects.

Mô tả trong gói .zip dùng "moTaNgan" của kem.json (tối đa 200 ký tự, giới hạn khi tải skill lên Claude);
--mo-ta-day-du giữ mô tả đầy đủ của SKILL.md (cho nền tảng không giới hạn, như Claude Code).
Python 3.9+, chỉ thư viện chuẩn.
"""
import sys
sys.dont_write_bytecode = True
import argparse  # noqa: E402
import hashlib  # noqa: E402
import io  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import posixpath  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402
import zipfile  # noqa: E402

import chung  # noqa: E402

TIEN_TO = 'xuong-viet-'
NGAY_CO_DINH = (2026, 1, 1, 0, 0, 0)
KHOA_BI_MAT = [r'sk-[A-Za-z0-9_-]{20,}', r'AKIA[0-9A-Z]{16}', r'AIza[0-9A-Za-z_-]{30,}',
               r'(?i)(mật khẩu|password|passwd)\s*[:=]\s*[^\s,.;]{6,}', r'-----BEGIN [A-Z ]*PRIVATE KEY-----',
               r'(?i)(số tài khoản|stk|cccd|cmnd|căn cước)\s*[:=]?\s*\d[\d .-]{7,}']


def ten_rieng(ten):
    return TIEN_TO + (ten[len('viet-'):] if ten.startswith('viet-') else ten)


def doc(p):
    with open(p, encoding='utf-8') as h:
        return h.read()


def tach_dau(s):
    m = re.match(r'^---\n(.*?)\n---\n', s, re.S)
    if not m:
        raise SystemExit('SKILL.md thiếu phần đầu YAML (---).')
    return m.group(1), s[m.end():]


def mo_ta_trong(fm):
    m = re.search(r'^description:\s*(.*?)(?=^\w[\w-]*:|\Z)', fm, re.M | re.S)
    if not m:
        return ''
    v = m.group(1).strip()
    if v.startswith('|') or v.startswith('>'):
        v = ' '.join(x.strip() for x in v[1:].splitlines())
    return v.strip().strip('"').replace('\\"', '"').strip()


def dau_moi(ten, mo_ta):
    mo_ta = mo_ta.replace('\\', '\\\\').replace('"', '\\"')
    return f'---\nname: {ten}\ndescription: "{mo_ta}"\n---\n'


def kiem_ten_mo_ta(ten, mo_ta, gioi_han, nguon):
    loi = []
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}', ten):
        loi.append(f'{nguon}: tên "{ten}" phải là chữ thường không dấu, số, gạch ngang, tối đa 64 ký tự')
    if not mo_ta:
        loi.append(f'{nguon}: thiếu mô tả')
    if len(mo_ta) > gioi_han:
        loi.append(f'{nguon}: mô tả dài {len(mo_ta)} ký tự, quá {gioi_han}')
    if '<' in mo_ta or '>' in mo_ta:
        loi.append(f'{nguon}: mô tả không được chứa dấu < hay >')
    return loi


def ds_skill(goc):
    thu_muc = os.path.join(goc, 'skills')
    return [t for t in sorted(os.listdir(thu_muc))
            if not t.startswith(('_', '.')) and os.path.isfile(os.path.join(thu_muc, t, 'SKILL.md'))]


def tep_cua_skill(goc, ten):
    """(đường trong gói, đường nguồn) cho SKILL.md và references/, scripts/, assets/ có sẵn trong thư mục skill."""
    nguon = os.path.join(goc, 'skills', ten)
    ra = []
    for dp, dn, fn in os.walk(nguon):
        dn[:] = sorted(d for d in dn if not d.startswith('.') and d != '__pycache__')
        for f in sorted(fn):
            if f in chung.BO_QUA_TEP or f.endswith('.pyc') or f == 'kem.json':
                continue
            p = os.path.join(dp, f)
            ra.append((os.path.relpath(p, nguon).replace(os.sep, '/'), p))
    return ra


def mo_rong(goc, bang):
    """Bảng {đích trong gói: nguồn trong xưởng}; nguồn kết thúc bằng / là cả thư mục."""
    ra = []
    for dich, nguon in bang.items():
        p = os.path.join(goc, nguon)
        if nguon.endswith('/'):
            if not os.path.isdir(p):
                raise SystemExit(f'kem.json trỏ tới thư mục không có: {nguon}')
            for dp, dn, fn in os.walk(p):
                dn[:] = sorted(d for d in dn if not d.startswith('.') and d != '__pycache__')
                for f in sorted(fn):
                    if f in chung.BO_QUA_TEP or f.endswith('.pyc'):
                        continue
                    q = os.path.join(dp, f)
                    ra.append((dich.rstrip('/') + '/' + os.path.relpath(q, p).replace(os.sep, '/'), q))
        else:
            ra.append((dich, p))
    return ra


def khoi_da_thiet_lap(goc, x, ngay):
    gv = os.path.join(goc, 'phong-cach', 'GIONG-VAN.md')
    t = doc(gv) if os.path.exists(gv) else ''
    m = re.search(r'^- Tên viết dưới bài.*?:\s*(.+)$', t, re.M)
    ten = m.group(1).strip() if m and '[...]' not in m.group(1) else '(chưa thiết lập)'
    mx = re.search(r'^- Trợ lý gọi bạn là:\s*(.+)$', t, re.M)
    xung_ho = (mx.group(1).strip() if mx and '[' not in mx.group(1) else '') \
        or x.get('xungHoNguoiDung') or '(chưa thiết lập)'
    lam_viec = x.get('thuMucLamViec') or '(chưa thiết lập)'

    def hien(khoa, mac_dinh):
        v = x.get(khoa) or mac_dinh
        if os.path.isabs(os.path.expanduser(v)) or lam_viec.startswith('('):
            return v
        return posixpath.normpath(posixpath.join(lam_viec, 'xuong-viet-ai', v))

    ten_skill = ', '.join(f'{t} là `{ten_rieng(t)}`' for t in ds_skill(goc))
    return (
        f'> **Đã thiết lập cho {ten}** (gói đóng ngày {ngay}, xưởng dựng từ bản vẽ {x.get("phienBan", "?")}).\n'
        f'> - Cấu hình đầy đủ: `phong-cach/GIONG-VAN.md` trong xưởng khi thư mục làm việc đã gắn vào phiên; chưa gắn '
        f'thì dùng bản chụp `references/GIONG-VAN.md` trong gói này. Hai bản lệch nhau thì theo bản trong xưởng. '
        f'Các mục bên dưới chỉ dùng cho điều tệp ấy chưa nói tới.\n'
        f'> - Gọi người dùng là "{xung_ho}".\n'
        f'> - Thư mục làm việc: `{lam_viec}`; xưởng: `{posixpath.join(lam_viec, "xuong-viet-ai")}`; kho tư liệu: '
        f'`{hien("thuMucKho", chung.KHO_MAC_DINH)}`; bài viết: `{hien("thuMucBai", chung.BAI_MAC_DINH)}`. '
        f'Thư mục chưa gắn vào phiên: nhắc người dùng gắn thư mục làm việc để dùng kho tư liệu và công cụ; vẫn làm '
        f'được phần hỏi, soạn, soi bằng bản chụp.\n'
        f'> - Tên skill trong tài khoản: {ten_skill}.\n'
    ), ten


def chen_khoi(than, khoi):
    m = re.search(r'^## Cấu hình cá nhân[^\n]*\n', than, re.M)
    if m:
        return than[:m.end()] + '\n' + khoi + '\n' + than[m.end():]
    m = re.search(r'^# [^\n]*\n', than, re.M)
    vi_tri = m.end() if m else 0
    return than[:vi_tri] + '\n## Cấu hình cá nhân\n\n' + khoi + '\n' + than[vi_tri:]


def quet_bi_mat(ten_tep, noi_dung):
    return [f'{ten_tep}: có dấu hiệu khóa hay mật khẩu ({mau})' for mau in KHOA_BI_MAT if re.search(mau, noi_dung)]


def ghi_zip(duong_zip, goc_trong_zip, muc):
    os.makedirs(os.path.dirname(duong_zip), exist_ok=True)
    with zipfile.ZipFile(duong_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        for ten_trong, du_lieu in muc:
            info = zipfile.ZipInfo(f'{goc_trong_zip}/{ten_trong}', NGAY_CO_DINH)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, du_lieu)


def dong_goi(goc, ten, che_do, mo_ta_day_du, x, ngay, chi_giong_van=False):
    kem = json.load(open(os.path.join(goc, 'skills', ten, 'kem.json'), encoding='utf-8'))
    fm, than = tach_dau(doc(os.path.join(goc, 'skills', ten, 'SKILL.md')))
    mo_ta_full = mo_ta_trong(fm)
    loi = kiem_ten_mo_ta(ten, mo_ta_full, 1024, f'skills/{ten}/SKILL.md')
    loi += kiem_ten_mo_ta(ten, kem.get('moTaNgan', ''), 200, f'skills/{ten}/kem.json moTaNgan')
    ten_goi = ten_rieng(ten) if che_do == 'rieng' else ten
    canh_bao = []
    if che_do == 'rieng':
        khoi, ten_nguoi = khoi_da_thiet_lap(goc, x, ngay)
        if ten_nguoi.startswith('('):
            canh_bao.append('cấu hình cá nhân còn thiếu: tên viết dưới bài trong phong-cach/GIONG-VAN.md mục 1')
        than = chen_khoi(than, khoi)
    mo_ta = mo_ta_full if mo_ta_day_du else kem['moTaNgan']
    skill_md = dau_moi(ten_goi, mo_ta) + than
    muc = [('SKILL.md', skill_md.encode('utf-8'))]
    for trong, p in tep_cua_skill(goc, ten):
        if trong != 'SKILL.md':
            muc.append((trong, open(p, 'rb').read()))
    for trong, p in mo_rong(goc, kem.get('kem', {})):
        muc.append((trong, open(p, 'rb').read()))
    if che_do == 'rieng':
        chup = []
        for trong, p in mo_rong(goc, kem.get('chup', {})):
            if chi_giong_van and not p.endswith('GIONG-VAN.md'):
                continue
            if not os.path.exists(p):
                canh_bao.append(f'chưa có {os.path.relpath(p, goc)} để chụp vào gói (chạy python3 tools/cai-dat.py)')
                continue
            b = open(p, 'rb').read()
            loi += quet_bi_mat(os.path.relpath(p, goc), b.decode('utf-8', 'replace'))
            muc.append((trong, b))
            chup.append((trong, os.path.relpath(p, goc), hashlib.sha256(b).hexdigest()[:12]))
        dau_goi = hashlib.sha256(b''.join(hashlib.sha256(d).digest() for _, d in sorted(muc))).hexdigest()[:16]
        dg = io.StringIO()
        dg.write(f'# Gói skill {ten_goi}\n\nĐóng gói ngày {ngay} bằng `tools/dong-goi-skill.py`, từ skill nguồn '
                 f'`skills/{ten}/` của xưởng (bản vẽ {x.get("phienBan", "?")}). Dấu gói: `{dau_goi}`.\n\n'
                 'Tệp chụp từ phần riêng của xưởng (bản chụp lúc đóng gói; bản trong xưởng mới hơn thì theo bản trong '
                 'xưởng):\n\n')
        for trong, nguon, h in chup:
            dg.write(f'- `{trong}` từ `{nguon}` (vân tay {h})\n')
        muc.append(('references/DONG-GOI.md', dg.getvalue().encode('utf-8')))
    for trong, du_lieu in muc:
        if trong.endswith(('.md', '.json', '.py', '.txt')) and che_do == 'chung':
            loi += quet_bi_mat(f'{ten}/{trong}', du_lieu.decode('utf-8', 'replace'))
    return ten_goi, muc, mo_ta_full, loi, canh_bao


def main():
    ap = argparse.ArgumentParser(description='Đóng gói skill của Xưởng viết AI.')
    ap.add_argument('--chung', action='store_true', help='ở bản vẽ: gói chung vào dong-goi/')
    ap.add_argument('--mo-ta-day-du', action='store_true', help='giữ mô tả đầy đủ trong gói .zip')
    ap.add_argument('--ra', help='thư mục ghi gói (mặc định: <thư mục bài>/_skill, hoặc dong-goi/ với --chung)')
    ap.add_argument('--chi-giong-van', action='store_true',
                    help='gói riêng chỉ chụp giọng văn, không chụp bài học giọng và hồ sơ người viết')
    a = ap.parse_args()
    goc = chung.GOC
    ngay = chung.hom_nay()
    if a.chung:
        if chung.la_xuong(goc):
            raise SystemExit('DỪNG: --chung chỉ chạy ở bản vẽ; trong xưởng đã dựng, bỏ --chung để đóng gói skill riêng.')
        che_do, x = 'chung', {}
        ra = os.path.abspath(a.ra) if a.ra else os.path.join(goc, 'dong-goi')
    else:
        chung.dung_neu_ban_ve('dong-goi-skill.py (không có --chung)')
        if not chung.la_xuong(goc):
            raise SystemExit('DỪNG: chưa có XUONG.json; dựng xưởng theo DUNG-XUONG.md trước.')
        che_do, x = 'rieng', chung.nap_xuong(goc)
        ra = os.path.abspath(a.ra) if a.ra else os.path.join(chung.thu_muc_bai(goc), '_skill')
    tat_ca_loi, tat_ca_canh_bao, ket_qua = [], [], []
    goi = [dong_goi(goc, t, che_do, a.mo_ta_day_du, x, ngay, a.chi_giong_van) + (t,) for t in ds_skill(goc)]
    for ten_goi, muc, mo_ta_full, loi, canh_bao, ten in goi:
        tat_ca_loi += loi
        tat_ca_canh_bao += canh_bao
    if tat_ca_loi:
        for l in tat_ca_loi:
            print('  LỖI: ' + l)
        print('\nĐÓNG GÓI: KHÔNG ĐẠT (chưa ghi gói nào).')
        sys.exit(1)
    os.makedirs(ra, exist_ok=True)
    phang = os.path.join(ra, 'tep-cho-du-an')
    if che_do == 'chung':
        if os.path.isdir(phang):
            for f in os.listdir(phang):
                if f.endswith('.md'):
                    os.remove(os.path.join(phang, f))
        os.makedirs(phang, exist_ok=True)
    for ten_goi, muc, mo_ta_full, loi, canh_bao, ten in goi:
        ghi_zip(os.path.join(ra, ten_goi + '.zip'), ten_goi, muc)
        if che_do == 'rieng':
            xem = os.path.join(ra, ten_goi)
            if os.path.isdir(xem) and os.path.exists(os.path.join(xem, 'references', 'DONG-GOI.md')):
                shutil.rmtree(xem)
            for trong, du_lieu in muc:
                p = os.path.join(xem, *trong.split('/'))
                os.makedirs(os.path.dirname(p), exist_ok=True)
                open(p, 'wb').write(du_lieu)
        else:
            for trong, du_lieu in muc:
                if trong == 'SKILL.md':
                    fm, than = tach_dau(du_lieu.decode('utf-8'))
                    open(os.path.join(phang, ten + '.md'), 'w', encoding='utf-8').write(dau_moi(ten, mo_ta_full) + than)
                elif trong.startswith('references/') and trong.endswith('.md') and trong.count('/') == 1:
                    open(os.path.join(phang, f'{ten}--{trong.split("/")[1]}'), 'wb').write(du_lieu)
        ket_qua.append(f'  ✓ {ten_goi}.zip ({len(muc)} tệp)')
    print('\n'.join(ket_qua))
    for c in dict.fromkeys(tat_ca_canh_bao):
        print('  CẢNH BÁO: ' + c)
    print(f'\nĐÓNG GÓI: ĐẠT, {len(goi)} gói trong {ra}' + (' (kèm tep-cho-du-an/)' if che_do == 'chung' else ''))


if __name__ == '__main__':
    main()

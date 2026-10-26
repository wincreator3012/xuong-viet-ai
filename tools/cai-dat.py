#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CÀI ĐẶT xưởng viết đã dựng: tạo phần riêng của người dùng, kho tư liệu, thư mục bài; báo trạng thái; ghi dấu bước.

    python3 tools/cai-dat.py                       # tạo những gì còn thiếu (không bao giờ ghi đè tệp đã có)
    python3 tools/cai-dat.py --khong-tao-ngan      # kho là một thư mục ghi chép có sẵn (ví dụ kho Obsidian):
                                                   #   chỉ thêm HUONG-DAN-KHO.md (bản cho kho có sẵn) và MUC-LUC.md,
                                                   #   không thêm sáu ngăn, ghi XUONG.json > khoCoSan = true
    tuỳ chọn: --kho <thư mục kho>  (đường dẫn kho mà phiên này thấy, khi khác đường dẫn trong XUONG.json, ví dụ
              trong máy ảo Cowork; kho nằm ngoài thư mục làm việc phải tồn tại sẵn, công cụ không tự tạo)
    python3 tools/cai-dat.py --trang-thai          # xưởng đang ở bước nào
    python3 tools/cai-dat.py --danh-dau <bước>     # thiet-lap | kho | skill | gioi-thieu

Tạo gì (chỉ khi chưa có):
  phong-cach/GIONG-VAN.md, bai-hoc-giong.md, ho-so-nguoi-viet.md   từ bản khởi đầu *.mau.md cùng thư mục
  <kho tư liệu> (XUONG.json > thuMucKho, mặc định ../Kho tu lieu)  từ khuon/kho-tu-lieu/
  <thư mục bài> (XUONG.json > thuMucBai, mặc định ../Bai viet)     kèm _skill/, _tam/, HUONG-DAN-BAI-VIET.md
Chạy nhiều lần vô hại. Python 3.9+, chỉ thư viện chuẩn.
"""
import sys
sys.dont_write_bytecode = True
import argparse  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import shutil  # noqa: E402

import chung  # noqa: E402

BUOC = ['thiet-lap', 'kho', 'skill', 'gioi-thieu']
TEN_BUOC = {'thiet-lap': 'Thiết lập giọng văn', 'kho': 'Kho tư liệu đã có tư liệu đầu tiên',
            'skill': 'Bộ skill riêng', 'gioi-thieu': 'Giới thiệu xưởng'}


def chep_neu_thieu(nguon, dich, bao):
    if os.path.exists(dich):
        return False
    os.makedirs(os.path.dirname(dich), exist_ok=True)
    shutil.copyfile(nguon, dich)
    bao.append(dich)
    return True


def cai(a):
    goc = chung.GOC
    if sys.version_info < (3, 9):
        raise SystemExit(f'Cần Python 3.9 trở lên (đang có {sys.version.split()[0]}).')
    bao = []
    # 1. phần riêng trong xưởng
    pc = os.path.join(goc, 'phong-cach')
    for f in sorted(os.listdir(pc)):
        if f.endswith('.mau.md'):
            chep_neu_thieu(os.path.join(pc, f), os.path.join(pc, f.replace('.mau.md', '.md')), bao)
    # 2. kho tư liệu
    kho = chung.thu_muc_kho(goc, ep=a.kho)
    lam_viec = os.path.dirname(goc)
    trong_lam_viec = os.path.commonpath([os.path.abspath(kho), lam_viec]) == lam_viec
    if not os.path.isdir(kho) and (a.kho or not trong_lam_viec):
        raise SystemExit(f'DỪNG: không thấy thư mục kho {kho}. Kho nằm ngoài thư mục làm việc phải có sẵn và được gắn '
                         'vào phiên; trong máy ảo, truyền --kho <đường dẫn máy ảo thấy>. Công cụ không tự tạo thư mục ấy.')
    os.makedirs(kho, exist_ok=True)
    khuon_kho = os.path.join(goc, 'khuon', 'kho-co-san' if a.khong_tao_ngan else 'kho-tu-lieu')
    if a.khong_tao_ngan:
        x = chung.nap_xuong(goc)
        if not x.get('khoCoSan'):
            x['khoCoSan'] = True
            chung.ghi_xuong(x, goc)
    for dp, dn, fn in os.walk(khuon_kho):
        rel_dir = os.path.relpath(dp, khuon_kho)
        for f in fn:
            if f in chung.BO_QUA_TEP:
                continue
            chep_neu_thieu(os.path.join(dp, f), os.path.normpath(os.path.join(kho, rel_dir, f)), bao)
    # 3. thư mục bài
    bai = chung.thu_muc_bai(goc)
    for d in (bai, os.path.join(bai, '_skill'), os.path.join(bai, '_tam')):
        if not os.path.isdir(d):
            os.makedirs(d, exist_ok=True)
            bao.append(d + os.sep)
    chep_neu_thieu(os.path.join(goc, 'khuon', 'bai-viet', 'HUONG-DAN-BAI-VIET.md'),
                   os.path.join(bai, 'HUONG-DAN-BAI-VIET.md'), bao)
    for d in bao:
        print('  + ' + os.path.relpath(d, lam_viec) + (os.sep if d.endswith(os.sep) else ''))
    print(f'\nKho tư liệu: {kho}\nThư mục bài: {bai}')
    print(f'\nCÀI XONG: tạo {len(bao)} mục mới' + (' (mọi thứ đã có sẵn từ trước)' if not bao else '') + '.')


def cho_trong(van_ban):
    return len(re.findall(r'\[[^\]\n]*\.\.\.[^\]\n]*\]|\[(?:ngày|tên người viết)\]', van_ban))


def trang_thai(a):
    goc = chung.GOC
    x = chung.nap_xuong(goc)
    print(f'Xưởng: {goc}')
    print(f'  dựng từ bản vẽ phiên bản {x.get("phienBan", "?")}, ngày dựng {x.get("ngayDung", "?")}, '
          f'cập nhật {x.get("ngayCapNhat", "?")}')
    gv = os.path.join(goc, 'phong-cach', 'GIONG-VAN.md')
    if not os.path.exists(gv):
        print('Giọng văn: CHƯA CÓ phong-cach/GIONG-VAN.md (chạy python3 tools/cai-dat.py)')
    else:
        t = open(gv, encoding='utf-8').read()
        ten = re.search(r'^- Tên viết dưới bài.*?:\s*(.+)$', t, re.M)
        co_ten = bool(ten) and '[...]' not in ten.group(1)
        print(f'Giọng văn: {"đã thiết lập" if co_ten else "CHƯA THIẾT LẬP"} '
              f'(còn {cho_trong(t)} chỗ trống; trợ lý hỏi dần, không đoán)')
    kho = chung.thu_muc_kho(goc, ep=a.kho)
    if not os.path.isdir(kho):
        print(f'Kho tư liệu: CHƯA CÓ hoặc phiên chưa thấy ({kho})')
    else:
        tl = chung.tep_tu_lieu(kho)
        ml = {p for p, _ in chung.dong_muc_luc(kho)}
        theo_ngan = {}
        for r in tl:
            ngan = r.split('/')[0] if '/' in r else '(gốc kho)'
            theo_ngan[ngan] = theo_ngan.get(ngan, 0) + 1
        chua = [r for r in tl if r not in ml]
        print(f'Kho tư liệu: {kho}')
        print(f'  {len(tl)} tư liệu, {len(ml)} dòng mục lục, {len(chua)} tư liệu chưa vào mục lục')
        if not x.get('khoCoSan'):
            for n in sorted(theo_ngan):
                print(f'    {n}: {theo_ngan[n]}')
    bai = chung.thu_muc_bai(goc)
    if os.path.isdir(bai):
        ds = [d for d in os.listdir(bai) if os.path.isdir(os.path.join(bai, d)) and not d.startswith(('_', '.'))]
        chot = [d for d in ds if os.path.exists(os.path.join(bai, d, 'ban-chot.md'))]
        goi = [f for f in os.listdir(os.path.join(bai, '_skill')) if f.endswith('.zip')] \
            if os.path.isdir(os.path.join(bai, '_skill')) else []
        print(f'Bài viết: {bai}\n  {len(ds)} bài, {len(chot)} bài đã chốt; {len(goi)} gói skill trong _skill/')
    else:
        print(f'Bài viết: CHƯA CÓ ({bai})')
    buoc = x.get('buoc', {})
    print('Các bước:')
    for b in BUOC:
        print(f'  {TEN_BUOC[b]}: ' + (f'đã ({buoc[b]})' if b in buoc else 'chưa'))


def danh_dau(b):
    if b not in BUOC:
        raise SystemExit('Bước phải là một trong: ' + ', '.join(BUOC))
    x = chung.nap_xuong()
    x.setdefault('buoc', {})[b] = chung.hom_nay()
    chung.ghi_xuong(x)
    print(f'✓ ghi dấu: {TEN_BUOC[b]} ({x["buoc"][b]})')


def main():
    ap = argparse.ArgumentParser(description='Cài đặt và trạng thái của xưởng viết đã dựng.')
    ap.add_argument('--trang-thai', action='store_true')
    ap.add_argument('--danh-dau', metavar='BUOC')
    ap.add_argument('--khong-tao-ngan', action='store_true',
                    help='kho là thư mục ghi chép có sẵn: chỉ thêm HUONG-DAN-KHO.md và MUC-LUC.md')
    ap.add_argument('--kho', help='thư mục kho mà phiên này thấy (mặc định theo XUONG.json > thuMucKho)')
    a = ap.parse_args()
    chung.dung_neu_ban_ve('cai-dat.py')
    if not chung.la_xuong():
        raise SystemExit('DỪNG: chưa có XUONG.json ở gốc xưởng. Viết XUONG.json theo DUNG-XUONG.md bước 4 trước.')
    if a.trang_thai:
        trang_thai(a)
    elif a.danh_dau:
        danh_dau(a.danh_dau)
    else:
        cai(a)


if __name__ == '__main__':
    main()

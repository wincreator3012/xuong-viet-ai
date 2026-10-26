# -*- coding: utf-8 -*-
"""Phần dùng chung cho công cụ của Xưởng viết AI: tìm gốc xưởng, đọc XUONG.json, đường dẫn kho tư liệu và thư mục bài.

Các công cụ đặt sys.dont_write_bytecode = True trước khi import tệp này, để không sinh __pycache__ trong xưởng.
Python 3.9+, chỉ thư viện chuẩn.
"""
import datetime
import json
import os
import re
import sys
import unicodedata

sys.dont_write_bytecode = True
for _luong in (sys.stdout, sys.stderr):  # Windows: in chữ có dấu không lỗi
    try:
        _luong.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

TOOLS = os.path.dirname(os.path.abspath(__file__))
GOC = os.path.dirname(TOOLS)

KHO_MAC_DINH = '../Kho tu lieu'
BAI_MAC_DINH = '../Bai viet'
TEP_HUONG_DAN_KHO = {'HUONG-DAN-KHO.md', 'MUC-LUC.md'}
BO_QUA_TEP = {'.DS_Store', 'Thumbs.db', 'desktop.ini'}


def nfc(s):
    return unicodedata.normalize('NFC', s)


def khong_dau(s):
    s = unicodedata.normalize('NFD', nfc(s).replace('đ', 'd').replace('Đ', 'D'))
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')


def rut_gon(s):
    """Chữ thường, bỏ dấu, gộp khoảng trắng: để so khớp khi tìm."""
    return re.sub(r'\s+', ' ', khong_dau(s).lower()).strip()


def slug(s, toi_da=60):
    s = re.sub(r'[^a-z0-9]+', '-', khong_dau(s).lower()).strip('-')
    return (s[:toi_da].rstrip('-')) or 'bai-moi'


def hom_nay():
    return datetime.date.today().isoformat()


def la_xuong(goc=GOC):
    return os.path.exists(os.path.join(goc, 'XUONG.json'))


def la_ban_ve(goc=GOC):
    return os.path.exists(os.path.join(goc, 'DUNG-XUONG.md')) and not la_xuong(goc)


def nap_xuong(goc=GOC):
    p = os.path.join(goc, 'XUONG.json')
    if not os.path.exists(p):
        return {}
    try:
        with open(p, encoding='utf-8') as h:
            return json.load(h)
    except ValueError as e:
        raise SystemExit(f'DỪNG: XUONG.json không đọc được ({e}). Mở tệp, sửa chỗ hỏng (thường là thiếu dấu phẩy '
                         'hay ngoặc kép), rồi chạy lại.')


def ghi_xuong(d, goc=GOC):
    with open(os.path.join(goc, 'XUONG.json'), 'w', encoding='utf-8', newline='\n') as h:
        json.dump(d, h, ensure_ascii=False, indent=1)
        h.write('\n')


def _giai(goc, gia_tri):
    gia_tri = os.path.expanduser(gia_tri)
    return os.path.normpath(gia_tri if os.path.isabs(gia_tri) else os.path.join(goc, gia_tri))


def thu_muc_kho(goc=GOC, ep=None):
    if ep:
        return os.path.abspath(os.path.expanduser(ep))
    return _giai(goc, nap_xuong(goc).get('thuMucKho') or KHO_MAC_DINH)


def thu_muc_bai(goc=GOC, ep=None):
    if ep:
        return os.path.abspath(os.path.expanduser(ep))
    return _giai(goc, nap_xuong(goc).get('thuMucBai') or BAI_MAC_DINH)


def dung_neu_ban_ve(viec):
    if la_ban_ve():
        raise SystemExit(f'DỪNG: đây là bản vẽ (có DUNG-XUONG.md, chưa có XUONG.json), không phải xưởng; {viec} chỉ '
                         'chạy trong xưởng đã dựng. Dựng xưởng ở thư mục làm việc khác theo DUNG-XUONG.md.')


def tep_tu_lieu(kho, kem_duong_that=False):
    """Mọi tệp tư liệu trong kho (đường dẫn tương đối, NFC), bỏ tệp hướng dẫn, tệp ẩn, tệp hệ thống.
    kem_duong_that=True: trả về cặp (đường dẫn NFC, đường dẫn thật trên đĩa), vì tên tệp có dấu có thể lưu dạng NFD."""
    ra = []
    for dp, dn, fn in os.walk(kho):
        dn[:] = sorted(d for d in dn if not d.startswith('.') and not d.startswith('_'))
        for f in sorted(fn):
            if f in BO_QUA_TEP or f.startswith('.') or f.startswith('_') or f.startswith('~$'):
                continue
            that = os.path.join(dp, f)
            rel = nfc(os.path.relpath(that, kho).replace(os.sep, '/'))
            if rel in TEP_HUONG_DAN_KHO:
                continue
            ra.append((rel, that) if kem_duong_that else rel)
    return ra


def dong_muc_luc(kho):
    """Các dòng của bảng trong MUC-LUC.md: danh sách (đường dẫn tệp, dòng gốc). Bỏ dòng tiêu đề và dòng kẻ."""
    p = os.path.join(kho, 'MUC-LUC.md')
    if not os.path.exists(p):
        return []
    ra = []
    for dong in open(p, encoding='utf-8').read().splitlines():
        dong = nfc(dong.strip())
        if not dong.startswith('|') or set(dong) <= set('|-: '):
            continue
        o = [x.strip() for x in dong.strip('|').split('|')]
        if not o or o[0] in ('Tệp', ''):
            continue
        m = re.match(r'`([^`]+)`', o[0])
        ra.append((nfc(m.group(1)) if m else o[0], dong))
    return ra

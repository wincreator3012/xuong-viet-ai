#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KIỂM SẠCH: xưởng (hay bản vẽ) chỉ chứa năng lực và phần riêng đúng chỗ; bài viết, tư liệu, việc tạm nằm ngoài.

    python3 tools/kiem-sach.py

Trong xưởng đã dựng: mọi tệp phải thuộc danh mục BAN-DUNG.json (nhóm chép) hoặc phần riêng của người dùng
(XUONG.json, BAN-DUNG.json, CLAUDE.md, AGENTS.md, phong-cach/*.md). Tệp khác là lạc chỗ: báo ra để trợ lý chuyển về
thư mục bài hay kho tư liệu, hoặc hỏi người dùng. Công cụ không xóa, không chuyển gì.
Ở bản vẽ: không được có phần riêng của ai (XUONG.json, phong-cach/*.md không phải bản .mau), không có rác hệ thống.
"""
import sys
sys.dont_write_bytecode = True
import fnmatch  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402

import chung  # noqa: E402

RIENG = ['XUONG.json', 'BAN-DUNG.json', 'CLAUDE.md', 'AGENTS.md', 'phong-cach/*.md']
RAC = {'.DS_Store', 'Thumbs.db', 'desktop.ini'}


def tat_ca_tep(goc):
    ra, rac = [], []
    for dp, dn, fn in os.walk(goc):
        for d in list(dn):
            if d in ('.git',):
                dn.remove(d)
            elif d == '__pycache__':
                rac.append(os.path.relpath(os.path.join(dp, d), goc) + '/')
                dn.remove(d)
        for f in fn:
            rel = chung.nfc(os.path.relpath(os.path.join(dp, f), goc).replace(os.sep, '/'))
            (rac if f in RAC or f.endswith('.pyc') else ra).append(rel)
    return sorted(ra), sorted(rac)


def main():
    goc = chung.GOC
    tep, rac = tat_ca_tep(goc)
    lac = []
    if chung.la_xuong(goc):
        p = os.path.join(goc, 'BAN-DUNG.json')
        chep = set()
        if os.path.exists(p):
            chep = {chung.nfc(t['duong']) for t in json.load(open(p, encoding='utf-8'))['tep'] if t['loai'] == 'chep'}
        else:
            print('CẢNH BÁO: chưa có BAN-DUNG.json trong xưởng; chỉ kiểm được rác hệ thống.')
        for rel in tep:
            if chep and rel not in chep and not any(fnmatch.fnmatch(rel, g) for g in RIENG):
                lac.append(rel)
        lam_viec = os.path.dirname(goc)
        if os.path.isdir(os.path.join(lam_viec, 'Claude outputs')):
            print(f'Ghi chú: có thư mục "Claude outputs" trong {lam_viec}: ứng dụng Claude tự chép tệp gửi vào chat '
                  'ra đó; là rác của phiên, hỏi người dùng trước khi dọn.')
        noi = 'xưởng'
    else:
        for rel in tep:
            if rel == 'XUONG.json' or (rel.startswith('phong-cach/') and not rel.endswith('.mau.md')):
                lac.append(rel)
        noi = 'bản vẽ'
    if lac:
        print(f'Lạc chỗ trong {noi} ({len(lac)}): bài, tư liệu, việc tạm thuộc thư mục bài hay kho, không thuộc {noi}.')
        for r in lac:
            print('  ' + r)
    if rac:
        print(f'Rác hệ thống ({len(rac)}): xin phép người dùng một lần rồi mới xóa.')
        for r in rac:
            print('  ' + r)
    dat = not lac and not rac
    print(f'\nKIỂM SẠCH ({noi}): ' + ('ĐẠT' if dat else 'KHÔNG ĐẠT'))
    sys.exit(0 if dat else 1)


if __name__ == '__main__':
    main()

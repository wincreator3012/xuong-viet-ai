#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""BÀI MỚI: tạo thư mục cho một bài trong thư mục bài viết của người dùng (ngoài xưởng).

    python3 tools/bai-moi.py "Khi thầy cô nói tôi chưa biết"
    python3 tools/bai-moi.py "Tên bài" --ngay 2026-11-02

Tạo <thư mục bài>/<ngày> <tên-không-dấu>/ gồm chat-lieu.md (từ khuon/bai-viet/mot-bai/) và ban-nhap/.
Thư mục của chính bài ấy (cùng tên) đã có thì giữ nguyên; tên khác mà trùng thư mục thì thêm hậu tố -2, -3. In đường dẫn thư mục bài ở dòng cuối.
"""
import sys
sys.dont_write_bytecode = True
import argparse  # noqa: E402
import datetime  # noqa: E402
import os  # noqa: E402

import chung  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description='Tạo thư mục cho một bài viết mới.')
    ap.add_argument('ten')
    ap.add_argument('--ngay', default=None, help='YYYY-MM-DD, mặc định hôm nay')
    ap.add_argument('--bai', help='thư mục bài viết (mặc định theo XUONG.json > thuMucBai)')
    a = ap.parse_args()
    chung.dung_neu_ban_ve('bai-moi.py')
    ngay = a.ngay or chung.hom_nay()
    try:
        datetime.date.fromisoformat(ngay)
    except ValueError:
        raise SystemExit('--ngay phải là một ngày có thật, dạng YYYY-MM-DD.')
    goc_bai = chung.thu_muc_bai(ep=a.bai)
    os.makedirs(goc_bai, exist_ok=True)
    ten = chung.nfc(a.ten.strip())
    goc_ten = f'{ngay} {chung.slug(ten)}'
    dich, so = os.path.join(goc_bai, goc_ten), 1
    while os.path.isdir(dich):
        cl = os.path.join(dich, 'chat-lieu.md')
        dau = chung.nfc(open(cl, encoding='utf-8').readline().strip()) if os.path.exists(cl) else ''
        if dau == f'# {ten}':
            print(f'Đã có thư mục của chính bài này, giữ nguyên:\n{dich}')
            return
        so += 1
        dich = os.path.join(goc_bai, f'{goc_ten}-{so}')
    os.makedirs(os.path.join(dich, 'ban-nhap'))
    mau = open(os.path.join(chung.GOC, 'khuon', 'bai-viet', 'mot-bai', 'chat-lieu.md'), encoding='utf-8').read()
    mau = mau.replace('[Tên bài]', ten, 1).replace('[ngày]', ngay, 1)
    with open(os.path.join(dich, 'chat-lieu.md'), 'w', encoding='utf-8', newline='\n') as h:
        h.write(mau)
    print(f'✓ tạo thư mục bài (chat-lieu.md, ban-nhap/):\n{dich}')


if __name__ == '__main__':
    main()

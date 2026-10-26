#!/usr/bin/env python3
"""Chuẩn hóa vị trí dấu thanh theo kiểu cũ cho cụm oa, oe, uy ở cuối âm tiết.

  hoá -> hóa, hoà -> hòa, toả -> tỏa, hoạ -> họa, khoẻ -> khỏe,
  thuỷ -> thủy, tuý -> túy, huỷ -> hủy, tuỳ -> tùy

Giữ nguyên khi có âm theo sau hoặc khi u thuộc "qu":
  hoàn, hoàng, khoảng, hoài, huỳnh, khuỷu, thuyền, quý, quỳ, quả.
Văn bản được đưa về dạng Unicode dựng sẵn (NFC) trước khi xử lý.

Dùng:
  python3 tools/chuan-hoa-dau-thanh.py file1.md file2.md      # chạy thử, chỉ báo
  python3 tools/chuan-hoa-dau-thanh.py --write file1.md ...    # ghi đè
"""
import re
import sys
import unicodedata

TONES = '̣́̀̉̃'  # sắc, huyền, hỏi, ngã, nặng
LETTER = r'[^\W\d_]'


def build():
    pats = []
    for v1, v2 in (('oO', 'aA'), ('oO', 'eE'), ('uU', 'yY')):
        toned = ''.join(unicodedata.normalize('NFC', b + t) for b in v2 for t in TONES)
        guard = r'(?<![qQ])' if v1 == 'uU' else ''
        pats.append(guard + '([' + v1 + '])([' + toned + '])(?!' + LETTER + ')')
    return re.compile('|'.join('(?:%s)' % p for p in pats))


RX = build()


def fix(m):
    v1, v2 = [x for x in m.groups() if x is not None]
    d = unicodedata.normalize('NFD', v2)
    return unicodedata.normalize('NFC', v1 + d[1:]) + d[0]


def run(text):
    return RX.subn(fix, unicodedata.normalize('NFC', text))


if __name__ == '__main__':
    write = '--write' in sys.argv
    total = 0
    for f in [a for a in sys.argv[1:] if a != '--write']:
        s = open(f, encoding='utf-8').read()
        new, n = run(s)
        total += n
        if n or new != s:
            ex = sorted(set(m.group(0) for m in RX.finditer(unicodedata.normalize('NFC', s))))
            print(f'{f}: {n} chỗ  {" ".join(ex[:30])}')
            if write:
                open(f, 'w', encoding='utf-8').write(new)
    print('Tổng:', total, '(đã ghi)' if write else '(chạy thử)')

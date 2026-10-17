#!/usr/bin/env python3
"""Đối chiếu nguyên văn: mọi đoạn "văn bản đang dàn" trong file đề xuất sửa phải tìm thấy
trong văn bản trích từ file dàn trang.

Cách dùng:
    pdftotext -layout ban-dan.pdf ban-dan.txt      (hoặc bất kỳ cách trích văn bản nào)
    python3 doi-chieu-nguyen-van.py de-xuat.md ban-dan.txt

Script nhận hai kiểu đánh dấu trong file đề xuất:
  1. Khối bắt đầu bằng dòng "**Văn bản đang dàn:**" và kết thúc ở dòng "**Đề xuất sửa:**".
  2. Bảng Markdown có cột tên "Văn bản đang dàn" (đổi bằng --cot).

Đoạn có "[...]" được tách thành nhiều mảnh, mỗi mảnh đối chiếu riêng. Dòng nằm trọn trong
ngoặc vuông (ghi chú như "[tr. 64 chỉ có tiêu đề chạy]") được bỏ qua.

Kết quả: danh sách mảnh không tìm thấy, kèm tỷ lệ độ dài phần đầu khớp được, để biết là lệch
một chữ hay lệch cả câu. Với bản dàn có nhãn lề (như "Vì sao / hiệu quả" chen giữa dòng) hay
bảng nhiều cột, văn bản trích từ PDF có thể xen chữ lạ vào câu: mảnh khớp phần lớn rồi lệch
thường là báo động giả do cách trích, cần mở trang để xem. Script chỉ kiểm bề mặt; nghĩa của
câu vẫn phải đọc.
"""
import argparse
import re
import sys


def chuan(s):
    s = s.replace('­', '')
    s = re.sub(r'-\s*\n\s*', '-', s)
    return ' '.join(s.split())


def tach_hang(l):
    o = []
    cur = ''
    i = 0
    while i < len(l):
        if l[i] == '\\' and i + 1 < len(l) and l[i + 1] == '|':
            cur += '|'
            i += 2
            continue
        if l[i] == '|':
            o.append(cur)
            cur = ''
        else:
            cur += l[i]
        i += 1
    o.append(cur)
    return [x.strip() for x in o[1:-1]]


def lay_doan(md, ten_cot):
    doan = []
    dong = md.split('\n')
    trong_khoi = False
    buf = []
    cot = None
    ma = None
    for n, l in enumerate(dong, 1):
        s = l.strip()
        m = re.match(r'#+ .*?\(?([A-ZĐ]{0,3}\d+)\)?\.', s)
        if m:
            ma = m.group(1)
        if s == '**Văn bản đang dàn:**':
            trong_khoi = True
            buf = []
            bat_dau = n
            continue
        if trong_khoi and s == '**Đề xuất sửa:**':
            trong_khoi = False
            doan.append((ma or '?', bat_dau, '\n'.join(buf)))
            continue
        if trong_khoi:
            buf.append(l)
            continue
        if s.startswith('|'):
            o = tach_hang(s)
            if ten_cot in o:
                cot = o.index(ten_cot)
                continue
            if cot is not None and len(o) > cot and not set(o[0]) <= set('-: '):
                doan.append((o[0], n, o[cot].replace('<br>', '\n')))
        else:
            cot = None if not s else cot
    return doan


def manh(text):
    out = []
    for dong in text.split('\n'):
        d = dong.strip()
        if not d or (d.startswith('[') and d.endswith(']')):
            continue
        d = d.strip('"').strip()
        for p in re.split(r'\[\.\.\.\]|\[…\]', d):
            p = p.strip(' "')
            if len(p) >= 12:
                out.append(p)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('de_xuat')
    ap.add_argument('ban_dan_txt')
    ap.add_argument('--cot', default='Văn bản đang dàn')
    a = ap.parse_args()
    ban_dan = chuan(open(a.ban_dan_txt, encoding='utf-8').read())
    md = open(a.de_xuat, encoding='utf-8').read()
    loi = 0
    tong = 0
    for ma, n, text in lay_doan(md, a.cot):
        for p in manh(text):
            tong += 1
            q = chuan(p)
            if q in ban_dan:
                continue
            k = 0
            while k < len(q) and q[:k + 1] in ban_dan:
                k += 1
            loi += 1
            print(f'[{ma}] dòng {n}: khớp {k}/{len(q)} ký tự đầu: {q[:90]}')
    print(f'Đã đối chiếu {tong} mảnh; {loi} mảnh không tìm thấy nguyên văn.')
    sys.exit(1 if loi else 0)


if __name__ == '__main__':
    main()

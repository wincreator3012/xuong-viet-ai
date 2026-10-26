#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KHO TƯ LIỆU: rà và tìm trong kho tư liệu nguyên bản của người viết. Công cụ chỉ đọc, không sửa, không chuyển tệp.

    python3 tools/kho.py --quet                    # tư liệu chưa vào mục lục, dòng mục lục mất tệp, ngăn "0 Moi them"
    python3 tools/kho.py --tim hoc tro cau hoi     # tìm tư liệu chứa đủ mọi từ (không phân biệt dấu, hoa thường) trong
                                                   #   mục lục, tên tệp và nội dung tệp chữ (.md, .txt)
    tuỳ chọn: --kho <thư mục kho> (mặc định theo XUONG.json > thuMucKho)   --toi-da <số dòng in ra, mặc định 20>

Riêng tư: kết quả tìm luôn kèm cột "Riêng tư" của mục lục. Tư liệu ghi "chỉ để mình đọc" hay "cần hỏi đồng ý" chỉ in
đường dẫn và mức riêng tư, không in trích đoạn; trợ lý hỏi người viết trước khi mở tệp ấy.
"""
import sys
sys.dont_write_bytecode = True
import argparse  # noqa: E402
import os  # noqa: E402

import chung  # noqa: E402

DUOI_CHU = ('.md', '.txt')
KHONG_TRICH = ('chi de minh doc', 'can hoi dong y')


def cot_rieng_tu(dong_ml):
    o = [x.strip() for x in dong_ml.strip('|').split('|')] if dong_ml else []
    return o[4] if len(o) > 4 and o[4] else ('chưa ghi' if dong_ml else 'chưa vào mục lục')


def in_ds(tieu_de, ds, toi_da):
    print(f'\n{tieu_de} ({len(ds)}):')
    for r in ds[:toi_da]:
        print('  ' + r)
    if len(ds) > toi_da:
        print(f'  ... và {len(ds) - toi_da} tệp khác (--toi-da để xem thêm)')


def quet(kho, toi_da, co_san):
    tl = chung.tep_tu_lieu(kho)
    ml = chung.dong_muc_luc(kho)
    co_ml = {p for p, _ in ml}
    chua = [r for r in tl if r not in co_ml]
    mat = [p for p, _ in ml if p not in set(tl)]
    moi = [r for r in tl if r.startswith('0 Moi them/')]
    print(f'Kho: {kho}\n{len(tl)} tư liệu, {len(ml)} dòng mục lục.')
    if not tl:
        print('Kho còn trống: chưa có tư liệu nào. Gợi ý người viết thả vài tư liệu đầu tiên vào (HUONG-DAN-KHO.md).')
        return
    if chua:
        if co_san:
            in_ds('Chưa vào mục lục: kho ghi chép có sẵn, chỉ lập mục lục cho tệp người viết chọn, không lập cho tất cả',
                  chua, toi_da)
        else:
            in_ds('Chưa vào mục lục: đọc từng tệp, đề xuất một dòng mục lục, người viết duyệt rồi mới ghi', chua, toi_da)
    if moi:
        in_ds('Ở ngăn "0 Moi them": đề xuất ngăn phù hợp, người viết đồng ý rồi mới chuyển', moi, toi_da)
    if mat:
        in_ds('Dòng mục lục không còn tệp: hỏi người viết tệp đã đổi tên, chuyển chỗ, hay bỏ', mat, toi_da)
    if not (chua or moi or mat):
        print('Kho gọn: mọi tư liệu đã vào mục lục.')


def tim(kho, tu, toi_da):
    can = [chung.rut_gon(t) for t in tu if t.strip()]
    if not can:
        raise SystemExit('Cho ít nhất một từ để tìm.')
    ml = dict(chung.dong_muc_luc(kho))
    ket_qua = []
    for rel, that in chung.tep_tu_lieu(kho, kem_duong_that=True):
        dong_ml = ml.get(rel, '')
        noi_dung = ''
        if rel.lower().endswith(DUOI_CHU):
            try:
                with open(that, encoding='utf-8', errors='replace') as h:
                    noi_dung = chung.nfc(h.read())
            except OSError:
                pass
        bo = chung.rut_gon(rel + ' ' + dong_ml + ' ' + noi_dung)
        if not all(c in bo for c in can):
            continue
        diem = sum(bo.count(c) for c in can)
        rieng_tu = cot_rieng_tu(dong_ml)
        trich = ''
        if not any(k in chung.rut_gon(rieng_tu) for k in KHONG_TRICH):
            for dong in noi_dung.splitlines():
                if any(c in chung.rut_gon(dong) for c in can):
                    trich = dong.strip()[:160]
                    break
        ket_qua.append((diem, rel, trich, rieng_tu))
    ket_qua.sort(key=lambda x: (-x[0], x[1]))
    print(f'Tìm "{" ".join(tu)}" trong {kho}: {len(ket_qua)} tư liệu khớp.')
    for diem, rel, trich, rieng_tu in ket_qua[:toi_da]:
        print(f'\n  {rel}\n    riêng tư: {rieng_tu}' + (f'\n    "{trich}"' if trich else ''))
    if len(ket_qua) > toi_da:
        print(f'\n  ... còn {len(ket_qua) - toi_da} kết quả; thu hẹp từ khóa hoặc tăng --toi-da.')
    if any(any(k in chung.rut_gon(r[3]) for k in KHONG_TRICH) for r in ket_qua):
        print('\nCó tư liệu ghi "chỉ để mình đọc" hay "cần hỏi đồng ý": không in trích đoạn; hỏi người viết trước khi mở.')


def main():
    ap = argparse.ArgumentParser(description='Rà và tìm trong kho tư liệu nguyên bản.')
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--quet', action='store_true')
    g.add_argument('--tim', nargs='+', metavar='TU')
    ap.add_argument('--kho')
    ap.add_argument('--toi-da', type=int, default=20)
    a = ap.parse_args()
    kho = chung.thu_muc_kho(ep=a.kho)
    if not os.path.isdir(kho):
        raise SystemExit(f'Không thấy kho tư liệu ở {kho}: chạy python3 tools/cai-dat.py, gắn thư mục kho vào phiên, '
                         'hoặc truyền --kho <đường dẫn phiên này thấy>.')
    if a.quet:
        quet(kho, a.toi_da, bool(chung.nap_xuong().get('khoCoSan')) if chung.la_xuong() else False)
    else:
        tim(kho, a.tim, a.toi_da)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Dò từ cấm, từ ngờ và cấu trúc hạn chế trong văn bản tiếng Việt.

Máy chỉ đếm phần đếm được. Kết quả là danh sách chỗ cần người đọc xem lại,
không phải lệnh sửa: với từ ngờ, kiểm điều kiện ngoại lệ ở mục B2 của file
tham chiếu trước khi thay; với cấu trúc, so số lần với trần ở mục D rồi hỏi
từng lần có mang luận điểm hay nhịp không.

Nguồn danh sách:
  - A1, A3 và C đọc thẳng từ bảng trong file tham chiếu (cột thứ hai của A1,
    cột đầu của A3, cột thứ hai của C), nên sửa file ấy là đủ.
  - A2, A4 và D là mẫu cấu trúc, viết sẵn trong script này theo file tham
    chiếu ngày 16/10/2026; khi sửa các mục ấy trong file tham chiếu, sửa
    danh sách MAU_* bên dưới cho khớp.

Dùng:
  python3 tools/ra-tu-va-cau-truc.py bai.md [bai2.md ...]
  python3 scripts/ra-tu-va-cau-truc.py bai.md   (trong gói skill viet-nguyen-ban)
  python3 tools/ra-tu-va-cau-truc.py --ref duong/dan/tu-vung-va-cau-truc.md bai.md
"""
import os
import re
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
REF_MAC_DINH = [
    # Trong repo: tools/ cạnh skills/.
    os.path.join(HERE, '..', 'skills', 'viet-nguyen-ban',
                 'references', 'tu-vung-va-cau-truc.md'),
    # Trong gói skill viet-nguyen-ban: scripts/ cạnh references/.
    os.path.join(HERE, '..', 'references', 'tu-vung-va-cau-truc.md'),
]

W = r'[^\W_]'  # một chữ cái hoặc chữ số

# A2: cụm sáo (đầu câu hoặc giữa câu). Viết thường; so khớp không phân biệt hoa thường.
MAU_A2 = [
    r'trong bối cảnh .{1,60}?(phát triển không ngừng|phát triển mạnh mẽ)',
    r'trong (thời đại số|kỷ nguyên 4\.0|kỷ nguyên ai|xã hội hiện đại|thời đại nhịp sống nhanh)',
    r'hãy (tưởng tượng|hình dung)',
    r'bạn đã bao giờ tự hỏi', r'có khi nào bạn cảm thấy', r'từ xưa đến nay',
    r'như đã đề cập', r'như chúng ta đã thấy', r'trong phần này', r'tiếp theo, chúng ta sẽ',
    r'trước hết, hãy', r'(chúng ta )?hãy cùng', r'(điều )?đáng chú ý là', r'cần lưu ý rằng',
    r'quan trọng hơn cả', r'có thể nói rằng', r'có thể thấy rằng', r'nhìn chung thì', r'về cơ bản,',
    r'tóm lại,', r'kết luận là,', r'trong tương lai, .{1,40}? sẽ tiếp tục phát triển',
    r'hành trình .{0,30}?vẫn còn ở phía trước', r'bắt đầu hành trình của bạn',
    r'hy vọng bài viết (này )?hữu ích', r'cảm ơn bạn đã đọc', r'đừng bỏ lỡ cơ hội',
    r'bước tiến đúng hướng', r'tảng băng chìm', r'bức tranh toàn cảnh',
    r'mở ra một (chương|kỷ nguyên|cánh cửa) mới', r'cánh cửa dẫn đến',
    r'định hình tương lai', r'thay đổi cuộc chơi', r'đi đầu xu hướng',
    r'đóng vai trò (then chốt|cốt lõi|quan trọng|trung tâm)', r'một phần không thể thiếu',
    r'cần thiết hơn bao giờ hết', r'(giá trị|lợi ích) vượt trội', r'trải nghiệm (tuyệt vời|độc đáo)',
    r'người bạn đồng hành đáng tin cậy', r'phát huy tối đa tiềm năng', r'khai phá khả năng tiềm ẩn',
    r'vượt qua chính mình', r'phiên bản tốt nhất của (bạn|mình|chính mình)', r'sống trọn vẹn',
    r'tìm thấy chính mình',
    r'nghiên cứu chỉ ra rằng', r'các chuyên gia cho rằng', r'theo nhiều nguồn tin',
    r'đã được chứng minh là', r'được công nhận rộng rãi', r'trong nhiều nghiên cứu',
    r'câu hỏi của bạn (thật )?tuyệt vời', r'là một mô hình (ai|ngôn ngữ)',
]

# A4: kết hợp từ sai và dịch sát.
MAU_A4 = [
    r'khép lại (chương trình|khóa học|ngày học|buổi học)', r'lời khép', r'đóng (một|lại) ngày học',
    r'gom lại (\S+ )?ngày', r'mọc lên từ', r'chạm nhẹ vào một vùng', r'đánh đổ một giả định',
    r'nới ra một giả định', r'đọc (năng lượng|tình huống|người khác|cơ thể|phản ứng)',
    r'rất người', r'ở lại với cơ thể', r'làm việc cho người nói',
    r'mang một gánh (khá )?nặng', r'một khoảng trống rỗng', r'nhiều chỗ để tinh luyện',
    r'tự thoại nội tâm', r'tái định nghĩa thất bại', r'đồng hồ sinh học được cài đặt lại',
]

# D: cấu trúc hạn chế. (tên, mẫu, trần mô tả)
MAU_D = [
    ('đối ngẫu phủ định', r'không chỉ .{1,80}? mà còn|không phải (là )?.{1,80}? mà là|'
     r'đây không phải là .{1,80}?\. đây là|tưởng chừng .{1,60}? nhưng', '1 bài ngắn, 2 bài dài'),
    ('"không hẳn vì..., mà vì"', r'không hẳn (là )?vì .{1,80}? mà (là )?vì', 'chỉ khi gỡ ngộ nhận phổ biến'),
    ('song đối "chưa đủ để... nhưng đã đủ để"', r'chưa đủ để .{1,80}? (nhưng )?đã đủ để', '0'),
    ('biển chỉ đường', r'đáng lo ngại hơn:|đặc biệt đáng chú ý:|thật đáng sợ:|câu hỏi còn lại là', '0'),
    ('danh ngữ hóa mở câu', r'(^|[.!?]\s+)(sự phát triển của|việc ứng dụng|tầm quan trọng của)', '0 ở đầu câu'),
    ('bị động kiểu Anh', r'được (xem|coi) là|được phản ánh qua', 'chỉ khi tác nhân không quan trọng'),
    ('ràng buộc định lượng giả', r'chọn một từ|(viết|chỉ cần) (đúng )?một câu|đúng một điểm|\(một câu\)', '0'),
]
TU_NOI_DEM = ['hơn nữa', 'thêm vào đó', 'bên cạnh đó', 'ngoài ra', 'đặc biệt là', 'mặt khác']


def nfc(s):
    return unicodedata.normalize('NFC', s)


def tim_ref(argv):
    if '--ref' in argv:
        i = argv.index('--ref')
        ref = argv[i + 1]
        del argv[i:i + 2]
        return ref
    for r in REF_MAC_DINH:
        if os.path.exists(r):
            return r
    sys.exit('Không tìm thấy file tu-vung-va-cau-truc.md; truyền --ref.')


def doc_muc(text, dau):
    """Trả về phần văn bản của mục bắt đầu bằng heading có tiền tố `dau`."""
    m = re.search(r'^#{2,3} ' + re.escape(dau) + r'.*?$(.*?)(?=^#{2,3} |\Z)', text, re.S | re.M)
    return m.group(1) if m else ''


def o_bang(muc, cot):
    ra = []
    for dong in muc.splitlines():
        if not dong.startswith('|') or set(dong) <= set('|- '):
            continue
        cac_o = [c.strip() for c in dong.strip('|').split('|')]
        if len(cac_o) > cot:
            ra.append(cac_o[cot])
    return ra[1:]  # bỏ dòng tiêu đề


def tach_tu(o):
    o = re.sub(r'\[[^\]]*\]', '', o)          # bỏ chú thích [English]
    o = re.sub(r'\([^)]*\)', '', o)           # bỏ chú thích (...)
    o = o.replace('*', '').replace('"', '')
    ra = []
    for t in re.split(r'[,;]', o):
        t = t.strip().rstrip('.').strip()
        t = t.replace('...', '').strip()
        if t and len(t) < 50:
            ra.append(t.lower())
    return ra


def mau_tu(t):
    return re.compile(r'(?<!' + W + ')' + re.escape(t) + r'(?!' + W + ')', re.I)


def dong_cua(text, vi_tri):
    return text.count('\n', 0, vi_tri) + 1


def ra_file(duong, A1, A3, C):
    goc = nfc(open(duong, encoding='utf-8').read())
    # bỏ khối mã và trích dẫn khối (thường là nguyên văn của người khác)
    text = re.sub(r'```.*?```', lambda m: '\n' * m.group(0).count('\n'), goc, flags=re.S)
    text = '\n'.join('' if l.lstrip().startswith('>') else l for l in text.split('\n'))
    so_chu = len(re.findall(W + '+', text))
    print('\n== %s (%d chữ, %s) ==' % (duong, so_chu, 'bài ngắn' if so_chu < 1000 else 'bài dài'))

    def bao(nhan, ket):
        if ket:
            print('  %s' % nhan)
            for k in ket:
                print('    - %s' % k)

    # A5: dấu câu
    a5 = []
    for kys, ten in (('—', 'em dash'), ('“”', 'ngoặc cong'), ('…', 'ba chấm Unicode')):
        dong = sorted({dong_cua(text, m.start()) for m in re.finditer('[' + re.escape(kys) + ']', text)})
        if dong:
            a5.append('%s ở %d dòng (dòng %s)' % (ten, len(dong), ', '.join(map(str, dong[:15]))))
    for m in re.finditer(r'^#{1,6} (.+)$', text, re.M):
        tu = re.findall(W + '+', m.group(1))
        if len(tu) >= 3 and all(t[0].isupper() for t in tu) and not m.group(1).isupper():
            a5.append('dòng %d: heading kiểu Title Case' % dong_cua(text, m.start()))
    bao('A5. Dấu câu và định dạng (phải sửa):', a5)

    for nhan, ds in (('A1. Thuật ngữ đã chốt (phải thay khi đúng nghĩa ở bảng):', A1),
                     ('A3. Từ vựng AI (phải thay):', A3)):
        ket = []
        for t in ds:
            for m in mau_tu(t).finditer(text):
                ket.append('dòng %d: "%s"' % (dong_cua(text, m.start()), m.group(0)))
        bao(nhan, ket)

    for nhan, ds in (('A2. Cụm sáo (xem ngữ cảnh rồi thay):', MAU_A2),
                     ('A4. Kết hợp từ sai, dịch sát (phải thay):', MAU_A4)):
        ket = []
        for p in ds:
            for m in re.finditer(r'(?<!' + W + ')' + p, text, re.I):
                ket.append('dòng %d: "%s"' % (dong_cua(text, m.start()), m.group(0).strip()))
        bao(nhan, ket)

    ket = []
    for t in C:
        dong = [dong_cua(text, m.start()) for m in mau_tu(t).finditer(text)]
        if dong:
            ket.append('"%s" x%d (dòng %s)' % (t, len(dong), ', '.join(map(str, dong[:8]))))
    bao('C. Từ ngờ (kiểm mục B2; không khớp thì thay hoặc ghi vào ghi chú bàn giao):', ket)

    ket = []
    for ten, p, tran in MAU_D:
        dong = [dong_cua(text, m.end() - 1) for m in re.finditer(p, text, re.I | re.M)]
        if dong:
            ket.append('%s x%d, trần %s (dòng %s)' % (ten, len(dong), tran, ', '.join(map(str, dong))))
    for t in TU_NOI_DEM:
        dong = [dong_cua(text, m.start()) for m in mau_tu(t).finditer(text)]
        if len(dong) > 1:
            ket.append('từ nối "%s" x%d, trần 1 (dòng %s)' % (t, len(dong), ', '.join(map(str, dong))))
    cau_chot = 0
    for doan in re.split(r'\n\s*\n', text):
        d = doan.strip()
        if d and not d.startswith(('#', '|', '-', '*')) and len(re.findall(r'[.!?]', d)) <= 1 \
                and len(re.findall(W + '+', d)) < 12:
            cau_chot += 1
    if cau_chot > (1 if so_chu < 1000 else 2):
        ket.append('đoạn một câu dưới 12 chữ x%d (câu chốt cô độc hoặc nhãn; trần 1 bài ngắn)' % cau_chot)
    for i, phan in enumerate(re.split(r'^#{1,6} .*$', text, flags=re.M)):
        hoi = phan.count('?')
        if hoi > 1:
            ket.append('section thứ %d có %d câu hỏi: trần 1 cho câu hỏi tu từ; câu hỏi phản tư trao người đọc (F4) không tính, kiểm từng câu' % (i, hoi))
    bao('D. Cấu trúc hạn chế (so trần, rồi hỏi từng lần):', ket)

    viet_hoa = [dong_cua(text, m.start()) for m in re.finditer(r':\s+[A-ZÀ-Ỹ]', text)]
    if viet_hoa:
        print('  Viết hoa sau hai chấm: kiểm luật ở dòng %s' % ', '.join(map(str, viet_hoa[:15])))


def main():
    argv = sys.argv[1:]
    ref = tim_ref(argv)
    if not argv:
        sys.exit(__doc__)
    t = nfc(open(ref, encoding='utf-8').read())
    A1 = [x for o in o_bang(doc_muc(t, 'A1.'), 1) for x in tach_tu(o)]
    A3 = [x for o in o_bang(doc_muc(t, 'A3.'), 0) for x in tach_tu(o)]
    C = [x for o in o_bang(doc_muc(t, 'C.'), 1) for x in tach_tu(o)]
    C = [x for x in C if x not in ('rất',)]  # quá phổ biến để dò máy
    print('Danh sách từ %s: A1 %d mục, A3 %d mục, C %d mục' % (os.path.relpath(ref), len(A1), len(A3), len(C)))
    for f in argv:
        ra_file(f, A1, A3, C)


if __name__ == '__main__':
    main()

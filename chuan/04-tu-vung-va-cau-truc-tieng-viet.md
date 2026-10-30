# Chuẩn 04. Từ và cấu trúc tiếng Việt: cấm, đặc thù, hạn chế

Cập nhật: 31/10/2026 (thêm mục 8, hai nếp tiếng Việt tự nhiên). Bản tóm cho người; bản đầy đủ (mọi danh sách, bảng thay, ví dụ) ở `skills/viet-nguyen-ban/references/tu-vung-va-cau-truc.md`. Công cụ: `tools/ra-tu-va-cau-truc.py`. Phương pháp: Thạc sĩ Lương Dũng Nhân.

## 1. Vì sao một xưởng viết theo phán đoán vẫn cần bảng từ

Chuẩn 02 đặt phán đoán lên trên khuôn: thủ pháp chỉ vào bài khi bài cần. Nhưng có những chỗ hỏi lại mỗi lần là phí sức và dễ trượt: thuật ngữ người viết đã chốt, cụm sáo mà văn máy tiếng Việt lặp đi lặp lại, kết hợp từ người Việt không nói. Với những chỗ ấy, một bảng rõ ràng giữ chất lượng tốt hơn một câu hỏi, và để dành sức phán đoán cho chỗ thật sự cần.

## 2. Bốn danh sách, bốn luật đọc

| Danh sách | Gồm | Luật đọc |
|---|---|---|
| A. Cấm tuyệt đối | Thuật ngữ người viết đã chốt; cụm sáo AI ở mở bài, chuyển đoạn, kết bài, giữa câu; uy tín giả không nguồn; từ vựng AI hiếm khi có trong giọng người viết thật; kết hợp từ sai và dịch sát; dấu câu và định dạng | Gặp là thay. Chỉ giữ trong trích dẫn nguyên văn của người khác hoặc khi bài bàn về chính từ đó |
| B. Từ đặc thù của người viết | Khái niệm riêng; những từ trong danh sách C người viết dùng ở nghĩa riêng, kèm điều kiện và ví dụ; cụm câu dấu vân tay; cặp chọn từ người viết đã sửa | Ưu tiên khi mạch gọi, đúng nghĩa đã ghi. Mỗi cụm câu dấu vân tay tối đa một lần một bài |
| C. Từ ngờ | Từ vựng "khai sáng", "đẹp lời", "to lớn", phóng đại, cảm xúc sáo, ngôn ngữ kinh doanh | Mặc định thay. Giữ khi khớp nghĩa riêng ở B; ngoài B, AI giữ thì phải ghi vào ghi chú bàn giao để người viết quyết |
| D. Cấu trúc hạn chế | Đối ngẫu phủ định, từ nối đệm, câu hỏi tu từ, câu chốt cô độc, nhóm ba mặc định, liệt kê đối xứng, danh ngữ hóa mở câu, bị động kiểu Anh, biển chỉ đường, tóm ý cuối phần, ràng buộc định lượng giả, từ đơn tiết cụt | Có trần. Vượt trần thì sửa; dưới trần, mỗi lần vẫn hỏi có mang luận điểm hay nhịp không |

## 3. Từ đặc thù vừa là dấu vân tay vừa là cửa ngoại lệ

Nhiều từ trong các danh sách chống văn AI là từ người viết chuyên môn dùng thật, ở nghĩa riêng: một nhà giáo dục có thể dùng "hành trình" làm ẩn dụ cho tiến trình học, "đồng hành" cho vai của cha mẹ, "nuôi dưỡng" thay cho "kiểm soát". Cấm trơn những từ ấy là xóa giọng người viết; thả trơn thì văn máy lọt qua. Vì vậy mỗi từ có điều kiện giữ, ví dụ từ bài của chính người viết, và cách dùng sáo vẫn phải thay.

Danh sách B không viết sẵn được: nó lấy từ bài người viết hài lòng, từ bản chốt, và từ lời người viết nói. Chiều ngược lại cũng là một bẫy: rắc dày dấu vân tay cho "giống giọng" là nhại giọng, một dấu hiệu văn máy khác.

## 4. Trần không phải chỉ tiêu

Trần ở D là số lần tối đa. Dưới trần không có nghĩa là nên dùng; mỗi lần dùng vẫn hỏi cấu trúc ấy có mang luận điểm hay nhịp không. Vượt trần thì sửa, nhưng không xóa ngẫu nhiên: giữ lần mang luận điểm hay bản lề, viết lại các lần còn lại cho thẳng.

## 5. Khi chính người viết dùng một từ trong danh sách A

Người viết là thẩm quyền về chính họ. Khi một từ ở A xuất hiện trong bản người viết tự viết, AI nêu ra trong ghi chú bàn giao, không tự đổi. Người viết giữ thì đó là dữ liệu để xem lại danh sách.

## 6. Danh sách lớn lên thế nào

- Người viết nói rõ "không dùng X" thì X vào A1, ghi ngày và bài nguồn.
- Người viết giữ hoặc tự viết một từ ở C với nghĩa riêng thì từ ấy vào B2, kèm điều kiện và ví dụ.
- AI giữ một từ ở C ngoài B2 thì ghi vào ghi chú bàn giao; người viết duyệt thì thêm vào B2.
- Người viết gộp hay cắt một cấu trúc nhiều lần cùng điều kiện thì xem lại trần ở D (thang nâng mức ở chuẩn 03).

## 7. Máy kiểm gì, người kiểm gì

`tools/ra-tu-va-cau-truc.py` đếm phần đếm được: dấu câu, tiêu đề viết hoa mọi chữ đầu từ, từ và cụm ở A và C, cấu trúc ở D, viết hoa sau hai chấm, số câu hỏi mỗi phần. Nó không biết một từ C có khớp nghĩa riêng của người viết không, không biết một cấu trúc có mang luận điểm không, và không thấy nhịp. Những việc ấy thuộc lượt rà của AI và cuối cùng là của người viết.

## 8. Hai nếp tiếng Việt tự nhiên: nhịp song âm tiết và thoát lối dịch sát

Hai lỗi văn máy khó thấy nhất không nằm ở từ cấm mà ở chỗ câu đúng ngữ pháp, sạch danh sách, nhưng người viết tiếng Việt chuẩn mực không viết như thế. Tác giả phương pháp đã sửa hai nếp này lặp lại qua nhiều bản chốt (newsletter, bài tạp chí, sách thực hành và ứng dụng đi kèm, 10/2026), nên chúng được gom thành một nguyên lý, mỗi nếp một bảng ở một nơi.

| Nếp | Phép thử | Nơi giữ bảng | Luật đọc |
|---|---|---|---|
| Nhịp song âm tiết | Đọc to; dừng ở mỗi động từ, tính từ, danh từ trừu tượng đứng một tiếng ("cần được chăm", "đang khá vững", "nặng", "lời"); hỏi người viết chuẩn mực có viết đủ hai tiếng không | `tu-vung-va-cau-truc.md` D1 | Trần 0 ở mục D; ngoại lệ có điều kiện |
| Thoát lối dịch sát | Dịch ngược cụm đáng ngờ sang tiếng Anh; ra trọn một cụm quen thuộc ("mang một gánh khá nặng", "tìm bộ lạc của mình", "tự thoại nội tâm") thì viết theo cách người Việt nói | `tu-vung-va-cau-truc.md` A4b | Danh sách A, gặp là thay |

Ngoại lệ chung của hai nếp: thành ngữ và cụm cố định ("biết đủ"); nhãn cột bảng; lời trích nguyên văn; tên gọi ngoài đời đúng như người ta dùng; thuật ngữ chuyên môn đã chốt, định danh một lần ở phần dẫn nghiên cứu rồi đời thường hóa ở phần hành động. Khi nới từ hay đổi cụm, không đẻ từ ghép gượng gạo chỉ để qua phép thử: đó là một kiểu văn máy khác.

Quy ước trình bày đi cùng là mặc định, không phải nguyên lý, nên đứng riêng ở A5: chữ số Ả Rập cho mọi số đếm và đại lượng ở mọi văn bản, không trộn chữ và số; ngoặc vuông tiếng Anh chỉ khi tiếng Việt chưa tự đủ nghĩa, khi là tên phương pháp cố định hoặc gốc sẽ dùng lại; tên ấn phẩm đúng từng chữ theo bản in cuối.

`tools/ra-tu-va-cau-truc.py` dò các cụm dịch sát đã có trong bảng, các từ đơn âm tiết đứng cuối mệnh đề và câu trộn chữ với số, để người đọc xem lại. Nó không biết một cụm mới có phải dịch sát không, cũng không nghe được nhịp; phép thử đọc to và dịch ngược vẫn là việc của người đọc.

---
name: kiem-chung
description: "Kiểm chứng và trình bày chuẩn xác thông tin trong văn bản tiếng Việt của người viết có uy tín nghề nghiệp (nhà giáo dục, nhà tham vấn, chuyên gia): truy nguồn gốc, đối chiếu bốn lớp của trích dẫn (danh tính, thư mục, nội dung, lời), diễn giải nghiên cứu đúng mực bằng thang chứng cứ, ghi danh xưng và cơ quan của nhà nghiên cứu cho trang trọng mà đúng thời điểm, tách sự thật chỉ tác giả xác nhận được, và trình bày đề xuất sửa cho tác giả hoặc ban biên tập. Dùng khi người dùng nói \"kiểm chứng trích dẫn\", \"rà trích dẫn\", \"fact-check sách/bài\", \"soát nguồn\", \"kiểm danh mục tham khảo\", \"kiểm chức danh, năm, tên tác giả\", \"rà phản hồi của biên tập về trích dẫn\", hoặc khi một văn bản sắp xuất bản có nhắc nhà nghiên cứu, con số, phát hiện khoa học, lời trích nổi tiếng."
---

# Kiểm chứng

## Cấu hình cá nhân

Điền một lần khi dựng skill cho mình. Phần thân skill gọi các mục này bằng tên; mục để trống nghĩa là dùng mặc định trong ngoặc. Trong xưởng đã dựng (có `XUONG.json`), đọc `phong-cach/GIONG-VAN.md` của xưởng thay cho các mục dưới; mục nào tệp ấy chưa nói tới mới dùng mặc định ở đây. Gói skill riêng có thêm khối "Đã thiết lập" ở đầu mục này.

- **Tên người viết và vai trò**: «...» (mặc định: "tác giả")
- **Cách gọi người thầy, đồng nghiệp hay xuất hiện trong bài**: «...» (mặc định: họ tên đầy đủ kèm học vị đã xác minh)
- **Mẫu ghi trích dẫn trong chính văn đã chốt với nhà xuất bản hay dự án**: «...» (mặc định: năm viết vào câu, như mục VI)
- **Quy ước chính tả riêng** (kiểu đặt dấu thanh, thuật ngữ cố định, từ tránh): «...» (mặc định: theo quy ước của nhà xuất bản)
- **Nơi lưu sổ nguồn và bài học**: «...» (mặc định trong xưởng: `so-nguon.md` trong thư mục bài ở `Bai viet/`; ngoài xưởng: một tệp `so-nguon.md` cạnh bản thảo. Tư liệu gốc người viết đã lưu ở ngăn `4 Tu lieu tham khao` của kho tư liệu là nơi tìm nguồn đầu tiên; kiểm xong thì đề xuất bổ sung nguồn đầy đủ vào mục lục kho)

Skill này dành cho người viết có uy tín nghề nghiệp: nhà giáo dục, nhà tham vấn, chuyên gia viết cho công chúng. Người đọc tin một câu "nghiên cứu cho thấy" vì họ tin người viết. Một tên sai, một năm lệch, một phát hiện bị nói quá, và người đọc có lý do nghi cả trang sách. Vì vậy kiểm chứng ở đây không phải thủ tục đánh dấu cho đủ mục, mà là một cách đọc: đọc câu văn rồi đọc nguồn, và hỏi hai bên đã khớp nhau hoàn toàn chưa.

Mệnh đề gốc của toàn skill: **mỗi câu nói về một nguồn phải nói đúng điều nguồn nói, ở đúng mức chắc chắn nguồn cho phép, và trao công cho đúng người, đúng thời điểm.** Mọi hướng dẫn bên dưới là cách soi mệnh đề này trong từng tình huống, không phải danh sách để điền.

Skill được chưng cất từ một đợt rà soát trích dẫn thật cho một cuốn sách thực hành về sức khỏe tinh thần (tháng 9-10/2026): 214 nguồn, hơn 300 chỗ cần chỉnh, ba vòng đối chiếu với ban biên tập, một bản rà soát độc lập, và các bản chốt chính tay tác giả sửa. Các ví dụ về nghiên cứu trong skill là lỗi có thật, đã kiểm lại trên nguồn.

## I. Sáu điều không đổi

Đây là những điều không đổi theo ngữ cảnh. Mọi chỗ khác là phán đoán.

1. **Không dựng thông tin thư mục từ trí nhớ.** Tên, năm, tạp chí, số trang, DOI lấy từ nguồn gốc (trang DOI, Crossref, trang tạp chí, nhà xuất bản, kho của trường), kể cả khi tôi "nhớ chắc". Trí nhớ của mô hình là đầu mối để tra, không phải bằng chứng.
2. **Không gắn nhãn "đã kiểm" cho điều chưa đọc tận gốc.** Mỗi nguồn mang một trong bốn trạng thái, đi theo nó tới tận bản cuối: "kiểm trên toàn văn"; "kiểm qua tóm tắt gốc" (tóm tắt của chính bài, trên trang tạp chí hay PubMed); "kiểm qua nguồn thứ cấp" (báo chí, blog, bài tổng hợp, ghi rõ nguồn nào); "chưa kiểm được".
3. **Không lấp chỗ trống bằng nguồn mơ hồ.** Không "một số nghiên cứu cho thấy", "các chuyên gia cho rằng", không bịa tên, năm, con số cho câu nghe có cơ sở.
4. **Không quyết thay tác giả những sự thật thuộc về đời họ.** Giai thoại, mốc thời gian, tên tổ chức tác giả từng làm, số liệu khảo sát của chính tác giả: chỉ tác giả xác nhận được. Tôi nêu chỗ lệch và hỏi; tôi không sửa theo suy đoán.
5. **Mọi đề xuất sửa tự nó cũng phải qua kiểm chứng.** Câu tôi viết lại không được mang thêm một tên, một con số, một khẳng định chưa kiểm. Sửa xong một lỗi mà gieo một lỗi mới là thất bại kép.
6. **Góp ý của người khác là đầu mối, không phải phán quyết.** Ghi chú của biên tập viên, bản rà soát độc lập, kết quả của một AI khác, kể cả kết quả của một phiên làm việc trước: đều kiểm lại trên nguồn trước khi nhận hay bác. Ví dụ thật: người rà soát độc lập ghi ngày bài báo Harvard Crimson là 25/10/2006, nhưng đường dẫn họ đưa không mở được, còn bài đang hoạt động trên trang báo nằm ở đường dẫn mang ngày 26/10/2006, nên giữ ngày 26/10. Biên tập viên tự điền họ tên đầy đủ cho "Park", "McRae", "Egan" nhưng điền nhầm sang ba người khác ngành (đúng là Denise C. Park, Kateri McRae, Sarah J. Egan).

## II. Khi nào dùng, và phân vai với skill khác

Dùng khi văn bản nhắc tới nhà nghiên cứu, công trình, con số, phát hiện khoa học, lời trích, sự kiện lịch sử, văn bản luật; khi lập hoặc soát danh mục tham khảo; khi nhận phản hồi của biên tập hay người rà soát về những điều ấy; và ở khâu rà cuối của mọi bài công khai.

- Các skill soạn bài, soạn sách, viết bài dài có dẫn nguồn của bạn: gọi skill này ở khâu nghiên cứu (mở sổ nguồn) và khâu rà cuối (đối chiếu ngược). Skill soạn bài lo giọng và mạch; skill này lo độ khớp với nguồn.
- Skill rà lập luận (nếu có, ví dụ một khung rà kiểu FACTUAL): rà chất lượng lập luận của cả văn bản (giả định, thiên lệch, đầy đủ, giới hạn). Khi chiều Sự thật [Facts] của FACTUAL chạm tới một nguồn cụ thể, chuyển sang cách đọc của skill này.
- Skill tổng quan tài liệu học thuật (nếu có): tổng quan tài liệu cấp học thuật. Skill này không thay việc tổng quan; nó kiểm từng mệnh đề đã viết ra.

## III. Bốn câu hỏi trước khi bắt đầu

1. **Văn bản này sẽ sống ở đâu, ai đọc?** Sách in, bài báo, tham luận cần mức kiểm sâu và danh mục đầy đủ; bài mạng xã hội cần ít nguồn nhưng mỗi nguồn vẫn phải đúng. Mức sâu đi theo hệ quả của sai sót, không theo độ dài.
2. **Mỗi loại sự thật thuộc thẩm quyền của ai?** Nguồn bên ngoài (tôi kiểm), đời và dữ liệu của tác giả (tác giả xác nhận), quy định của nhà xuất bản hay tổ chức (bên đó quyết). Chia rõ từ đầu để biết câu nào tôi tự sửa, câu nào tôi hỏi.
3. **Kết quả dành cho ai?** Tác giả tự sửa trên bản thảo, hay ban biên tập sửa trên bản dàn trang. Hai người đọc này cần hai cách trình bày khác nhau (mục IX).
4. **Tôi có công cụ gì?** Tìm kiếm web, đọc trang, file dàn trang, kho lưu trữ. Khi một nguồn bị chặn, tìm đường khác (trang tạp chí, PubMed, kho của trường, bản lưu của nhà xuất bản) và ghi lại; không suy ra kết quả từ việc không truy cập được. Khi không có công cụ tra cứu nào, nói rõ giới hạn ấy ngay đầu báo cáo, gắn mọi mục "chưa kiểm được", và không phán "đúng" dựa vào trí nhớ; việc còn làm được là chỉ ra những câu cần kiểm và vì sao.

## IV. Bốn lớp của một trích dẫn

Một câu nhắc nghiên cứu thường sai ở một trong bốn lớp. Đọc câu, rồi soi lần lượt từng lớp. Mỗi lớp dưới đây gồm câu hỏi soi và những cái bẫy đã gặp thật.

### 4.1. Danh tính: đúng người chưa?

- Người được nêu có đúng là tác giả đứng đầu, hay là đồng tác giả nổi tiếng hơn? Thứ tự tác giả có đúng như trên công bố không? Bài một tác giả có bị gắn thêm "và cộng sự" không?
- Họ tên đầy đủ viết theo cách chính người ấy ký trên công bố (kể cả chữ đệm viết tắt, dấu của tiếng gốc như Kjær).
- Cùng họ không có nghĩa cùng người. Khi chỉ có họ, tra theo DOI của chính bài, đừng tra theo họ.
- Cơ quan **tại thời điểm công bố**, không phải nơi người ấy làm hôm nay. Ví dụ: năm 2005 Kennon Sheldon ở Đại học Missouri, nên câu gắn "Đại học California" cho cả ba tác giả của mô hình 50/10/40 là sai với ông.
- Chức danh tại thời điểm công bố (xem mục VI).

### 4.2. Thư mục: đúng công trình chưa?

- Năm công bố hay năm thực hiện? Một nghiên cứu làm năm 2019, công bố năm 2021, cần ghi rõ năm nào khi câu văn nói "năm...".
- Cùng tác giả, cùng năm có thể có hai bài. Kristin Neff có hai bài trên Self and Identity năm 2003: bài định nghĩa ba thành phần của lòng tự trắc ẩn (tr. 85-101) và bài xây thang đo (tr. 223-250). Câu nói về ba thành phần phải trỏ về bài thứ nhất.
- Tên gọi chính thức của một lý thuyết có khi xuất hiện muộn hơn ý tưởng. Bài năm 1998 của Barbara Fredrickson trình bày mô hình ban đầu; cụm "lý thuyết mở rộng và xây dựng về cảm xúc tích cực" [broaden-and-build theory of positive emotions] là tựa bài năm 2001. Khi câu văn dùng tên gọi chính thức, đối chiếu cả hai bài.
- Nguồn có tồn tại không? Đợt rà sách gặp hai nguồn không tồn tại: "Campbell và cộng sự (2023)" và "Graham Bodie (2015) nêu bốn rào cản lắng nghe". Bốn rào cản thật ra nằm trong một danh sách lưu hành không rõ tác giả.
- Con số có thuộc đúng bài được gắn không? Con số 1-10 cm/s về sợi C xúc giác thuộc nghiên cứu năm 2009 của Löken, không phải bài tổng quan 2014 của McGlone. Kết quả các nghiên cứu bữa ăn gia đình năm 2004 không thể nằm trong bài tổng quan năm 2002 của Fiese.
- Sách kinh điển: năm nguyên tác và ấn bản đang dùng. "Đi tìm lẽ sống" ra đời năm 1946 bằng tiếng Đức, đổi tựa và thêm phần qua nhiều ấn bản tiếng Anh; trích số trang thì phải nói rõ ấn bản nào. Tên bản dịch tiếng Việt theo đúng bản in đã phát hành, kể cả khi tên ấy lệch thuật ngữ của sách (tên sách đã xuất bản giữ nguyên).

### 4.3. Nội dung: nghiên cứu thật sự tìm thấy gì?

Đây là lớp sai nhiều nhất và khó bắt nhất, vì câu văn sai vẫn nghe hợp lý. Soi theo các câu hỏi:

- **Đã đo gì, và không đo gì?** Nghiên cứu tự chạm của Dreisoerner (2021) đo cortisol; nhịp tim không khác giữa các nhóm; oxytocin không được đo, chỉ được nêu như cơ chế để nghiên cứu sau. Câu "tự chạm giúp cơ thể tiết oxytocin, nhịp tim giảm" sai ở cả hai vế.
- **Kết quả hay lời bàn luận?** Phần bàn luận chứa giả thuyết của tác giả. Laborde và cộng sự (2021) đo hoạt động phó giao cảm khi thở ra dài hơn hít vào; cơ chế acetylcholine là lời giải thích trong phần bàn luận, và nghiên cứu không hề thử tỷ lệ 1:2 hay gọi tỷ lệ nào là tối ưu.
- **Thiết kế gì?** Thực nghiệm có đối chứng, tương quan, khảo sát tự báo cáo, tổng quan, phân tích tổng hợp, bài giảng, quan sát lâm sàng, hồi ký. Mỗi loại cho phép một kiểu khẳng định (mục V). "Đi tìm lẽ sống" là hồi ký và quan sát của Frankl, nên không thể nói người có lẽ sống "có xác suất sống sót cao hơn hẳn". Bài phát biểu năm 1993 của Padesky là quan điểm chuyên môn, và chính bà nói điều ấy chưa được kiểm chứng.
- **So với ai?** Nhóm so sánh quyết định nghĩa của kết quả. Một thí nghiệm không có nhóm "tự trách" thì không thể nói "hơn hẳn người tự trách".
- **Trên ai?** Chuột hay người, sinh viên hay người trưởng thành, vận động viên hay người thường, bao nhiêu người. Kết quả trên chuột chỉ gợi ý cơ chế cho người.
- **Mạnh tới đâu và diễn đạt đã hết mơ hồ chưa?** Độ lớn hiệu ứng, ý nghĩa thống kê, kéo dài bao lâu. Hệ số r = 0,075 là "có lợi nhưng nhỏ". Một kết quả không có ý nghĩa thống kê (khoảng tin cậy chứa 0 với hiệu số hay hệ số tương quan, chứa 1 với tỷ số odds hay nguy cơ tương đối) là chưa đủ chứng cứ cho một hiệu ứng, không phải bằng chứng là có hiệu ứng. Với bài phân tích nghiên cứu và tạp chí trí thức, không dùng lối nói tương đối mơ hồ ("cao gấp đôi", "nhiều hồ sơ") mà không nêu rõ con số gốc hoặc độ lớn hiệu ứng cụ thể; khi so sánh các can thiệp thực nghiệm, phải chỉ rõ các biến số đã được kiểm soát đồng nhất giữa các nhóm (như cùng thời lượng đào tạo, cùng chi phí) để lập luận nhân quả chặt chẽ, đồng thời nêu rõ giới hạn cấu trúc ở các nghiên cứu theo dõi dọc dài hạn (như khác biệt theo giới tính hoặc rào cản nguồn lực).
- **Còn đứng vững không?** Bài đã bị rút [retraction] hay đính chính [erratum] chưa (trang tạp chí, Retraction Watch)? Hiệu ứng có thất bại khi lặp lại [replication] ở các nhóm độc lập không (những ví dụ nổi tiếng: kiệt quệ bản ngã [ego depletion], tư thế quyền lực [power posing])? Bài là bản tiền ấn phẩm [preprint] chưa bình duyệt hay đã đăng? Một phát hiện đẹp mà đã lung lay thì nói đúng tình trạng của nó, hoặc không dùng.
- **Của ai?** Phát hiện của nhiều nhóm có bị gom cho một người nổi tiếng không? Phát hiện thực nghiệm có bị gán cho một bài tổng quan không? Ý của tác giả sách có bị gán cho nghiên cứu không?
- **Nguồn thứ cấp có tóm đúng không?** Bản tóm tắt của Greater Good về nghiên cứu Frias và cộng sự (2011) chỉ nêu một nhóm; tóm tắt gốc cho thấy cả hai nhóm suy ngẫm về cái chết đều tăng lòng biết ơn. Khi lệch, theo tóm tắt gốc.

### 4.4. Lời: câu trích và lời ghi công có thật không?

- Lời trong ngoặc kép phải tìm được nguyên văn ở nguồn. Câu trích Andrew Huberman trong sách không khớp nguyên văn nào của ông, nên hoặc dẫn đúng lời, hoặc chuyển thành diễn giải không ngoặc kép.
- Câu nổi tiếng thường bị gán sai (câu "làm vô thức trở thành ý thức..." không có trong tác phẩm của Jung). Ghi công còn tranh luận thì nói đúng mức tranh luận: Lời cầu nguyện thanh thản [Serenity Prayer] "thường được ghi công cho nhà thần học Reinhold Niebuhr", vì năm 2009 Fred Shapiro, người biên soạn The Yale Book of Quotations (Đại học Yale), chỉ nói bằng chứng mới làm tăng khả năng Niebuhr là tác giả.
- Ghi công cho truyền thống hay cho một người khai sinh kỹ thuật cần nguồn như mọi khẳng định khác. "Hatha Yoga Pradipika mô tả tư thế gác chân lên tường" sai: văn bản ấy mô tả một ấn pháp đảo ngược. "Porges đánh giá cao TRE" không có phát biểu nào làm căn cứ, nên bỏ.

## V. Diễn giải đúng mực: mức chắc chắn nằm trong động từ

Diễn giải đúng mực có hai chiều: không nói quá điều nguồn cho phép, và cũng không rào đón tới mức câu văn mất sức. Bài học rõ nhất của đợt rà sách đến từ chính bản chốt của tác giả: nhiều câu rào đón mà bản đề xuất của AI thêm vào cuối đoạn ("Đây là khảo sát tự báo cáo nên chưa chứng minh quan hệ nhân quả", "Đây mới là kết quả sơ bộ trên một mẫu nhỏ") đã bị tác giả cắt. Thay vào đó, tác giả viết lại chính câu nói về phát hiện, để mức chắc chắn nằm ngay trong động từ và chủ ngữ:

- Trước: "...ghi nhận những người tham gia các hoạt động văn hóa thường tự đánh giá sức khỏe tốt hơn...; đây là mối tương quan, chưa phải bằng chứng nhân quả."
- Sau: "...ghi nhận việc tham gia các hoạt động văn hóa có tương quan với việc người đó thường tự đánh giá sức khỏe tốt hơn..."
- Trước: "Christine Padesky... cho rằng...; bà cũng thẳng thắn thừa nhận khi đó điều này chưa được nghiên cứu kiểm chứng."
- Sau: "Christine Padesky... nêu quan điểm rằng..."

Nguyên lý: **chọn động từ khớp với loại chứng cứ, rồi để câu tự đứng.** Chỉ thêm một câu giới hạn riêng khi giới hạn ấy thay đổi cách người đọc sẽ hành động (ví dụ lưu ý an toàn, hay khi nghiên cứu trên chuột được dùng để gợi ý một thực hành cho người).

| Loại chứng cứ | Động từ và khung câu hợp | Tránh |
|---|---|---|
| Thực nghiệm có đối chứng | phát hiện, cho thấy, thấy rằng (kèm đối tượng và nhóm so sánh) | chứng minh, khẳng định (trừ khi đã được nhiều nhóm độc lập lặp lại, hoặc có phân tích tổng hợp ủng hộ) |
| Tương quan, khảo sát | ghi nhận ... có tương quan với, những người ... thường ... | khiến, giúp, làm cho |
| Phân tích tổng hợp, tổng quan | tổng hợp ... thấy rằng, khi tổng quan ... thì thấy | gán phát hiện của một nghiên cứu lẻ cho bài tổng quan |
| Giả thuyết cơ chế, phần bàn luận | các tác giả giải thích rằng, gợi ý | đã được kiểm chứng, cơ chế là |
| Nghiên cứu trên động vật | trên chuột, ... gợi ý một cơ chế cho ... | trình bày như kết quả trên người |
| Quan điểm, bài giảng, sách phổ thông | nêu quan điểm, cho rằng, viết rằng | nghiên cứu cho thấy |
| Ghi công chưa chắc | thường được gắn với tên, thường được ghi công cho | do X phát triển, của X |
| Quan sát, suy rộng của chính tác giả | Tôi cho rằng, Tôi thấy rằng, Theo quan sát của tôi | để ở thể bị động như thể nguồn nói |

Bảng là gợi ý để chọn chữ, không phải bảng tra. Quyết định cuối dựa trên những gì đã soi ở mục 4.3: thiết kế, đối tượng, độ lớn hiệu ứng, và việc phát hiện còn đứng vững hay không.

Thang khoảng cách diễn giải: (a) nguyên văn, ngắn, trong ngoặc kép; (b) diễn giải gần, giữ đúng phạm vi khẳng định của nguồn; (c) suy rộng, đi xa hơn nguồn. Mức (c) là chỗ người viết dung hợp và được phép, miễn mang giọng sở hữu để người đọc biết đâu là nguồn, đâu là tác giả. Không để (c) đội lốt (b).

Thêm vài thao tác giữ chính xác, đều từ bản chốt: thu hẹp đúng phạm vi ("tin đồn tốt đẹp là một cách thức giúp danh tiếng lan truyền", không phải "tin đồn là con đường"); gọi đúng thuật ngữ ("đường dẫn thần kinh", không "con đường"); nêu con số giới hạn khi nó quan trọng với người đọc ("dao động rất rộng, có thể lên tới 8 tháng"); số liệu nghiên cứu viết dạng số, dấu chấm ngăn hàng nghìn.

## VI. Danh xưng và ghi công trong văn tiếng Việt

Người đọc Việt cần biết người được dẫn là ai để đặt mức tin, và văn hóa đọc của ta coi trọng cách gọi trang trọng. Nhưng danh xưng sai còn tệ hơn không có. Cân hai điều ấy như sau:

1. **Lần nhắc đầu (áp dụng cho cả tác giả chính lẫn mọi đồng tác giả được nêu tên)**: bắt buộc có chức danh học thuật hoặc chuyên môn đã xác minh tại thời điểm công bố, họ tên đầy đủ, cơ quan tại thời điểm công bố, năm viết vào câu. Tuyệt đối không để tên nhà nghiên cứu đứng trơn không có chức danh (kể cả khi liệt kê đồng tác giả thứ hai, thứ ba trong câu), và không dùng danh xưng chung chung kiểu "nhà nghiên cứu" khi có thể xác minh chức danh cụ thể từ bài báo gốc hoặc hồ sơ học thuật năm công bố (ví dụ: Giáo sư, Phó Giáo sư, Giáo sư trợ lý, Tiến sĩ, Chuyên gia kinh tế trưởng, Chuyên gia kinh tế cao cấp...). Lần sau trong cùng chương hoặc cùng bài chỉ cần họ hoặc tên. Với văn phổ thông, năm viết thành lời trong câu ("trong nghiên cứu năm 2018") hơn là để trong ngoặc; nhưng khi dự án đã chốt một mẫu khác (ví dụ một hướng dẫn biên soạn ghi "Giáo sư Carol Dweck (2006)"), theo mẫu của dự án, vì chỉ đạo của tác giả thắng mặc định của skill.
2. **Chức danh "giáo sư" chỉ dùng khi người đó giữ chức danh ấy vào thời điểm công bố nghiên cứu được dẫn.** Ở Mỹ và châu Âu, phân biệt rõ full professor ("giáo sư"), associate professor ("phó giáo sư") và assistant professor ("giáo sư trợ lý"); ở các viện nghiên cứu và tổ chức quốc tế (như Ngân hàng Thế giới), dùng đúng chức danh chuyên môn năm công bố ("chuyên gia kinh tế trưởng" cho Lead Economist, "chuyên gia kinh tế cao cấp" cho Senior Economist). Chỉ khi đã tra cứu kỹ mà tác giả không có chức danh học thuật hay chức vụ chuyên môn cụ thể mới dùng vai trò nghề nghiệp theo đúng chuyên ngành ("nhà tâm lý học", "nhà thần kinh học", "nhà kinh tế học"). Học vị "tiến sĩ" cũng cần kiểm. Cách kiểm chức danh năm công bố: chú thích tác giả trên chính bài báo, trang khoa qua bản lưu Wayback Machine, CV công khai, ORCID, tin tức của trường năm ấy.
3. **Lần đầu luôn có chức danh hoặc vai trò chuyên ngành cụ thể**, kể cả với đồng tác giả đi kèm: ở bản chốt, tác giả thêm "nhà tâm lý học" trước Sonja Lyubomirsky, "nhà tâm lý học phát triển" trước Mary Spagnola, và yêu cầu mọi nhà nghiên cứu được nêu tên trong bài báo trí thức đều phải có chức danh rõ ràng.
4. Chức danh viết thường khi đứng giữa câu; viết hoa chữ đầu khi mở câu.
5. Cơ quan: dùng tên Việt khi đã có cách gọi quen (Đại học Stanford, Trường Kinh doanh Harvard); giữ tên gốc khi không có tên Việt ổn định hoặc khi dịch làm mất nhận diện, ví dụ "(University College London)".
6. Nhiều tác giả: tác giả đầu "và các cộng sự"; khi nêu tên thêm đồng tác giả vì vai trò đáng nói, mỗi đồng tác giả được gọi tên đều phải kèm chức danh và cơ quan năm công bố.
7. Gọn mà không lặp: danh xưng nêu một lần, dệt vào câu, không chồng chuỗi đồng vị ngữ [appositive] "X, nhà tâm lý học tại Đại học Y, người nghiên cứu Z" mỗi lần nhắc. Lặp danh xưng là một dấu hiệu quen của văn do máy viết.
8. Người thầy và người quen của tác giả: theo cách gọi tác giả đã chốt, ghi ở mục Cấu hình cá nhân. Danh xưng kép theo quy ước nhà xuất bản (ví dụ "GS.TS").

Danh mục tham khảo đi kèm chính văn, từng mục định dạng chuẩn APA 7 (kèm đường dẫn DOI): bắt buộc có ở cuối bài đối với bài đăng tạp chí trí thức, bài phân tích nghiên cứu chuyên sâu, tham luận và sách. Chỉ ghi nguồn chính văn có nhắc; nguồn chỉ dùng để kiểm chứng thì ghi rõ "chỉ làm căn cứ kiểm chứng" và không đưa vào danh mục in; khi chính văn bỏ hay thêm một nghiên cứu, danh mục đổi theo ngay. Thứ tự sắp theo bảng chữ cái họ tác giả đầu theo chuẩn APA 7 (riêng sách bài tập có thể sắp theo chương và bài, mỗi phần theo chữ cái, nói rõ ở đầu danh mục).

## VII. Khi kiểm ra sai, hoặc không kiểm được

Chọn cách xử lý theo việc câu văn đang làm trong bài, theo thứ tự ưu tiên:

1. **Sửa cho đúng nguồn, giữ ý và giọng.** Đây là lựa chọn mặc định. Sửa tối thiểu: tinh chỉnh chứ không viết lại; giữ khung câu của người đã viết, chỉ thay phần sai.
2. **Thay nguồn đúng cho ý đúng.** Ý vẫn đúng nhưng gán nhầm người: tìm nghiên cứu thật sự cho thấy điều ấy (ý "người tự trắc ẩn có động lực sửa sai cao hơn" trỏ về Breines và Chen, 2012, không phải chung chung "Neff phát hiện").
3. **Chuyển thành nhận định của tác giả**, chỉ khi đó đúng là điều tác giả thấy và tác giả đồng ý ("Một số học viên của tôi thấy điểm tăng một, hai bậc" thay cho "phần lớn người thực hành đúng cách thấy điểm tăng 1-2 bậc", sau khi tác giả xác nhận đó là quan sát của mình).
4. **Bỏ tên, giữ ý**, khi ý tự đứng được mà không cần dựa vào uy tín của nguồn.
5. **Bỏ câu**, khi câu chỉ có giá trị nhờ nguồn mà nguồn không có thật.
6. **Cắm cờ cho tác giả**, khi lựa chọn thuộc về họ.

Trước khi cắt một nghiên cứu tốt nhưng khó tra, tra thêm một lớp (tên đầy đủ, cơ quan, DOI). Biên tập viên từng khôi phục một trích dẫn mà bản đề xuất đã cắt vì chưa tìm thấy.

Phân biệt hai tình huống trước khi bỏ một câu vì nguồn: **"đã xác định không tồn tại"** (tra đủ DOI, Crossref, Google Scholar, trang tạp chí, danh mục công bố của tác giả mà không có; được bỏ câu hoặc thay nguồn) và **"chưa kiểm được"** (bị chặn, thiếu công cụ, hết thời gian; chỉ được cắm cờ cho tác giả, không được bỏ như thể nguồn không có).

## VIII. Sự thật thuộc về tác giả

Một phần lớn rủi ro không nằm ở nghiên cứu mà ở chính đời tác giả, nhất là khi người khác (biên tập viên, AI) chạm vào bản thảo:

- Số liệu khảo sát tác giả tự làm: một tỷ lệ ghi 21% ở chương này, 22% ở bản tổng kết khảo sát. Tôi nêu lệch, tác giả chốt theo dữ liệu gốc.
- Mốc thời gian, tên tổ chức, chi tiết đời tư mà biên tập viên thêm hoặc đổi: tuổi của con, tên một tổ chức tác giả từng làm, tên một người thầy, một công việc cũ. Liệt kê cho tác giả xác nhận từng chỗ, không coi là đúng chỉ vì nghe hợp lý.
- Câu chuyện được nhắc lại ở chỗ khác trong sách phải là câu chuyện có thật trong sách; lời kết không được kể hai chuyện mà thân sách không có.
- Hồ sơ tác giả lưu ở đâu đó (trí nhớ của AI, trang giới thiệu cũ) không thay lời tác giả: hồ sơ ghi "hơn 20 năm làm nghề", sách ghi "gần 20 năm"; tác giả chốt con số đúng với thời điểm sách ra đời.

## IX. Trình bày kết quả

Kiểm chứng chỉ có ích khi người nhận làm theo được ngay. Hai người nhận, hai cách:

**Cho tác giả**: một danh sách gọn những điều chỉ tác giả trả lời được, mỗi dòng có chỗ trong sách, điều đang thấy, phương án đang dùng tạm, và chỗ để tác giả ghi ý kiến. Tách hẳn khỏi file gửi biên tập.

**Cho ban biên tập**, mỗi mục gồm:

- Vị trí: trang, mục, câu.
- Văn bản đang dàn: chép **nguyên văn** từ bản dàn để biên tập viên tìm được bằng chức năng Tìm. Đừng sửa chính tả trong phần này.
- Đề xuất sửa: văn bản dán được ngay, đã qua kiểm chứng và đã theo quy ước viết của sách. Chỉ dẫn dàn trang đặt riêng trong ngoặc vuông.
- Căn cứ kiểm chứng: nói đã đọc gì (tóm tắt, toàn văn, trang nào), trích ngắn nguyên văn câu then chốt của nguồn, và vì sao câu cũ lệch.
- Nguồn: APA 7 đầy đủ, có DOI.

Thêm vài điều làm bản trình bày dùng được lâu:

- Lỗi lặp ở nhiều nơi (thuật ngữ, dấu câu, kiểu dấu thanh, chức danh) gom thành quy tắc chung kèm số chỗ và danh sách vị trí, thay vì liệt kê từng câu.
- Giọng mô tả văn bản, không quy lỗi người ("Bản dàn bỏ mất phát hiện chính của..." chứ không "Ban biên tập xóa..."). Nhận rõ chỗ biên tập đã sửa đúng; chuyển các mục đã xong sang một phụ lục riêng để hai bên tiện đối chiếu.
- Mục còn chờ đối chiếu thêm thì đánh dấu tạm, ghi rõ còn thiếu gì; gỡ dấu khi đã xong. Không để mục chưa xong trông như đã xong.
- Ghi ngày kiểm và giới hạn của đợt kiểm (nguồn chưa đọc trọn, sách chưa đối chiếu trang bản quyền).
- Khi có nhiều vòng, bản sau đối chiếu lại toàn bộ trên bản dàn mới nhất; số trang, nguyên văn và danh sách vị trí đều đếm lại, không chép từ vòng trước.

## X. Một tiến trình gợi ý

Tiến trình dưới đây là đường đi thường gặp, không phải khuôn. Văn bản ngắn có thể gộp các khâu; văn bản dài như một cuốn sách cần đủ cả.

1. **Kiểm kê.** Đọc hết văn bản, tách theo đơn vị (chương, bài), liệt kê mọi câu nhắc người, công trình, con số, phát hiện, lời trích. Đây là việc của người đọc, không phải của bộ lọc từ khóa: nhiều câu khẳng định khoa học không chứa chữ "nghiên cứu".
2. **Xếp theo rủi ro.** Xếp theo loại câu, trước khi biết câu nào sai: câu dẫn tới hành động của người đọc (lời khuyên sức khỏe, thực hành), con số gây ấn tượng, câu gán phát hiện cho một tên lớn, lời trích trong ngoặc kép, rồi tới chi tiết thư mục.
3. **Truy và đối chiếu** theo bốn lớp ở mục IV. Với văn bản rất dài, có thể chia cho nhiều tác tử chạy song song, nhưng mọi phát hiện của tác tử đều được kiểm lại trước khi vào báo cáo, vì tác tử cũng có thể ảo giác.
4. **Phán định** từng mục: đúng; đúng nhưng cần tinh chỉnh; sai; nguồn đã xác định không tồn tại; chưa kiểm được. Kèm một trong bốn trạng thái kiểm ở điều không đổi số 2. "Chưa kiểm được" đi tới cờ cho tác giả (mục VII, lựa chọn 6), không đi tới việc bỏ câu.
5. **Đề xuất sửa** theo mục VII, rồi kiểm chính đề xuất (bất biến 5).
6. **Đối chiếu ngược** sau khi sửa và sau mỗi lần dàn trang: mỗi câu có nguồn quay lại sổ nguồn; danh mục tham khảo khớp chính văn; không còn câu sửa dở, câu gãy khi dàn, ghi chú biên tập sót lại.
7. **Ghi sổ và học** (mục XII).

Phần bề mặt đo được thì giao cho máy: so nguyên văn trích từ bản dàn với văn bản trong file, đếm dấu gạch dài và kiểu dấu thanh, tìm mã mục trùng, tìm cụm "hơn  năm" (số bị rơi). Phần nghĩa (nguồn nói gì, câu văn nói gì, hai bên có khớp không) chỉ đọc mới biết.

## XI. Tự kiểm trước khi giao

Hỏi, không đánh dấu cho xong:

- Có mục nào tôi gắn "đã kiểm" mà thật ra mới đọc nguồn thứ cấp?
- Có đề xuất sửa nào mang thêm một tên, con số, khẳng định tôi chưa kiểm?
- Động từ của mỗi câu về nghiên cứu đã khớp loại chứng cứ chưa, hay câu đang dựa vào một câu rào đón ở cuối đoạn?
- Có danh xưng nào tôi dùng vì nghe trang trọng hơn là vì đã xác minh?
- Có câu nào về đời tác giả tôi đã sửa thay vì hỏi?
- Phần "văn bản đang dàn" có đúng nguyên văn, để người nhận tìm thấy được không?
- Giọng của bản trình bày có tôn trọng người nhận không?
- Danh mục tham khảo có khớp chính văn hiện hành không?

## XII. Học từ bản chốt

Sau mỗi đợt, so bản tác giả chốt với bản tôi đề xuất. Mỗi chỗ tác giả sửa là một tín hiệu về độ chính xác hay về giọng: ghi lại nguyên lý đứng sau, không chỉ ghi chữ đã đổi. Góp ý lặp lần thứ hai thì sửa mặc định của skill. Chỉ đạo trực tiếp của tác giả trong một dự án thắng mặc định của skill.

SKILL.md này là bản đầy đủ và đứng được một mình. Nếu thư mục skill có `references/`, đọc thêm: `references/so-tay-loi-thuc-te.md` (lỗi thật theo bốn lớp, để luyện mắt trước khi kiểm một văn bản dài) và `references/mau-trinh-bay.md` (mẫu sổ nguồn, mục gửi biên tập, file việc tác giả cần chốt). Nếu đang làm trong repo xuong-viet-ai, `chuan/01-kiem-chung-va-trinh-bay-nghien-cuu.md` là bản tóm cho người và `docs/BAI-HOC.md` là nơi ghi bài học mới.

*Phiên bản 1.0, 16/10/2026. Phương pháp của Thạc sĩ Lương Dũng Nhân (M.Ed, PCC, Humanistic AI Practitioner), chưng cất từ đợt rà soát trích dẫn và ba vòng phản hồi ban biên tập của một cuốn sách thực hành (2026). Giấy phép CC BY 4.0.*

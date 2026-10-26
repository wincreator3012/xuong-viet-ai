# Xưởng viết AI

**Viết cùng trí năng nhân tạo [AI] mà văn vẫn là của mình, và mình viết giỏi lên sau mỗi bài.**

Xưởng viết AI là một bộ cách làm việc (gọi là "skill") kèm chuẩn nghề, công cụ nhỏ và một kho tư liệu nguyên bản, để trợ lý AI của bạn (Claude, ChatGPT, Gemini, Codex...) làm việc với bạn như một cộng sự biết điều: hỏi trước khi viết, tìm trong tư liệu của chính bạn trước khi hỏi, không bịa chuyện thay bạn, kiểm từng nguồn trước khi trích, nói rõ những chỗ nó đã quyết thay bạn, và giúp bạn tự viết giỏi hơn thay vì viết hộ bạn mãi.

Xưởng dành trước hết cho người viết có uy tín nghề nghiệp, viết tiếng Việt dưới tên mình: nhà giáo dục, giáo viên, giảng viên, nhà tham vấn, nhà trị liệu, nhà khai vấn [coach], người làm đào tạo, chuyên gia làm nghề độc lập: những người mà người đọc tin vì tin chính con người họ.

Xưởng miễn phí, mở, dùng lại được theo giấy phép CC BY 4.0 (tài liệu) và MIT (mã). Bạn không cần biết lập trình.

> **Repo này là bản vẽ, không phải phần mềm để tải về.** Bạn không cần bấm nút mã nguồn [Code] hay tải tệp nén [Download ZIP]. Bạn đưa đường dẫn repo cho trợ lý AI của mình; trợ lý đọc bản vẽ, hỏi bạn vài câu, rồi dựng trên máy bạn **một xưởng viết riêng**, kèm **kho tư liệu nguyên bản** để bạn đưa tư liệu của chính mình vào. Bạn là trợ lý AI đang đọc repo này: bắt đầu từ [`AGENTS.md`](AGENTS.md).

Mục lục: [Vì sao có xưởng này](#vì-sao-có-xưởng-này) · [Tinh thần của xưởng](#tinh-thần-của-xưởng) · [Bắt đầu bằng một câu](#bắt-đầu-bằng-một-câu) · [Bạn sẽ có gì trên máy](#bạn-sẽ-có-gì-trên-máy) · [Kho tư liệu nguyên bản](#kho-tư-liệu-nguyên-bản) · [Năm skill của xưởng](#năm-skill-của-xưởng) · [Một buổi làm việc mẫu](#một-buổi-làm-việc-mẫu-minh-họa) · [Những khái niệm bạn sẽ gặp](#những-khái-niệm-bạn-sẽ-gặp) · [Xưởng không làm gì](#xưởng-không-làm-gì) · [Câu hỏi thường gặp](#câu-hỏi-thường-gặp) · [Ghi công và giấy phép](#ghi-công-và-giấy-phép)

## Vì sao có xưởng này

AI viết rất nhanh và rất trơn. Nhưng người viết lâu năm nào dùng AI một thời gian cũng sẽ gặp vài điều khó chịu:

- **Văn ai cũng giống ai.** Bài nào cũng một kiểu mở, một nhịp, một kiểu kết, nghe "đúng" mà không nghe ra người viết. Nghiên cứu về viết cùng AI gợi ý rằng chính phần văn bản do mô hình đóng góp làm các bài giống nhau hơn (Doshi & Hauser, 2024; Padmakumar & He, 2024).
- **Bài đứng tên mình mà mình không thấy là của mình.** Người viết dễ mất cảm giác sở hữu, khó nhớ và khó bảo vệ điều "mình" đã viết (Draxler và cộng sự, 2024; Kosmyna và cộng sự, 2025, chưa bình duyệt).
- **Người đọc mất lòng tin** khi biết hay nghi một lá thư, một lời chia buồn, một bài tâm huyết là do AI viết (Liu và cộng sự, 2022; Hohenstein và cộng sự, 2023).
- **AI bịa.** Một câu trích dẫn "nghe rất thật", một nghiên cứu không tồn tại, một học viên chưa từng có, một chi tiết cơ thể không ai chứng kiến.

Phần lớn những nghiên cứu này làm bằng tiếng Anh, trên những bài viết ngắn; với tiếng Việt, chúng là gợi ý đáng để ý hơn là kết luận chắc chắn. Dù vậy, chúng khớp với điều người viết cảm thấy: vấn đề không nằm ở câu chữ, mà ở chỗ AI đang làm thay phần lẽ ra thuộc về người viết.

Xưởng này chưng cất từ nhiều tháng tác giả Lương Dũng Nhân viết bài báo, bản tin, bài mạng xã hội, sách thực hành cùng AI, và từ mỗi lần tác giả tự tay sửa bản AI soạn. Phần kiểm chứng chưng cất từ một đợt rà soát trích dẫn thật cho một cuốn sách thực hành: 214 nguồn, hơn 300 chỗ cần chỉnh, ba vòng làm việc với ban biên tập.

## Tinh thần của xưởng

**Sau mỗi câu có một người thật đứng.** Văn nguyên bản là văn mà chất liệu là của người viết, phán đoán là của người viết, và người viết sẵn lòng đứng tên. Vì vậy AI trong xưởng không bịa trải nghiệm, lời chứng thực, ca thực hành, con số, trích dẫn; khi được nhờ làm vậy, nó từ chối và gợi ý một lối thay thật.

**Chất liệu thật đến trước câu chữ.** Bài nguyên bản được viết từ những gì chỉ bạn có. Xưởng cho bạn một kho để giữ những thứ ấy, và dạy AI tìm trong kho trước khi hỏi, hỏi trước khi viết.

**Trân trọng con người, không thao túng.** Người viết, người đọc, và cả những người được nhắc tới trong bài đều được tôn trọng: chuyện của học viên, thân chủ, người thân được ẩn danh hoặc có đồng ý; không giật tít, không dọa, không khan hiếm giả, không khung "bị bỏ lại phía sau".

**Nguyên lý, không công thức.** Xưởng không có khuôn "bài nào cũng phải có năm phần". Mọi khung, bảng, tiêu chí là gương soi sau khi viết, không phải khuôn đúc trước khi viết. Ý trong bài được gọi lên bởi ý đứng trước nó và bởi điều người đọc đang mang trong mình; hướng của cả bài do bản chất chủ đề quyết.

**Người viết lớn lên.** Viết là cách để nghĩ. Nếu AI làm thay hết, nó lấy mất phần quý nhất của việc viết. Vì vậy xưởng có hẳn một skill để bạn tự viết, còn AI hỏi, phản biện, soi và cùng bạn nhìn lại.

## Bắt đầu bằng một câu

Mở một ứng dụng AI làm việc được với thư mục trên máy (khuyên dùng Claude Desktop ở chế độ Cowork; Claude Code, ChatGPT desktop chế độ Codex, Google Antigravity cũng được), gắn một thư mục trống tên `Viet AI`, rồi nói:

> Đọc bản vẽ xưởng viết ở https://github.com/wincreator3012/xuong-viet-ai (bắt đầu từ AGENTS.md) rồi dựng xưởng viết riêng cho tôi trong thư mục Viet AI.

Trợ lý sẽ dựng xưởng trong vài phút, rồi cùng bạn: ghi giọng văn của bạn qua ba lượt hỏi ngắn; tạo kho tư liệu và chỉ bạn đưa vài tư liệu đầu tiên vào; đóng gói bộ skill mang cấu hình của bạn để lưu vào tài khoản AI; giới thiệu xưởng làm được gì và cùng bạn chọn bài đầu tiên. Tổng cộng khoảng 40-60 phút.

Từng bước cho người mới hoàn toàn, kể cả cài ứng dụng: **[BAT-DAU.md](BAT-DAU.md)**.

**Chỉ dùng khung chat** (Claude trên web, ChatGPT, Gemini), chưa có ứng dụng làm việc với thư mục: vẫn dùng được, theo **đường nhẹ** trong `BAT-DAU.md`: tải các gói skill chung trong `dong-goi/` lên Claude, hoặc các tệp trong `dong-goi/tep-cho-du-an/` lên ChatGPT Projects, Gemini Gems. Trợ lý vẫn hỏi, soạn, soi, kiểm chứng; kho tư liệu khi ấy là các tệp bạn tải vào dự án.

Tên các nút, menu và gói tài khoản do từng hãng đặt và có thể đổi; khi khác với mô tả ở đây, trợ lý sẽ theo trang hướng dẫn chính thức của hãng.

## Bạn sẽ có gì trên máy

```
Documents/
└── Viet AI/
    ├── xuong-viet-ai/   xưởng của bạn: skill, chuẩn, công cụ, và giọng văn của bạn (phong-cach/GIONG-VAN.md)
    ├── Kho tu lieu/     kho tư liệu nguyên bản: sáu ngăn, hướng dẫn, mục lục
    └── Bai viet/        mỗi bài một thư mục: chất liệu, bản nháp, ghi chú bàn giao, sổ nguồn, bản chốt;
                         _skill/ chứa bộ skill riêng để lưu vào tài khoản AI
```

Xưởng dựng xong không nối với bản vẽ: không có gì tự đổi sau lưng bạn. Khi bản vẽ có bản mới, bạn nói "cập nhật xưởng"; trợ lý đọc nhật ký thay đổi (`CHANGELOG.md`), kể bạn nghe điều gì mới, rồi áp những gì bạn đồng ý. Giọng văn, kho tư liệu và bài viết của bạn không bao giờ bị ghi đè.

## Kho tư liệu nguyên bản

Kho là nơi giữ những thứ chỉ bạn có: chuyện bạn đã sống, điều bạn thấy trong nghề, lời bạn đã nói, bài bạn đã viết, tư liệu bạn đã đọc và tin. Khi bạn nhờ viết, trợ lý tìm trong kho trước, đưa bạn xem những gì có thể dùng kèm mức riêng tư, rồi mới hỏi phần còn thiếu. Nhờ vậy bạn không phải kể lại từ đầu mỗi lần, và bài không phải lấp chỗ trống bằng chuyện bịa hay câu chung chung.

| Ngăn | Để gì vào |
|---|---|
| `0 Moi them` | Thứ chưa biết xếp đâu; trợ lý đề xuất xếp, bạn đồng ý mới chuyển |
| `1 Ky uc va noi tam` | Nhật ký, ghi chú trên điện thoại, kỷ niệm, trăn trở chưa thành lời |
| `2 Loi noi` | Ghi âm sau buổi dạy, bài nói, podcast, phỏng vấn, bản gỡ băng |
| `3 Ban viet cua toi` | Bài đã đăng, bản chốt, thư, giáo án, ghi chép chuyên môn |
| `4 Tu lieu tham khao` | Nghiên cứu, trích sách, số liệu kèm nguồn; phản hồi học viên đã ẩn danh |
| `5 Hinh anh va do vat` | Ảnh lớp học, bảng trắng, sơ đồ vẽ tay, đồ vật có câu chuyện, kèm một dòng kể |

Bạn đưa tư liệu vào bằng cách kéo thả tệp vào đúng ngăn, rồi nói "xếp kho": trợ lý đề xuất một dòng mục lục cho mỗi tệp (nội dung, loại chất liệu, nguồn và ngày, mức riêng tư), bạn duyệt rồi mới ghi. Khi bài chốt, mục lục ghi lại tư liệu đã dùng ở bài nào, cho ai, để không kể lặp với cùng người đọc.

Về riêng tư: kho nằm trên máy bạn; trợ lý chỉ đọc khi bạn mở thư mục làm việc trong một phiên, chỉ đọc phần cần cho việc đang làm, và phần đã đọc được gửi tới dịch vụ AI bạn dùng như mọi điều bạn gõ vào khung chat. Tư liệu ghi "chỉ để mình đọc" không bao giờ được trích vào bài; chuyện của người khác dùng khi đã ẩn danh hoặc có đồng ý. Trợ lý không sửa, xóa, chuyển tệp nào trong kho khi bạn chưa đồng ý, và gói skill không mang theo tư liệu nào.

## Năm skill của xưởng

Mỗi skill là một thư mục trong `skills/`, có tệp `SKILL.md` đứng được một mình.

**Thiết lập (`viet-thiet-lap`).** Dựng kho tư liệu và thư mục bài, ghi giọng văn của bạn, dẫn bạn đưa tư liệu đầu tiên vào kho và xếp kho, đóng gói bộ skill riêng, giới thiệu xưởng. Gọi lại bất cứ lúc nào: "xếp kho", "đổi giọng văn", "kiểm tra xưởng".

**Tập viết (`tap-viet`): khi bạn muốn tự nghĩ, tự viết.** AI không soạn bản thay bạn. Bốn cửa:

- **Cùng nghĩ:** bạn có một trăn trở, một ý còn non. AI hỏi để neo ý vào chuyện thật (kể cả chuyện bạn đã ghi trong kho), phản chiếu lại bằng chính lời bạn, dựng phía phản biện mạnh nhất, rồi mời bạn tự nói ra "hạt giống của bài".
- **Định hình:** bạn biết muốn nói gì nhưng chưa biết nên viết thành gì. AI đưa hai ba phương án thể loại, thể thức, nói rõ cái được và cái giá của mỗi phương án.
- **Soi bản tự viết:** AI hỏi trước, nhận định sau, chỉ ra vài chỗ đáng sửa nhất kèm chứng cứ trong bài và hướng sửa, không viết lại thay bạn. Mức soi (nhanh, vừa, sâu) tùy chất lượng bạn muốn và thời gian còn lại.
- **Nhìn lại:** sau mỗi bài, hai câu hỏi ngắn để thấy điều bài viết đã dạy mình, và một hồ sơ người viết do chính bạn giữ.

**Viết nguyên bản (`viet-nguyen-ban`): khi bạn cần AI soạn từ chất liệu của bạn.** Bài chiêm nghiệm, bài quan điểm, bản tin, bài mạng xã hội chuyên môn, bài chuyển từ bài nói hay podcast, thư gửi học viên. AI tìm trong kho trước, rồi hỏi bạn chọn: phỏng vấn để lấy chất liệu còn thiếu; soạn ngay một bản có "cờ" ở chỗ cần chuyện thật của bạn; hoặc bạn viết thô trước. Bản nháp luôn kèm **ghi chú bàn giao**. Khi bạn gửi lại bản đã sửa, AI học từ chính những chỗ bạn sửa.

**Kiểm chứng (`kiem-chung`): khi bài có nguồn, con số, nhà nghiên cứu, lời trích.** Kiểm bốn lớp của mỗi trích dẫn: đúng người, đúng công trình, đúng điều nghiên cứu tìm thấy, đúng lời. Viết câu về nghiên cứu cho đúng mực, đặt mức chắc chắn vào động từ ("phát hiện", "có tương quan với", "nêu quan điểm rằng") thay vì chồng câu rào đón.

**Rà soát FACTUAL (`factual-review`): khi bạn muốn rà kỹ lập luận và dữ kiện.** Bảy chiều: dữ kiện, giả định, độ đầy đủ, rủi ro và thiên lệch, mức chắc chắn, lập luận, giới hạn. Skill viết bằng tiếng Anh nhưng trả báo cáo bằng ngôn ngữ của văn bản được rà.

### Chọn skill nào

Bạn không cần nhớ tên skill: nói việc bằng lời thường, trợ lý chọn đúng.

| Bạn đang có | Bạn muốn | Skill |
|---|---|---|
| Một ý, một trăn trở | Nghĩ cho rõ trước khi viết | `tap-viet`, cửa cùng nghĩ |
| Ý rõ, chưa biết viết thành gì | Chọn thể loại, nơi đăng, độ dài | `tap-viet`, cửa định hình |
| Chuyện thật, ghi âm, ghi chép trong kho | AI soạn thành bài | `viet-nguyen-ban` |
| Một bản tự viết | Được soi và góp ý, tự sửa | `tap-viet`, cửa soi bản tự viết |
| Bản thảo sách, chương trình, khóa học | Thẩm định kỹ theo ACCORD-ACCEPT | `tap-viet`, kèm `kiem-chung` |
| Bài có nhiều nguồn, con số | Kiểm từng trích dẫn | `kiem-chung` |
| Một văn bản cần rà lập luận | Rà giả định, thiên lệch, độ đầy đủ | `factual-review` |
| Bản bạn đã sửa xong từ bản AI soạn | Để AI học giọng bạn | `viet-nguyen-ban` (gửi lại "bản chốt") |
| Tư liệu mới vừa thả vào kho | Xếp vào mục lục | `viet-thiet-lap` ("xếp kho") |

## Một buổi làm việc mẫu (minh họa)

Đoạn dưới đây là minh họa do xưởng soạn để bạn hình dung cách làm việc, không phải lời của một người dùng thật.

> **Người viết:** Tôi đang có một ý về chuyện giáo viên ngại nói "tôi không biết" trước học trò. Nghĩ cùng tôi.
>
> **AI:** Lần gần nhất bạn thấy điều này là khi nào? Ai nói gì, và lúc ấy bạn đang ở vị trí nào: người đứng lớp, người dự giờ, hay người nghe kể lại?
>
> *(AI cũng tìm trong kho tư liệu của người viết và thấy một ghi âm sau buổi tập huấn tháng trước, mục lục ghi "ẩn danh khi dùng". AI hỏi: "Trong kho có ghi âm ngày 12, bạn kể về một giáo viên trẻ; chuyện ấy có liên quan không?")*
>
> **Người viết:** Tuần trước, một cô giáo trẻ trong lớp tập huấn của tôi kể cô bịa đại một đáp án khi học sinh hỏi câu khó, rồi mất ngủ cả đêm.
>
> **AI:** Bạn vừa dùng chữ "bịa đại". Theo bạn, cô ấy sợ điều gì nhất ở khoảnh khắc ấy? Và ai sẽ phản đối bạn mạnh nhất nếu bạn viết rằng giáo viên nên nói "tôi không biết"?
>
> *(Vài lượt sau)*
>
> **AI:** Nếu phải nói bằng lời thường, không dùng thuật ngữ nào, bài này nói về điều gì?
>
> **Người viết:** Học trò học được cách đối diện với điều mình chưa biết từ chính lúc thầy cô dám nói "tôi chưa biết".
>
> **AI:** Đó là hạt giống của bài, bằng lời của bạn. Bạn muốn viết thành một bài trong bản tin gửi đồng nghiệp, hay một bài báo cho phụ huynh? Hai lựa chọn này khác nhau ở người đọc, độ dài và cách mở bài...

Từ đây, người viết có thể tự viết rồi nhờ soi (`tap-viet`), hoặc nhờ AI soạn từ chất liệu vừa nói ra (`viet-nguyen-ban`). Dù chọn đường nào, câu chuyện của cô giáo được ẩn danh, mọi nghiên cứu được nhắc đều qua kiểm chứng, và khi bài chốt, mục lục kho ghi lại chuyện ấy đã dùng ở bài nào, cho ai.

## Những khái niệm bạn sẽ gặp

Bạn không cần thuộc những khái niệm này để dùng xưởng; AI sẽ dùng chúng thay bạn. Đọc qua để hiểu vì sao AI hỏi và soi như thế. Tên chính thức của mọi khái niệm ở `chuan/00-ten-goi-va-he-mo-hinh.md`.

**Chất liệu nguyên bản.** Những gì chỉ bạn có: thông tin độc đáo, cảm xúc chân thật, câu chuyện của mình, ý tưởng nguyên bản, triết lý sống (năm yếu tố IF-SIP). Chất liệu chỉ có ba hạng: ca thật (ẩn danh hoặc có đồng ý); ca ghép từ ít nhất ba người thật, có ghi rõ; hư cấu được gọi rõ ngay trong câu ("Giả sử..."). Thiếu chất liệu thì AI hỏi hoặc đánh dấu chỗ trống, không lấp bằng khái quát hay chi tiết tưởng tượng.

**Năm vai của người viết chuyên gia (STEPP).** Nhà nghiên cứu (giúp người đọc tin đúng mức), nhà đào tạo (giúp hiểu và làm được), nhà khởi nghiệp (giúp thấy đúng vấn đề và một lối giải mới), nhà thực hành (giúp thấy điều có thật từ thực hành), nhà chiêm nghiệm (giúp soi lại mình, nhìn tới gốc). Mỗi bài có một hai vai nói chính, các vai khác canh. Lỗi hay gặp nhất của AI là "diễn vai" khi không có chất liệu thật đứng sau, như thêm chi tiết cơ thể tưởng tượng hay một học giả thứ ba cho có vẻ uyên bác.

**Vòng viết năm chặng.** Tiếp nhận (bài này để làm gì, cho ai) - Nội quán (gốc của chủ đề là gì, mình đứng ở đâu) - Đồng kiến tạo (soạn từ chất liệu thật, kiểm nguồn) - Nghiền ngẫm (bản này còn là của mình không, đã đủ chín chưa) - Học hỏi (mình đã chọn khác AI ở đâu, và bài này để lại gì cho mình). Ba chặng giữa dựng trên chu trình ICC [Introspect - Co-create - Contemplate].

**Mức nguyên bản và mức dùng AI.** Thể loại càng gắn với con người bạn, AI càng lùi về vai hỏi, soi, biên tập. Biên bản, tóm tắt (mức Trung thành): AI soạn phần lớn, bạn kiểm. Bài giải thích, học liệu, đề xuất (Chuyên môn): hai bên cùng làm. Thư phản hồi, thư xin lỗi, thư mời (Hiện diện) và bài chiêm nghiệm, bài quan điểm, sách (Căn tính): bạn chủ đạo. Với truyện, AI không viết câu nào vào truyện.

**Ba bộ soi chất lượng.**

- *Tám phẩm chất* cho mọi văn bản: Chân thật, Chính xác, Nguyên bản, Làm chủ, Mạch lạc, Trong sáng, Phù hợp, Tôn trọng. Ba phẩm chất Chân thật, Nguyên bản, Làm chủ chỉ người viết thẩm định được, nên một bài chưa qua tay người viết thì chưa xong.
- *FACTUAL* cho lập luận và dữ kiện.
- *ACCORD-ACCEPT* cho tác phẩm hướng tới chuyển hóa người đọc (sách, chương trình, khóa học, bài dài): mười hai tiêu chí, ba mức Xuất sắc, Đạt chuẩn, Cần cải thiện. Dùng linh hoạt: không tác phẩm nào phải đạt mức cao nhất ở mọi tiêu chí; mỗi nhận định đi kèm chứng cứ trong bài và hướng sửa.

**Bản chốt và ghi chú bàn giao.** Bản chốt là bản bạn đã tự sửa và đăng hay gửi đi. Đó là nguồn học quý nhất về giọng của bạn, đáng tin hơn mọi bản "phân tích phong cách". Ghi chú bàn giao là lời AI nói thật về những gì nó đã làm với bài của bạn, để bạn duyệt thay vì phải đoán.

## Xưởng không làm gì

- Không viết bài mang tên bạn khi chưa có chất liệu của bạn, và không dựng trải nghiệm, lời chứng thực, nghiên cứu, con số.
- Không viết truyện thay bạn; với hư cấu, AI chỉ hỏi và soi.
- Không phải công cụ "qua mặt máy phát hiện AI". Các máy ấy không đáng tin và thiên lệch với người viết ngôn ngữ thứ hai (Liang và cộng sự, 2023); xưởng nhắm vào chất lượng thật của văn, không vào điểm số của máy.
- Không đóng vai nhà trị liệu. Khi chất liệu chạm một tổn thương còn đang sống, AI dừng hỏi thêm, hỏi bạn muốn dừng hay chuyển hướng, và gợi ý tìm người đồng hành chuyên môn khi phù hợp.
- Không phải tư vấn pháp lý, và không thay tổng quan tài liệu học thuật cấp luận án.
- Không thay được biên tập viên, người đọc thân quen, hay chính sự chín chắn của bạn.

Giới hạn hiện tại: xưởng làm tốt nhất với tiếng Việt; chuẩn cho văn tiếng Anh đang được soạn. Kiểm chứng cần AI có công cụ tìm kiếm web; không có công cụ ấy, AI sẽ chỉ ra những câu cần kiểm và vì sao, chứ không phán đúng sai.

## Câu hỏi thường gặp

**Tôi không rành công nghệ, có dùng được không?**
Được. Bạn tạo một thư mục, gắn vào ứng dụng AI, dán một câu; trợ lý làm phần còn lại và hỏi bạn bằng lời thường. `BAT-DAU.md` đi từng bước, kể cả cài ứng dụng. Chỉ dùng khung chat thì theo đường nhẹ.

**Có mất phí không?**
Xưởng miễn phí. Bạn cần tài khoản của một trợ lý AI; chế độ làm việc với thư mục (như Cowork của Claude) và tính năng Skills tùy gói tài khoản của từng hãng.

**Bài viết và tư liệu của tôi đi đâu?**
Repo này không thu thập gì. Xưởng, kho tư liệu và bài viết nằm trên máy bạn. Phần trợ lý đọc trong một phiên được gửi tới dịch vụ AI bạn dùng, theo chính sách của hãng ấy. Với chuyện của học viên, thân chủ, người thân, hãy ẩn danh ngay khi ghi vào kho.

**Văn của tôi có bị kéo theo giọng của tác giả xưởng không?**
Không. Skill không chứa giọng của ai. Giọng của bạn đến từ tệp giọng văn bạn khai, từ tư liệu và bài cũ của chính bạn trong kho, và từ bản chốt của bạn. Xưởng chỉ giữ chung những nguyên lý và quy ước nền về tiếng Việt, và bạn sửa được cả những quy ước ấy.

**Tôi đã có kho ghi chép riêng (Obsidian, một thư mục ghi chú). Có phải chép sang không?**
Không bắt buộc. Lúc dựng xưởng, trợ lý hỏi bạn đang giữ ghi chép ở đâu; bạn có thể dùng luôn thư mục ấy làm kho, trợ lý chỉ thêm tệp hướng dẫn và mục lục, không sắp xếp lại ghi chép của bạn.

**Tôi có phải ghi "bài này có AI hỗ trợ" không?**
Xưởng không quyết thay bạn. Một cách nghĩ hữu ích: khi bạn đã viết lại và chịu trách nhiệm từng câu, như làm việc với một biên tập viên, nhiều người chọn có một lời giới thiệu chung về cách mình làm việc với AI thay vì gắn nhãn từng bài; khi phần lớn nội dung do AI tạo mà bạn không viết lại, khi có hình ảnh, giọng nói, video do AI tạo, hay khi nơi đăng, tạp chí, hợp đồng yêu cầu, hãy ghi rõ. Đây không phải tư vấn pháp lý; hãy đối chiếu quy định hiện hành nơi bạn làm việc và đăng bài.

**Dùng cho học sinh, sinh viên được không?**
Xưởng thiết kế cho người viết chuyên nghiệp. Với người đang học viết, `tap-viet` hợp hơn `viet-nguyen-ban`, vì AI hỏi và soi chứ không soạn thay; nên có thầy cô đồng hành, và tuân thủ quy định về liêm chính học thuật của trường.

**Tôi muốn sửa skill cho hợp với mình thì sao?**
Cứ sửa trong xưởng của bạn (`xuong-viet-ai/skills/`), rồi nhờ trợ lý "đóng gói lại skill". Khi cập nhật xưởng, tệp bạn đã sửa được giữ nguyên và trợ lý hỏi bạn muốn giữ, lấy bản mới, hay trộn. Hãy giữ ghi công tác giả theo giấy phép CC BY 4.0.

**Xưởng có cập nhật không?**
Có. Nhật ký thay đổi ở `CHANGELOG.md`; bài học mới ở `docs/BAI-HOC.md`. Trong xưởng của bạn, nói "cập nhật xưởng".

## Bản vẽ gồm gì

| Tệp, thư mục | Nội dung |
|---|---|
| `README.md`, `BAT-DAU.md` | Cho người dùng: giới thiệu, bắt đầu từng bước (cả đường nhẹ) |
| `AGENTS.md`, `CLAUDE.md`, `GEMINI.md` | Cửa vào cho trợ lý AI (hai tệp sau trỏ về `AGENTS.md`) |
| `DUNG-XUONG.md` | Quy trình dựng, cập nhật, gỡ rối (cho trợ lý) |
| `BAN-DUNG.json` | Danh mục từng tệp: chép vào xưởng, mẫu để điền, hay chỉ ở bản vẽ; vân tay sha256 |
| `CHANGELOG.md` | Nhật ký thay đổi: trợ lý đọc khi cập nhật xưởng của bạn |
| `HUONG-DAN.md` | Cách dùng xưởng hằng ngày (được chép vào xưởng) |
| `skills/` | Năm skill; `skills/README.md` giải thích skill và cách lưu vào tài khoản |
| `chuan/` | Bản tóm cho người đọc: `00` tên gọi và hệ mô hình, `01` kiểm chứng, `02` viết nguyên bản, `03` học từ bản chốt, `04` từ và cấu trúc tiếng Việt |
| `khuon/` | Khuôn kho tư liệu (sáu ngăn, hướng dẫn, mục lục) và thư mục bài |
| `phong-cach/` | Bản khởi đầu giọng văn, sổ bài học giọng, hồ sơ người viết (`.mau.md`) |
| `tools/` | Công cụ Python, chỉ dùng thư viện chuẩn: dựng và kiểm xưởng, cài đặt, kho tư liệu, bài mới, đóng gói skill, rà từ và cấu trúc, chuẩn hóa dấu thanh, đối chiếu nguyên văn |
| `mau-xuong/` | Mẫu tệp điểm vào của xưởng dựng ra |
| `dong-goi/` | Gói skill chung cho đường nhẹ: tệp `.zip` cho Claude, `tep-cho-du-an/` cho ChatGPT, Gemini, Claude Projects |
| `docs/` | `BAI-HOC.md` (bài học theo chủ đề), `DONG-GOP.md` (cho người bảo trì) |
| `GHI-CONG.md`, `LICENSE`, `LICENSE-TAI-LIEU.md` | Ghi công và giấy phép |

## Góp ý

Nếu bạn dùng xưởng và thấy một chỗ chưa ổn (AI vẫn bịa, vẫn rập khuôn, một quy ước không hợp tiếng Việt, một hướng dẫn khó hiểu), hãy mở một issue trên GitHub, kèm đoạn trước và sau nếu có, đã ẩn danh. Bài học từ người dùng được ghi vào `docs/BAI-HOC.md`.

## Ghi công và giấy phép

Phương pháp và nội dung: Thạc sĩ Lương Dũng Nhân (M.Ed, PCC, Humanistic AI Practitioner), gồm khung năm vai STEPP, chu trình ICC, nguyên lý "ý sinh theo duyên, mạch thuận theo pháp", tám phẩm chất của văn bản, khung FACTUAL và bộ tiêu chí ACCORD-ACCEPT. Các khung và nghiên cứu của tác giả khác được ghi công ngay tại chỗ dùng. Mô hình tổ chức "bản vẽ dựng xưởng riêng" dùng chung với các xưởng web, xưởng phim, xưởng thiết kế cùng tác giả.

Tài liệu theo giấy phép CC BY 4.0 (`LICENSE-TAI-LIEU.md`); mã trong `tools/` theo giấy phép MIT (`LICENSE`). Bạn được dùng lại, chỉnh sửa, kể cả cho mục đích thương mại, miễn là ghi công. Cách ghi gợi ý ở `GHI-CONG.md`:

> Lương Dũng Nhân. (2026). *Xưởng viết AI* [Bộ skill và chuẩn viết cùng AI]. https://github.com/wincreator3012/xuong-viet-ai

Bài bạn viết RA bằng xưởng là của bạn: không cần ghi công xưởng trong bài.

Cập nhật lần cuối: 26/10/2026.

## In English

*Xưởng viết AI* (AI Writing Workshop) is a free, open blueprint for writing with AI assistants (Claude, ChatGPT, Gemini, Codex) so that the text stays yours and you grow as a writer. Give the repository link to an assistant that can work with folders on your computer, and it builds a personal workshop there: five skills, standards, small tools, your own voice profile, and a library for your original material (memories, recordings, past writing, references, images) that the assistant searches before it asks you anything. It is built for professionals who write in Vietnamese under their own name, such as educators, counsellors, coaches and trainers. Its principles: no fabricated stories, sources or testimonials; respect for readers and for the people a text mentions; principles instead of templates. A lighter path uses the packaged skills in `dong-goi/` inside a chat. The skills are written in Vietnamese; standards for English prose are in progress. Method and content by Luong Dung Nhan (M.Ed, PCC), licensed CC BY 4.0 (documents) and MIT (code).

## Lời cuối

Xưởng này không hứa làm bạn viết nhanh hơn. Nó mời bạn viết chậm đúng chỗ, giữ lại những gì mình đã sống, để mỗi bài còn mang hơi thở của chính mình. Lần gần nhất bạn đọc lại một bài mình viết cùng AI, bạn có còn nhận ra mình trong từng câu không?

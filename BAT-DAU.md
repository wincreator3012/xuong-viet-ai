# Bắt đầu: để trợ lý AI dựng xưởng viết cho bạn, từng bước

Tài liệu này dành cho cả người chưa từng dùng AI làm việc với tệp trên máy. Đọc hết một lần khoảng mười phút; làm theo khoảng 40-60 phút, phần lớn là trả lời vài câu hỏi và chọn tư liệu của chính bạn. Bạn không cần tải gì từ GitHub và không phải gõ lệnh nào: trợ lý AI đọc bản vẽ rồi dựng xưởng trên máy bạn. Giới thiệu chung ở [README.md](README.md).

Có hai đường:

- **Đường chính: dựng xưởng trên máy** (bước 1 tới 6). Bạn có xưởng riêng, kho tư liệu nguyên bản, thư mục bài viết, bộ skill mang giọng của bạn. Cần một ứng dụng AI làm việc được với thư mục trên máy.
- **Đường nhẹ: chỉ dùng khung chat** (mục cuối). Dùng các gói skill chung trên Claude, ChatGPT hay Gemini, không có kho trên máy. Hợp khi bạn muốn thử trước, hoặc chưa có ứng dụng làm việc với thư mục.

## Trước khi bắt đầu, bạn cần

- **Một máy tính** Mac hoặc Windows 10/11.
- **Một ứng dụng AI làm việc được với thư mục trên máy** (bước 1).
- **Mạng ổn định** trong vài phút dựng xưởng (trợ lý đọc khoảng 60 tệp chữ từ bản vẽ, dung lượng nhỏ).
- **Một bài bạn đang muốn viết**, hay một ý đang ấp ủ.
- **Vài tư liệu của chính bạn** (nên có, không bắt buộc): hai ba bài bạn đã viết và hài lòng, một ghi chép hay ghi âm gần đây, một nghiên cứu bạn hay dẫn. Bước 4 sẽ đưa chúng vào kho.

## Bước 1: cài một ứng dụng AI làm việc được với thư mục

Xưởng được viết và kiểm chứng trên Claude; các ứng dụng khác dùng được vì xưởng là tệp chữ và công cụ Python thông thường. Chọn MỘT:

| Ứng dụng | Hợp với ai | Ghi chú |
|---|---|---|
| **Claude Desktop** (chế độ Cowork) | người mới, muốn ít trục trặc nhất | Khuyên dùng. Tải ở [claude.ai/download](https://claude.ai/download); Cowork cần gói trả phí. Claude làm việc với thư mục bạn gắn vào |
| **ChatGPT desktop** (chế độ Codex) | người đang dùng ChatGPT | Mở một thư mục rồi làm việc trong đó; khung chat thường không dựng được xưởng |
| **Google Antigravity** | người quen sản phẩm Google | Mở thư mục làm dự án |
| **Claude Code**, Codex CLI, Cursor | người quen dòng lệnh | Chạy thẳng trên máy |

Giá, gói và tên gọi của các ứng dụng AI thay đổi nhanh; xem trang chính thức của từng hãng trước khi đăng ký.

## Bước 2: tạo thư mục làm việc và gắn vào ứng dụng

1. Mở thư mục tài liệu [Documents], tạo một thư mục mới, để trống, tên **Viet AI** (đã có `Viet AI` từ đường nhẹ thì dùng luôn thư mục ấy). Đây là nơi chứa xưởng, kho tư liệu và mọi bài bạn viết.
2. Gắn thư mục đó vào ứng dụng:
   - **Claude Desktop, Cowork**: bắt đầu một phiên mới, bấm nút thêm thư mục [Add folder], chọn `Viet AI`. Lần đầu, máy có thể hỏi quyền truy cập thư mục: bấm cho phép.
   - **ChatGPT desktop, Codex**: chọn mở thư mục [Open folder] hoặc tạo dự án từ thư mục `Viet AI`.
   - **Antigravity, Cursor**: vào menu tệp [File], chọn mở thư mục [Open Folder], chọn `Viet AI`.

Từ lúc này trợ lý đọc và ghi được trong thư mục đó, và chỉ thư mục đó.

Một điều nên nghĩ trước: kho tư liệu sẽ nằm trong thư mục này. Đặt `Viet AI` trong iCloud Drive, Google Drive, Dropbox hay OneDrive thì dùng được trên nhiều máy, nhưng tư liệu cũng được đồng bộ lên dịch vụ ấy. Đặt ở đâu là quyết định của bạn.

## Bước 3: nói câu đầu tiên

Gõ vào khung chat:

> Đọc bản vẽ xưởng viết ở https://github.com/wincreator3012/xuong-viet-ai (bắt đầu từ AGENTS.md) rồi dựng xưởng viết riêng cho tôi trong thư mục Viet AI.

Trợ lý tự đọc bản vẽ trên GitHub. Bạn không cần mở trang GitHub, không bấm nút tải về nào.

## Bước 4: chuyện gì sẽ xảy ra

**Vài câu hỏi đầu (2 phút).** Trợ lý hỏi một lượt: dùng thư mục nào, gọi bạn là gì, bạn dùng ứng dụng AI nào hằng ngày, bạn đang giữ ghi chép ở đâu. Nếu bạn đã có một kho ghi chép riêng (ví dụ một thư mục Obsidian), bạn có thể chọn dùng luôn nó làm kho.

**Dựng xưởng (vài phút, bạn chỉ chờ).** Trợ lý chép phần năng lực (skill, chuẩn, công cụ) vào `Viet AI/xuong-viet-ai` và tự kiểm từng tệp khớp bản vẽ, rồi tạo `Viet AI/Kho tu lieu` và `Viet AI/Bai viet`. Máy thiếu Python thì trợ lý hướng dẫn cài (mục "Nếu máy chưa có Python").

**Giọng văn của bạn (10-15 phút).** Trợ lý hỏi ba lượt ngắn, mỗi lượt vài câu có sẵn lựa chọn:

- Bạn là ai: tên viết dưới bài đúng nguyên văn (kèm học vị nếu có), cách trợ lý gọi bạn, nghề, kinh nghiệm viết.
- Những vai bạn thật sự giữ khi viết (nghiên cứu, đào tạo, nhận diện vấn đề và sáng tạo lối giải, thực hành nghề, chiêm nghiệm), mỗi vai một chất liệu có thật đứng sau; người đọc và kênh của bạn.
- Chữ viết thế nào: quy ước ngôn ngữ (giữ mặc định hay đổi), từ bạn dùng theo nghĩa riêng, từ bạn không bao giờ dùng; bạn muốn trợ lý phỏng vấn trước, soạn có cờ, hay để bạn viết thô trước.

Trả lời tới đâu trợ lý ghi tới đó vào `xuong-viet-ai/phong-cach/GIONG-VAN.md`. Câu nào chưa muốn trả lời thì để sau; trợ lý không đoán thay. Sau này bạn mở tệp ấy đọc lại, sửa tay được, hoặc chỉ cần nói "từ nay...".

**Kho tư liệu (10-20 phút).** Trợ lý giải thích kho, chỉ bạn thư mục `Kho tu lieu` trên máy và sáu ngăn của nó, rồi gợi ý ba đến năm tư liệu đầu tiên hợp với điều bạn sắp viết. Bạn tự kéo thả tệp vào đúng ngăn (không biết để đâu thì thả vào `0 Moi them`), hoặc kể ngay một chuyện để trợ lý ghi lại đúng lời bạn. Rồi trợ lý "xếp kho": đề xuất một dòng mục lục cho mỗi tư liệu (nội dung, loại chất liệu, nguồn và ngày, mức riêng tư), bạn duyệt rồi mới ghi. Chưa có tư liệu lúc này cũng không sao: thả sau, rồi nói "xếp kho".

**Bộ skill riêng (5-10 phút).** Skill là một cách làm việc đã kiểm chứng viết thành tệp chữ, để trợ lý mở ra đúng lúc, như một cuốn sổ tay nghề. Trợ lý đóng gói năm skill mang cấu hình và bản chụp giọng văn của bạn vào `Viet AI/Bai viet/_skill/` (không mang tư liệu nào trong kho), rồi dẫn bạn lưu vào tài khoản AI. Bạn tự bấm tải lên; trợ lý chỉ từng bước. Không muốn lưu lúc này cũng được: xưởng vẫn chạy đủ khi bạn mở thư mục.

**Giới thiệu xưởng (khoảng 10 phút).** Trợ lý giải thích xưởng làm được gì cho bạn, một bài đi qua những bước nào, việc nào chỉ bạn làm được, vài thói quen nuôi kho, những gì xưởng chưa làm, rồi cùng bạn chọn bài đầu tiên. Muốn nghe lại lúc nào cũng được: "giới thiệu lại xưởng".

Kết quả trên máy bạn:

```
Documents/
└── Viet AI/
    ├── xuong-viet-ai/   xưởng của bạn (năng lực + giọng văn của bạn)
    ├── Kho tu lieu/     kho tư liệu nguyên bản: sáu ngăn, hướng dẫn, mục lục
    └── Bai viet/        mỗi bài một thư mục; _skill/ là bộ skill riêng
```

## Bước 5: bài đầu tiên

Chọn một bài ngắn, thật, sắp dùng. Nói với trợ lý một câu có đủ ba ý: muốn gì, cho ai, đăng đâu. Ví dụ (do xưởng soạn để minh họa):

> Tôi đang có một ý về chuyện giáo viên ngại nói "tôi chưa biết" trước học trò. Nghĩ cùng tôi, đừng viết gì cả.

> Viết giúp tôi bài cho bản tin tháng này gửi phụ huynh, về chuyện so sánh con với "con nhà người ta". Tìm trong kho trước, rồi phỏng vấn tôi phần còn thiếu.

Câu mở đầu cho từng việc, thói quen nuôi kho, gỡ rối: `HUONG-DAN.md` trong xưởng của bạn.

## Bước 6: những điều nên biết

- **Xưởng là của bạn, không nối với bản vẽ.** Không có gì tự đổi sau lưng bạn. Muốn nhận bản mới: nói "cập nhật xưởng"; trợ lý kể bạn nghe điều gì mới rồi mới áp. Giọng văn, kho tư liệu và bài viết của bạn không bị đụng tới.
- **Mỗi phiên làm việc, gắn thư mục `Viet AI`** (thư mục cha), không chỉ thư mục xưởng, để trợ lý đọc được kho và ghi được bài.
- **Mật khẩu là của bạn.** Trợ lý không bao giờ hỏi mật khẩu, mã xác thực, mã khôi phục. Ai hỏi những thứ đó, kể cả một trợ lý AI, thì đừng đưa. Đừng để những thứ ấy trong kho.
- **Đổi giọng văn** (tên, xưng hô, quy ước, từ của bạn): nói "đổi giọng văn" hoặc "từ nay...". Đã lưu skill lên tài khoản thì nhờ "đóng gói lại skill".
- **Dùng trên máy khác**: đặt `Viet AI` trong dịch vụ đồng bộ (cân nhắc riêng tư như ở bước 2), chờ tệp tải hết về rồi nói "kiểm tra xưởng".

## Nếu máy chưa có Python

- **Mac**: Python 3 thường có sẵn. Chưa có thì trợ lý hướng dẫn cài, hoặc tải bản cài từ [python.org](https://www.python.org/downloads/).
- **Windows**: tải bản cài từ [python.org](https://www.python.org/downloads/), lúc cài nhớ đánh dấu ô "Add python.exe to PATH". Trên Windows, lệnh là `py` thay cho `python3`.

Claude Cowork có sẵn Python trong máy làm việc của nó; bạn thường không cần cài gì.

## Khi có gì không chạy

Nói với trợ lý điều bạn thấy, bằng lời thường ("nó dừng ở chỗ chép tệp", "không thấy thư mục kho"). Ba việc bạn tự kiểm được: thư mục `Viet AI` còn được gắn vào ứng dụng không; máy còn mạng không; ổ đĩa còn chỗ không. Muốn trợ lý tự kiểm toàn bộ, nói: "kiểm tra xưởng".

---

## Đường nhẹ: chỉ dùng khung chat

Khi bạn chưa có ứng dụng làm việc được với thư mục, hoặc muốn thử trước. Bạn có các skill trong khung chat; chưa có kho tư liệu trên máy, chưa có công cụ, và giọng văn là một tệp hay một đoạn chỉ dẫn bạn tự giữ.

Lấy các tệp: trên trang GitHub của repo, mở thư mục `dong-goi/`, bấm vào từng tệp cần dùng rồi bấm nút tải tệp gốc [Download raw file]. Hoặc nhờ trợ lý có duyệt web lấy giúp. Tên nút trên GitHub có thể đổi theo thời gian.

### Claude, dùng Skills

Theo [hướng dẫn của Anthropic](https://support.claude.com/en/articles/12512180-using-skills-in-claude), Skills có ở các gói Pro, Max, Team và Enterprise, và cần bật tính năng chạy mã.

1. Mở cài đặt [Settings] > tính năng [Capabilities], bật công tắc chạy mã và tạo tệp [Code execution and file creation].
2. Mở trang skill [Skills] (trong mục tùy chỉnh [Customize]; một số tài khoản thấy ngay trong cài đặt tính năng [Capabilities]), bấm tải skill lên, chọn một tệp `.zip` trong `dong-goi/`. Lặp lại cho từng skill: `viet-thiet-lap.zip`, `tap-viet.zip`, `viet-nguyen-ban.zip`, `kiem-chung.zip`, `factual-review.zip`. Không giải nén.
3. Mở một cuộc trò chuyện mới, nói "thiết lập xưởng viết cho tôi". Skill thiết lập sẽ hỏi giọng văn của bạn và trả về tệp `GIONG-VAN.md` để bạn giữ; có công cụ chạy mã thì nó dựng sẵn tệp nén `Viet AI.zip` (kho tư liệu sáu ngăn và thư mục bài) để bạn tải về, giải nén vào Documents. Sau này khi có ứng dụng làm việc với thư mục, bạn dựng xưởng đầy đủ và dùng lại đúng thư mục ấy.

### ChatGPT, dùng Projects

1. Ở thanh bên, chọn dự án mới [New project], đặt tên ví dụ "Xưởng viết" (xem [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)).
2. Tải lên các tệp trong `dong-goi/tep-cho-du-an/` (mỗi lần tối đa mười tệp). Theo trang hướng dẫn của OpenAI, gói miễn phí chỉ nhận năm tệp mỗi Project; khi đó chọn năm tệp hợp việc bạn làm nhiều nhất, ví dụ `tap-viet.md`, `viet-nguyen-ban.md`, `viet-nguyen-ban--tu-vung-va-cau-truc.md`, `kiem-chung.md`, `viet-thiet-lap.md`, và dán giọng văn của bạn vào phần chỉ dẫn thay vì tải thành tệp.
3. Mở menu ba chấm của Project, chọn cài đặt dự án [Project settings], dán đoạn chỉ dẫn mẫu dưới đây vào phần chỉ dẫn [instructions].
4. Mở một cuộc trò chuyện trong Project, nói "thiết lập xưởng viết cho tôi".

### Gemini, dùng Gems

1. Mở trang Gem [Gems], chọn tạo Gem mới [New Gem], đặt tên (xem [Use Gems in Gemini Apps](https://support.google.com/gemini/answer/15146780)).
2. Dán đoạn chỉ dẫn mẫu vào phần chỉ dẫn; ở mục tri thức [Knowledge], chọn thêm tệp [Add files], thêm các tệp như phần ChatGPT.
3. Bấm lưu [Save], rồi nói "thiết lập xưởng viết cho tôi".

Trang hướng dẫn của Google cho biết từ tháng 11/2026, Gems trên tài khoản Google cá nhân sẽ chuyển dần sang dạng skills. Khi tài khoản của bạn đã đổi, làm theo hướng dẫn mới của Google; nội dung cần đưa vào vẫn là các tệp trong `dong-goi/`.

### Claude Projects, khi tài khoản chưa có Skills

Làm như phần ChatGPT: tạo một Project, tải các tệp trong `dong-goi/tep-cho-du-an/` vào phần tri thức, dán đoạn chỉ dẫn mẫu vào phần chỉ dẫn.

### Tư liệu trong khung chat

Tải tư liệu của bạn vào phần tri thức của Project hay Gem, tên tệp bắt đầu bằng số ngăn để trợ lý biết loại chất liệu: `1` ký ức và nội tâm, `2` lời nói, `3` bản viết của bạn, `4` tư liệu tham khảo, `5` hình ảnh và đồ vật. Ví dụ: `1 - 2026-10-20 hoc tro hoi cau kho.md`. Ẩn danh chuyện của người khác trước khi tải lên.

### Đoạn chỉ dẫn mẫu

```
Bạn làm việc với tôi theo Xưởng viết AI (phương pháp của Thạc sĩ Lương Dũng Nhân). Các tệp trong phần tri thức là các skill của xưởng; tệp có tên "ten-skill--ten-tep.md" là tệp tham chiếu "references/ten-tep.md" của skill ấy. Tệp có tên bắt đầu bằng số 1 tới 5 là tư liệu nguyên bản của tôi.

Chọn skill theo việc:
- Thiết lập, ghi giọng văn, sắp xếp tư liệu: làm theo viet-thiet-lap.md (chế độ nhẹ).
- Tôi muốn tự nghĩ, tự viết, nhờ góp ý mà không viết lại, chọn thể loại, nhìn lại sau bài, hay thẩm định bản thảo, chương trình: làm theo tap-viet.md.
- Tôi nhờ soạn bài dưới tên tôi: làm theo viet-nguyen-ban.md; tìm trong tư liệu của tôi trước khi hỏi.
- Văn bản có nguồn, con số, nhà nghiên cứu, lời trích: làm theo kiem-chung.md.
- Tôi nhờ rà lập luận theo FACTUAL: làm theo factual-review.md.

Luôn giữ: không bịa chuyện, nguồn, con số, lời chứng thực; thiếu thì hỏi tôi. Hỏi trước khi viết. Mỗi bản nháp kèm ghi chú bàn giao. Chuyện của người khác trong tư liệu của tôi chỉ dùng khi đã ẩn danh hoặc có đồng ý.

Giọng văn của tôi (dán nội dung tệp GIONG-VAN.md, hoặc điền ngắn):
- Tên viết dưới bài, cách gọi tôi:
- Nghề, và những vai tôi thật sự giữ (nghiên cứu, đào tạo, nhận diện vấn đề và sáng tạo lối giải, thực hành nghề, chiêm nghiệm):
- Người đọc và kênh chính:
- Quy ước ngôn ngữ (thuật ngữ nước ngoài, dấu câu, kiểu dấu thanh, từ tôi tránh, từ tôi hay dùng):
- Kinh nghiệm viết của tôi (mới viết, đang lớn, lâu năm):
```

# Skill của xưởng: là gì, sống ở đâu, lưu vào tài khoản AI thế nào

Tài liệu này dành cho bạn, chủ xưởng, và cho trợ lý AI đang hướng dẫn bạn. Đọc một lần khoảng năm phút; phần "Lưu vào tài khoản" làm theo từng bước cùng trợ lý.

## Skill là gì, nói bằng lời thường

Skill là một cách làm việc đã được kiểm chứng, viết thành tệp chữ `SKILL.md` để trợ lý AI đọc và làm theo. Hình dung một cuốn sổ tay nghề: khi bạn nói "nghĩ cùng tôi về chuyện này", trợ lý mở đúng cuốn sổ tập viết, đi đúng cách đã định (hỏi trước, không viết thay, soi khi bạn nhờ) thay vì mỗi lần nghĩ lại từ đầu. Nhờ vậy cách làm việc đều tay, và những gì bạn đã dặn "từ nay" được giữ lại.

Skill không phải phần mềm cài vào máy và không chạy ngầm. Nó chỉ là chỉ dẫn; trợ lý đọc nó khi việc bạn nhờ khớp với phần mô tả ở đầu tệp. Khi skill bảo tìm trong kho tư liệu, trợ lý chỉ đọc được kho trong phiên bạn đã gắn thư mục làm việc.

## Xưởng có năm skill

| Skill trong xưởng | Tên trên tài khoản AI của bạn | Trợ lý dùng khi bạn |
|---|---|---|
| `skills/viet-thiet-lap/` | `xuong-viet-thiet-lap` | thiết lập lần đầu, xếp kho tư liệu, đổi giọng văn, hỏi "xưởng làm được gì", nhờ đóng gói lại skill |
| `skills/tap-viet/` | `xuong-viet-tap-viet` | muốn tự nghĩ, tự viết; cần hỏi, phản biện, soi, nhìn lại; thẩm định bản thảo theo ACCORD-ACCEPT |
| `skills/viet-nguyen-ban/` | `xuong-viet-nguyen-ban` | nhờ soạn bài đứng tên bạn từ chất liệu thật; gửi bản chốt để trợ lý học giọng |
| `skills/kiem-chung/` | `xuong-viet-kiem-chung` | bài có nguồn, con số, nhà nghiên cứu, lời trích |
| `skills/factual-review/` | `xuong-viet-factual-review` | rà lập luận và dữ kiện của một văn bản theo FACTUAL |

Tên trên tài khoản có tiền tố `xuong-viet-` để không trùng skill khác bạn đang có.

## Hai nơi skill sống

- **Trong xưởng** (`skills/` trong thư mục `xuong-viet-ai`): bản gốc, luôn mới nhất, đi cùng công cụ và chuẩn của xưởng. Khi bạn mở thư mục làm việc trong ứng dụng AI, trợ lý đọc thẳng bản này. Chỉ dùng xưởng trong thư mục đó thì không cần làm gì thêm.
- **Trên tài khoản AI của bạn**: bản đóng gói từ bản gốc, mang khối "Đã thiết lập" (tên bạn, cách trợ lý gọi bạn, thư mục làm việc, nơi để kho tư liệu) và bản chụp giọng văn của bạn. Lợi ích:
  - trợ lý tự nhận ra việc viết ở **mọi cuộc trò chuyện**, kể cả khi bạn quên mở thư mục, và nhắc bạn gắn thư mục để dùng kho tư liệu;
  - đang ở điện thoại, chưa gắn được thư mục, trợ lý vẫn hỏi, soạn, soi đúng giọng bạn nhờ bản chụp (chỉ chưa đọc được kho và chưa chạy được công cụ);
  - mọi cuộc trò chuyện dùng cùng một cách làm, không lệch nhau.

Gói skill **không chứa tư liệu nào trong kho** của bạn. Gói chụp ba tệp riêng: giọng văn (mọi gói), bài học giọng (gói viết nguyên bản), hồ sơ người viết (gói tập viết); muốn chỉ mang giọng văn thì nhờ trợ lý đóng gói với `--chi-giong-van`. Bản trên tài khoản là bản chụp lúc đóng gói: đổi giọng văn hay cập nhật xưởng thì đóng gói lại và thay bản cũ.

## Gói skill của bạn có gì

Trợ lý tạo gói bằng lệnh `python3 tools/dong-goi-skill.py`, ghi vào `Bai viet/_skill/` (ngoài xưởng): mỗi skill một tệp `.zip` để tải lên, kèm một thư mục cùng tên để bạn mở ra xem.

```
xuong-viet-tap-viet.zip
└── xuong-viet-tap-viet/
    ├── SKILL.md             cách làm việc; dưới mục "Cấu hình cá nhân" là khối "Đã thiết lập" của bạn
    └── references/          tài liệu đi kèm
        ├── GIONG-VAN.md     bản chụp giọng văn của bạn
        ├── DONG-GOI.md      ngày đóng gói, tệp đã chụp, dấu gói
        └── ...
```

Dấu gói là một chuỗi ký tự máy tính ra từ nội dung gói, giúp biết bản trên tài khoản có đúng bản mới nhất không. Mô tả trong gói được rút gọn còn dưới 200 ký tự vì Claude giới hạn độ dài mô tả của skill tải lên.

## Lưu vào tài khoản: từng bước

Giao diện các ứng dụng AI đổi thường xuyên. Các bước dưới đây theo trang trợ giúp chính thức, kiểm ngày 26/10/2026; trợ lý kiểm lại trang trợ giúp hiện hành trước khi dẫn bạn, và dẫn theo đúng chữ trên màn hình bạn đang thấy.

### Claude (ứng dụng trên máy tính, trang web claude.ai)

1. **Bật tính năng cần thiết (một lần).** Mở cài đặt [Settings] > tính năng [Capabilities], bật công tắc chạy mã và tạo tệp [Code execution and file creation]. Skills có ở các gói Pro, Max, Team và Enterprise; với Enterprise, người quản trị tổ chức bật trước.
2. **Mở trang skill.** Vào tùy chỉnh [Customize] > skill [Skills] (claude.ai/customize/skills); một số tài khoản thấy mục skill ngay trong cài đặt tính năng [Capabilities].
3. **Tải gói lên.** Bấm nút tải skill lên [Upload skill] (có tài khoản là nút "+" rồi chọn tạo skill bằng cách tải tệp lên), chọn một tệp `.zip` trong `Bai viet/_skill/`, mỗi lần một tệp. Không giải nén trước. Dấu hiệu xong: skill hiện trong danh sách với công tắc đang bật.
4. **Lặp lại** cho các gói còn lại.

Nguồn: [Use skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude), [How to create custom skills](https://support.claude.com/en/articles/12512198).

### Claude Code

Claude Code đọc skill từ thư mục skill của nó (gõ `/skills` để xem skill đang có). Trợ lý tra tài liệu hiện hành của Claude Code xem skill trên tài khoản claude.ai có được đồng bộ sang không; không thấy thì chép thư mục skill trong `Bai viet/_skill/` vào thư mục skill của Claude Code theo tài liệu ấy, và có thể đóng gói với `--mo-ta-day-du` để giữ mô tả đầy đủ.

### ChatGPT, Gemini và trợ lý khác

Nền tảng có tính năng skill theo chuẩn mở Agent Skills thì tải gói theo trang trợ giúp của nền tảng ấy; trợ lý tra trang đó trước khi dẫn bạn. Chưa có thì không sao: khi bạn mở thư mục làm việc trong ứng dụng làm việc được với thư mục (ChatGPT desktop chế độ Codex, Antigravity...), trợ lý đọc thẳng `skills/` trong xưởng. Chỉ dùng khung chat thì dùng gói chung theo `BAT-DAU.md` của bản vẽ, mục "Đường nhẹ".

## Thử xem skill đã chạy chưa

Mở một cuộc trò chuyện mới, chưa gắn thư mục, nói: "Tôi đang có một ý về chuyện học trò sợ hỏi, nghĩ cùng tôi." Skill chạy đúng thì trợ lý gọi bạn đúng cách bạn đã chọn, không viết gì thay bạn mà hỏi bạn về một lần cụ thể bạn thấy chuyện ấy, và nhắc gắn thư mục làm việc nếu muốn dùng kho tư liệu.

## Khi nào đóng gói lại và thay bản cũ

Nói với trợ lý "đóng gói lại skill" khi: vừa đổi giọng văn (tên, xưng hô, vai, quy ước, từ của bạn), vừa cập nhật xưởng mà trợ lý báo skill đã đổi, hoặc chuyển thư mục làm việc sang chỗ khác. Thay bản trên Claude: tắt công tắc skill cũ, bấm "..." cạnh công tắc, chọn xóa, rồi tải gói mới lên như bước 3.

## An toàn

- Skill là chỉ dẫn cho trợ lý: chỉ cài skill từ nguồn bạn tin. Gói của xưởng do chính trợ lý của bạn tạo trên máy bạn, từ tệp bạn xem được.
- Không đưa mật khẩu, khóa truy cập, thông tin cá nhân của người khác vào giọng văn hay skill. Công cụ đóng gói dừng lại nếu thấy dấu hiệu khóa hay mật khẩu.
- Skill trên tài khoản đi theo tài khoản của bạn: muốn ngừng dùng thì tắt hoặc xóa trong trang Skills.

## Gỡ rối

| Bạn thấy | Thường do | Làm gì |
|---|---|---|
| Tải lên báo lỗi về mô tả [description] | mô tả quá 200 ký tự (gói đóng bằng `--mo-ta-day-du`) | nhờ trợ lý đóng gói lại không có `--mo-ta-day-du` |
| Báo trùng tên skill | bản cũ còn trên tài khoản | xóa bản cũ rồi tải lại |
| Không thấy mục Skills, không có nút tải lên | chưa bật "Code execution and file creation", gói tài khoản chưa có Skills, hoặc tổ chức đã tắt | xem bước 1 |
| Skill có trên tài khoản nhưng trợ lý không dùng | công tắc đang tắt, hoặc câu nói chưa khớp mô tả | bật công tắc; nói rõ hơn, ví dụ "dùng skill xuong-viet-tap-viet" |
| Trợ lý gọi sai tên, sai xưng hô | gói đóng trước khi đổi giọng văn | đổi trong xưởng, đóng gói lại, thay bản cũ |
| Hai skill cùng việc chạy lẫn nhau | đã tải cả gói chung lẫn gói riêng, hoặc trùng skill viết khác | giữ một bản, tắt bản kia |

## Dành cho trợ lý AI khi hướng dẫn phần này

- Giải thích skill bằng lời thường trong bốn đến sáu câu (đoạn đầu tệp này là chất liệu), rồi hỏi người dùng có muốn lưu vào tài khoản không. Không muốn thì tôn trọng: xưởng vẫn chạy đủ khi mở thư mục.
- Dẫn từng bước một, đúng chữ trên màn hình, chờ xác nhận; người dùng tự bấm tải lên và tự chọn tệp.
- Trước khi dẫn, kiểm trang trợ giúp hiện hành của nền tảng khi có công cụ tìm kiếm; khác với tài liệu này thì dẫn theo trang hiện hành.
- Xong thì cùng người dùng thử một câu, rồi ghi dấu: `python3 tools/cai-dat.py --danh-dau skill`.

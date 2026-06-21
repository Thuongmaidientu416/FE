# PHẦN 2. XÂY DỰNG VÀ THIẾT KẾ WEBSITE

> **Ghi chú khi chèn hình:** Toàn bộ ảnh chụp màn hình nên lưu trong thư mục `docs/report-images/` (đã tạo sẵn), đặt tên đúng theo gợi ý dưới mỗi vị trí để dễ tra. Cách chụp: chạy `npm run dev` ở thư mục gốc, mở trình duyệt ở địa chỉ localhost, dùng Snipping Tool/Win+Shift+S để cắt đúng khung nội dung (không cần lấy thanh địa chỉ trình duyệt), độ phân giải trình duyệt nên để khoảng 1440px chiều rộng cho ảnh nét. Cú pháp chèn ảnh trong Word/Markdown:
> `![Mô tả](docs/report-images/ten-anh.png)`

## 2.1. Mục tiêu xây dựng website

Website WanderHUB được xây dựng để biến một dịch vụ vốn vô hình — thiết kế và điều phối lịch trình trải nghiệm đô thị — thành một sản phẩm số có thể giao dịch trực tuyến trọn vẹn, từ lúc khách tìm hiểu đến lúc thanh toán và sử dụng dịch vụ, mà không cần qua bước nhắn tin chờ tư vấn như cách vận hành phổ biến của các đơn vị tour custom hiện nay. Website hướng đến năm mục tiêu cụ thể:

**Thứ nhất, số hóa sản phẩm dịch vụ thành một "món hàng" có đầy đủ thành phần thương mại.** Vì WanderHUB không bán hàng hóa vật lý, website phải biến lịch trình do AI tạo ra thành sản phẩm có tên gọi, mô tả, hình ảnh, mức giá và nút hành động mua/đăng ký rõ ràng, giống cách một sản phẩm e-commerce chuẩn được trình bày.

**Thứ hai, thay thế quy trình tư vấn thủ công bằng AI tự động, rút ngắn thời gian ra quyết định của khách.** Khách chỉ cần nhập mood, ngân sách, khu vực và thời gian rảnh, hệ thống sẽ trả về một lịch trình hoàn chỉnh trong vài giây, thay vì phải chờ nhân viên phản hồi qua tin nhắn.

**Thứ ba, vận hành đồng thời mô hình freemium ba gói (Free/Basic – Premium – International Tourist) để vừa thu hút người dùng mới, vừa tạo doanh thu định kỳ.** Website là nơi duy nhất khách có thể xem, so sánh, đăng ký và thanh toán các gói này, do đó cũng chính là điểm chốt doanh thu của toàn bộ mô hình kinh doanh.

**Thứ tư, đóng vai trò điểm đến cuối cho mọi kênh truyền thông.** Mọi nội dung quảng bá trên mạng xã hội đều cần một nơi để "đổ" traffic về, chuyển đổi thành tài khoản đăng ký và sau đó thành giao dịch trả phí — website chính là điểm hội tụ đó.

**Thứ năm, tạo cảm giác an toàn và đáng tin cậy cho khách hàng, đặc biệt là khách quốc tế lần đầu đến TP.HCM.** Giao diện, nội dung và quy trình thanh toán cần minh bạch, có bằng chứng cụ thể (điểm số AI, mô tả chi tiết, thông tin chuyển khoản rõ ràng) để giảm tâm lý lo lắng khi sử dụng một dịch vụ mới và đặt niềm tin vào một nền tảng chưa có thương hiệu lâu năm.

![Toàn cảnh trang chủ WanderHUB — hero section thể hiện định vị thương hiệu](docs/report-images/01-homepage-hero.png)
*Hình 2.1: Trang chủ website — nơi truyền tải mục tiêu định vị thương hiệu và CTA dẫn vào dịch vụ.*
> Chụp: mở `/` (trang chủ), cuộn để lấy trọn phần hero (tiêu đề lớn + 2 nút CTA "Lên lịch trình ngay" / "Xem Trải Nghiệm Đô Thị" + thẻ "AI ITINERARY RECOMMENDED" góc phải).

## 2.2. Cấu trúc website

Website được xây dựng dưới dạng một nền tảng web hiện đại, phản hồi nhanh và không cần tải lại trang khi chuyển đổi giữa các mục — toàn bộ thao tác từ xem thông tin, đăng ký, tạo lịch trình đến thanh toán diễn ra liền mạch trong một trải nghiệm duy nhất, không bị gián đoạn hay chờ tải giữa các bước. Dữ liệu người dùng, đối tác cung cấp dịch vụ và lịch sử lịch trình được quản lý tập trung để phục vụ cá nhân hóa và chăm sóc khách hàng về sau. Cấu trúc menu chính trên thanh điều hướng được sắp xếp theo đúng hành trình nhận biết – tìm hiểu – giao dịch của khách hàng:

| Menu | Đường dẫn | Vai trò trong cấu trúc |
|---|---|---|
| Trang chủ | `/` | Giới thiệu tổng quan, hero section, lý do chọn dịch vụ, dẫn vào công cụ lập lịch trình |
| Về chúng tôi | `/about` | Câu chuyện thương hiệu, cách AI kết hợp am hiểu địa phương |
| Gói dịch vụ | `/pricing` | Bảng so sánh ba gói dịch vụ và cổng thanh toán |
| Khám phá | `/explore` | Nội dung dạng blog/POV theo từng "vibe", hỗ trợ nuôi dưỡng khách trước khi mua |
| Liên hệ | `/contact` | Form gửi yêu cầu hỗ trợ |
| Đăng nhập/Đăng ký | `/auth` | Cổng xác thực, điều kiện bắt buộc trước khi vào công cụ lập lịch trình |
| Lên lịch trình | `/planner` | Trang lõi — nơi diễn ra giao dịch dịch vụ chính: AI tạo route, đặt xe, theo dõi hành trình |
| FAQ, Điều khoản | `/faq`, `/terms` | Trang hỗ trợ, tăng độ tin cậy và minh bạch pháp lý |

![Sơ đồ cấu trúc website WanderHUB](docs/report-images/02-sitemap.png)
*Hình 2.2: Sơ đồ cấu trúc (sitemap) website theo 3 lớp Khám phá – Giao dịch – Hỗ trợ.*
> Đây là hình **bạn cần tự vẽ** (không chụp màn hình), dùng PowerPoint/Canva/draw.io: vẽ 3 khối lớn "Lớp khám phá / Lớp giao dịch / Lớp hỗ trợ", mỗi khối liệt kê các trang tương ứng trong bảng trên, có mũi tên nối từ Trang chủ → Pricing/Planner → Payment để thể hiện luồng điều hướng.

![Thanh điều hướng (Navbar) của website](docs/report-images/03-navbar.png)
*Hình 2.3: Thanh điều hướng chính, thể hiện đầy đủ các mục menu.*
> Chụp: phần header cố định trên cùng của bất kỳ trang nào (logo WanderHUB bên trái, menu Trang chủ/Về WanderHUB/Gói dịch vụ/Khám phá/Liên hệ, nút Đăng nhập bên phải).

Toàn bộ cấu trúc có thể nhóm thành ba lớp chức năng rõ rệt:

- **Lớp khám phá:** Trang chủ, Về chúng tôi, Khám phá — phục vụ khách đang tìm hiểu, xây dựng niềm tin và truyền tải giọng điệu thương hiệu gần gũi, am hiểu thành phố.
- **Lớp giao dịch:** Gói dịch vụ, Đăng nhập/Đăng ký, Lên lịch trình, cổng thanh toán — đây là lớp e-commerce thực sự, nơi khách chọn gói, tạo tài khoản, nhập nhu cầu, nhận lịch trình, đặt xe và thanh toán.
- **Lớp hỗ trợ:** Liên hệ, FAQ, Điều khoản, và một trợ lý chat AI nổi xuất hiện trên mọi trang — duy trì trải nghiệm hậu mãi và giải đáp thắc mắc theo thời gian thực.

Ba lớp này được kết nối liền mạch bằng các nút kêu gọi hành động lặp lại nhất quán trên mọi trang ("Lên lịch trình ngay", "Bắt đầu Premium"), giúp khách không bao giờ "lạc" trong cấu trúc mà luôn có một lối đi rõ ràng để tiến tới giao dịch.

Hai thành phần cố định xuất hiện trên mọi trang là **Header** và **Footer**. Header (đã thể hiện ở Hình 2.3) gồm logo thương hiệu, menu điều hướng chính và nút đăng nhập/CTA — không có biểu tượng giỏ hàng hay thanh tìm kiếm sản phẩm như các website thương mại điện tử bán lẻ thông thường, vì WanderHUB bán dịch vụ theo yêu cầu (make-to-order) chứ không bán danh mục hàng hóa có sẵn để khách tự tìm và bỏ vào giỏ. Footer gồm ba khối thông tin: giới thiệu ngắn về thương hiệu kèm logo, thông tin liên hệ (địa chỉ, hotline, fanpage), và nhóm liên kết hỗ trợ (FAQ, Điều khoản, Đăng nhập/Đăng ký, lối tắt vào công cụ lập lịch trình) — đóng vai trò là một "bản đồ thu nhỏ" của toàn bộ website, giúp khách luôn có lối thoát quay về các trang quan trọng dù đang ở bất kỳ đâu.

![Footer của website WanderHUB](docs/report-images/17-footer.png)
*Hình 2.17: Footer — khối thương hiệu, thông tin liên hệ và liên kết hỗ trợ.*
> Chụp: cuộn xuống cuối bất kỳ trang nào, lấy trọn phần footer.

## 2.3. Nội dung và hình ảnh sản phẩm/dịch vụ trên website

Vì sản phẩm là dịch vụ vô hình, nội dung trên website được xây dựng để "vật chất hóa" trải nghiệm — biến những khái niệm trừu tượng như "AI gợi ý lịch trình" thành hình ảnh, câu chữ và số liệu cụ thể mà khách có thể nhìn thấy và tin tưởng ngay từ lần ghé đầu tiên.

**Tại trang chủ:** Hero section sử dụng hiệu ứng chuyển động (cảnh xe chạy qua thành phố, lớp phủ tuyến đường mô phỏng) tái hiện một hành trình thực tế qua các địa danh quen thuộc của TP.HCM như Landmark 81 hay khu vực ven sông Sài Gòn, kèm một thẻ minh họa trực tiếp đầu ra của AI (ví dụ route "Q1 Urban Vibe": cà phê phố Nguyễn Huệ → hải sản kiểu Ốc Đào Q1 → check-in Landmark 81). Cách trình bày này không bán "một tour" mà bán "một câu chuyện hành trình". Tiếp theo là phần "Ba bước – Một hành trình" minh họa lại quy trình sử dụng dịch vụ bằng hình ảnh số (chọn mood & vibe → AI dựng lịch trình → lên đường), giúp khách hình dung quy trình mua hàng trước khi thực sự thao tác.

![Thẻ "AI Itinerary Recommended" trên trang chủ](docs/report-images/04-ai-itinerary-card.png)
*Hình 2.4: Thẻ minh họa đầu ra AI ngay tại hero — route mẫu "Q1 Urban Vibe".*
> Chụp cận khung thẻ nổi bên phải hero (góc trên ghi "AI ITINERARY RECOMMENDED", có 3 dòng Cafe/Ốc Đào/Landmark 81).

![Phần "Ba bước – Một hành trình"](docs/report-images/05-three-steps.png)
*Hình 2.5: Ba bước sử dụng dịch vụ được trực quan hóa bằng icon và số thứ tự 01–02–03.*
> Chụp: cuộn xuống section "Nền tảng WanderHUB / Ba bước – Một hành trình" (3 cột: Chọn mood & vibe / AI dựng lịch trình / Lên đường thôi!).

**Tại trang Gói dịch vụ:** Mỗi gói (Basic/Free, Premium, International Tourist) được trình bày đầy đủ thành phần của một sản phẩm e-commerce chuẩn: tên gói, mức giá, mô tả ngắn định vị đối tượng phù hợp, danh sách quyền lợi được đánh dấu tích xanh, danh sách quyền lợi không bao gồm được gạch ngang để khách dễ so sánh, một nhãn nổi bật ("Best vibe") đặt ở gói được ưu tiên bán, và nút hành động thay đổi theo ngữ cảnh sử dụng ("Dùng miễn phí", "Bắt đầu Premium", hoặc "Đang sử dụng" nếu gói đó đang active trên tài khoản). Việc trình bày song hành quyền lợi có/không có theo từng gói giúp khách ra quyết định nhanh, không cần hỏi thêm.

![Bảng 3 gói dịch vụ tại trang Pricing](docs/report-images/06-pricing-cards.png)
*Hình 2.6: Ba thẻ gói dịch vụ Basic – Premium – International Tourist, có nhãn "Best vibe" ở gói Premium.*
> Chụp: toàn bộ trang `/pricing`, lấy đủ 3 card cạnh nhau, thấy rõ tích xanh/gạch ngang và nút bấm dưới mỗi card.

**Tại trang Lên lịch trình (sản phẩm lõi):** Mỗi điểm đến trong lịch trình được hiển thị như một thẻ sản phẩm con, gồm hình ảnh thực địa, tên địa điểm, mô tả ngắn mang giọng văn cá nhân hóa (ví dụ: "Rooftop có không khí riêng tư, hợp hẹn hò hoặc nhóm nhỏ"), khung giờ dự kiến, danh mục (cà phê/ẩm thực/về đêm/văn hóa…), điểm phù hợp do AI tính toán, chi phí ước tính theo VNĐ và thời lượng dự kiến. Toàn bộ nội dung này được sinh từ engine gợi ý dựa trên dữ liệu đối tác thật trong cơ sở dữ liệu — không phải nội dung tĩnh viết sẵn — nên luôn gắn với thông tin có thật, tránh tình trạng AI tạo ra thông tin sai lệch hoặc không tồn tại.

![Thẻ điểm dừng (route stop) trong kết quả lịch trình AI](docs/report-images/07-route-stop-card.png)
*Hình 2.7: Một điểm dừng trong lịch trình — đầy đủ ảnh, mô tả, điểm AI, chi phí, thời lượng.*
> Chụp: sau khi tạo lịch trình tại `/planner`, lấy cận 1–2 thẻ kết quả (ví dụ "Secret Garden Rooftop" hoặc "Nhà Hàng Royal Saigon") thấy rõ ảnh + điểm số + giá.

**Tại trang Khám phá:** Nội dung dạng blog/POV theo từng vibe (foodie, healing, check-in…) đóng vai trò nuôi dưỡng khách hàng trước khi họ chuyển đổi sang dùng dịch vụ, đồng thời tạo cảm giác quen thuộc cho những khách đến từ mạng xã hội — họ sẽ thấy phong cách nội dung tương đồng khi chuyển từ fanpage sang website, không bị "đứt mạch" trải nghiệm.

![Trang Khám phá (Explore) dạng lưới bài viết POV](docs/report-images/08-explore-grid.png)
*Hình 2.8: Lưới bài viết Explore theo từng vibe, mỗi bài có ảnh đại diện và nút "Đọc POV".*
> Chụp: trang `/explore`, lấy 3–6 card bài viết hiển thị dạng lưới.

**Hình ảnh sản phẩm** được lựa chọn theo logic phân loại theo từng danh mục (có ảnh dự phòng riêng cho nhóm ẩm thực, cà phê, về đêm, văn hóa, vui chơi…), để bất kỳ điểm đến nào — kể cả khi dữ liệu đối tác chưa có ảnh thật — vẫn hiển thị hình ảnh đúng ngữ cảnh, giữ tính chuyên nghiệp và đồng bộ với phong cách thẩm mỹ hiện đại, mang hơi hướng hospitality cao cấp mà thương hiệu định vị.

## 2.4. Chức năng hỗ trợ giao dịch

Website tích hợp đầy đủ các chức năng cần thiết của một nền tảng thương mại điện tử dịch vụ:

**(1) Xác thực và quản lý tài khoản.** Khách đăng ký/đăng nhập bằng email và mật khẩu; mật khẩu được mã hóa và lưu trữ an toàn theo chuẩn bảo mật phổ biến, phiên đăng nhập có thời hạn và tự động yêu cầu đăng nhập lại khi hết hạn. Đây là lớp bảo mật tối thiểu bắt buộc đối với một nền tảng có phát sinh thanh toán, giúp khách an tâm rằng tài khoản và lịch sử giao dịch của họ được bảo vệ.

![Trang Đăng nhập/Đăng ký](docs/report-images/09-auth-form.png)
*Hình 2.9: Form Đăng nhập/Đăng ký tài khoản.*
> Chụp: trang `/auth`, có thể chụp cả 2 tab (đăng nhập và đăng ký) ghép cạnh nhau hoặc chọn 1 trong 2.

**(2) Công cụ tạo lịch trình bằng AI.** Khách nhập năm nhóm tiêu chí: mood/vibe (chill, hẹn hò, nhóm bạn, foodie, về đêm, văn hóa, check-in, hidden gem, healing…), mức ngân sách (ba mức: tiết kiệm/vừa đẹp/thoải mái), khung giờ, khu vực (quận) và sở thích trải nghiệm cụ thể. Từ các tiêu chí này, AI phân tích và so khớp với toàn bộ đối tác phù hợp đang có trong dữ liệu của nền tảng để chọn ra những điểm đến sát nhu cầu nhất, rồi sắp xếp lại theo trình tự thời gian hợp lý cho một hành trình hoàn chỉnh. Vì gợi ý luôn được chọn từ danh sách đối tác thật — không phải do AI tự "bịa" ra — nội dung lịch trình trả về vừa cá nhân hóa, vừa đảm bảo độ chính xác và tin cậy cho khách hàng.

![Form nhập nhu cầu tại trang Lên lịch trình](docs/report-images/10-planner-form.png)
*Hình 2.10: Form chọn mood, ngân sách, khung giờ, khu vực, sở thích và phương tiện di chuyển.*
> Chụp: trang `/planner` trước khi bấm tạo lịch trình — thấy rõ các nhóm lựa chọn (chip mood, segmented budget/time, district grid, transport row).

**(3) Giới hạn sử dụng theo gói, gắn với mô hình freemium.** Người dùng gói Free/Basic bị giới hạn số lần tạo lịch trình trong một khoảng thời gian nhất định (được đếm cả ở phía hệ thống khi đã đăng nhập và phía thiết bị khi chưa đăng nhập); khi đạt hạn mức, hệ thống sẽ tự động điều hướng khách sang trang Gói dịch vụ. Đây là cơ chế kỹ thuật cụ thể hóa vai trò của gói miễn phí: dùng để trải nghiệm thử, sau đó khuyến khích chuyển đổi sang gói trả phí.

**(4) Theo dõi tương tác hành vi.** Mọi hành động của khách trên kết quả gợi ý (xem, di chuột qua, nhấn xem chi tiết, chọn, lưu lại, không thích, yêu cầu đổi lộ trình) đều được ghi nhận kèm trọng số tương ứng. Đây là hạ tầng dữ liệu để cải thiện chất lượng gợi ý theo thời gian, giúp nền tảng không chỉ gợi ý một lần mà có khả năng cá nhân hóa ngày càng chính xác hơn cho từng người dùng.

**(5) Chức năng đặt xe/hướng dẫn viên tích hợp.** Sau khi có lịch trình, khách có thể đặt trực tiếp xe và tài xế kiêm hướng dẫn viên của nền tảng theo quy trình hai bước: kiểm tra xe khả dụng, chọn loại xe (xe máy hoặc ô tô 7 chỗ), và xác nhận đặt. Việc nội bộ hóa dịch vụ vận chuyển giúp nền tảng chủ động kiểm soát chất lượng trải nghiệm và biên lợi nhuận, thay vì chỉ đơn thuần dẫn link sang ứng dụng gọi xe khác.

![Bảng chọn loại xe / xác nhận đặt xe](docs/report-images/11-vehicle-booking.png)
*Hình 2.11: Bảng "Chọn loại xe" hiển thị xe máy / ô tô 7 chỗ sau khi bấm "Đặt xe ngay".*
> Chụp: trong kết quả lịch trình, bấm nút "Đặt xe ngay" để hệ thống chuyển sang trạng thái "selecting", chụp bảng chọn loại xe.

**(6) Theo dõi hành trình thời gian thực.** Một bản đồ tương tác hiển thị các điểm dừng được nối bằng tuyến đường di chuyển, kèm danh sách trạng thái từng điểm ("đang đến/tiếp theo/đang chờ"), giúp khách luôn biết mình đang ở đâu trong hành trình và bước tiếp theo là gì — giải quyết trực tiếp tâm lý lo lắng về định hướng của khách lần đầu đến một thành phố lạ.

![Journey Tracker — bản đồ và timeline hành trình](docs/report-images/12-journey-tracker.png)
*Hình 2.12: Bản đồ Leaflet hiển thị các điểm dừng nối bằng tuyến đường, kèm timeline trạng thái bên phải.*
> Chụp: sau khi đặt xe/bắt đầu hành trình, lấy trọn khung 2 cột — bản đồ bên trái (có pin số 1,2,3 và đường nối) và timeline bên phải.

**(7) Cổng thanh toán bằng mã QR.** Khi chọn gói trả phí, hệ thống hiển thị một cửa sổ thanh toán có mã QR sinh động riêng cho từng gói và mã giao dịch tham chiếu, kèm đầy đủ thông tin chuyển khoản (ngân hàng, số tài khoản, số tiền, nội dung chuyển khoản có gắn mã đối soát). Sau khi khách xác nhận đã thanh toán, hệ thống chuyển qua trạng thái "đang xác minh" rồi "thành công" trước khi kích hoạt gói dịch vụ trên tài khoản — mô phỏng đúng luồng thanh toán chuyển khoản ngân hàng phổ biến tại Việt Nam.

![Cửa sổ thanh toán QR](docs/report-images/13-payment-modal.png)
*Hình 2.13: Modal thanh toán — mã QR bên phải, danh sách quyền lợi bên trái, thông tin chuyển khoản phía dưới.*
> Chụp: tại `/pricing`, chọn gói trả phí (Premium hoặc International Tourist) để mở modal thanh toán, chụp toàn bộ modal ở trạng thái "qr" (trước khi bấm xác nhận).

**(8) Trợ lý ảo dạng chat.** Một cửa sổ chat nổi xuất hiện cố định trên mọi trang, sử dụng mô hình ngôn ngữ lớn để trả lời câu hỏi của khách theo thời gian thực, đóng vai trò hỗ trợ liên tục và giảm tải cho việc tư vấn thủ công.

![Cửa sổ Floating Chatbot đang mở](docs/report-images/14-chatbot.png)
*Hình 2.14: Khung chat AI nổi ở góc màn hình, đang hiển thị hội thoại mẫu.*
> Chụp: bấm icon chat nổi ở góc dưới phải bất kỳ trang nào, gửi thử 1 câu hỏi rồi chụp cả khung chat.

**(9) Form liên hệ và hỗ trợ.** Trang Liên hệ cho phép khách gửi yêu cầu hỗ trợ trực tiếp đến hệ thống, bổ trợ cho những trường hợp nằm ngoài khả năng xử lý của chatbot.

![Trang Liên hệ](docs/report-images/15-contact-form.png)
*Hình 2.15: Form liên hệ với các trường tên, email, chủ đề, nội dung.*
> Chụp: trang `/contact`, lấy trọn form.

## 2.5. Quy trình giao dịch trên website

Quy trình giao dịch trên website được thiết kế thành một luồng liền mạch duy nhất, gồm mười bước:

**Bước 1 — Tiếp cận và nhận biết nhu cầu.** Khách đến website từ hai nguồn chính: trực tiếp qua tìm kiếm hoặc giới thiệu (vào trang chủ để tìm hiểu mô hình), hoặc từ các kênh truyền thông xã hội theo lời kêu gọi hành động dẫn thẳng vào trang Gói dịch vụ hoặc trang Lên lịch trình.

**Bước 2 — Xác thực tài khoản.** Hệ thống yêu cầu đăng nhập hoặc đăng ký trước khi cho phép vào công cụ lập lịch trình hoặc chọn gói trả phí. Việc bắt buộc có tài khoản giúp gắn lịch sử sử dụng, hạn mức gói miễn phí và dữ liệu hành vi vào đúng một người dùng — nền tảng cần thiết để cá nhân hóa về lâu dài.

**Bước 3 — Chọn gói dịch vụ.** Tại trang Gói dịch vụ, khách so sánh ba gói và chọn. Nếu chọn gói miễn phí, hệ thống lưu lựa chọn ngay và chuyển khách vào trang lập lịch trình. Nếu chọn gói trả phí, hệ thống mở cửa sổ thanh toán.

**Bước 4 — Thanh toán.** Khách quét mã QR hoặc chuyển khoản theo thông tin hiển thị, sau đó bấm xác nhận đã thanh toán. Hệ thống chuyển trạng thái từ "đang xác minh" sang "thành công", ghi nhận gói mới cho tài khoản và đồng thời lưu lại trên thiết bị để hiển thị ngay nhãn "gói đang dùng" trên giao diện.

**Bước 5 — Nhập nhu cầu trải nghiệm.** Tại công cụ lập lịch trình, khách thiết lập các tham số: mood/vibe, khu vực, ngân sách, khung giờ, sở thích cụ thể và phương tiện di chuyển mong muốn. Hệ thống kiểm tra hạn mức sử dụng theo gói trước khi cho phép tạo lịch trình mới; nếu gói miễn phí đã hết lượt trong kỳ, khách được điều hướng quay lại trang Gói dịch vụ.

**Bước 6 — AI xử lý và trả kết quả.** Yêu cầu được gửi đến hệ thống xử lý, nơi nhu cầu của khách được đối chiếu với toàn bộ đối tác phù hợp khu vực/ngân sách để chọn ra danh sách điểm dừng tối ưu kèm điểm số phù hợp, sắp xếp theo trình tự thời gian hợp lý và tổng hợp chi phí, thời lượng toàn tuyến. Trong lúc xử lý, giao diện hiển thị trạng thái "đang tính toán" để khách hiểu hệ thống đang làm việc.

**Bước 7 — Khách xem, tương tác và tinh chỉnh lịch trình.** Khách xem từng điểm dừng với đầy đủ hình ảnh, mô tả, điểm phù hợp và chi phí; có thể nhấn xem chi tiết hoặc yêu cầu đổi lộ trình — mọi tương tác được ghi nhận để cải thiện gợi ý về sau. Hệ thống cũng hiển thị thêm một số gợi ý từ đối tác thương mại, được tách biệt rõ ràng khỏi kết quả do AI chọn, để khách luôn phân biệt được đâu là gợi ý dựa trên nhu cầu thực và đâu là nội dung được ưu tiên hiển thị có trả phí.

**Bước 8 — Đặt phương tiện di chuyển.** Nếu chọn hình thức có hướng dẫn viên đi kèm, khách bấm đặt xe ngay, hệ thống kiểm tra xe khả dụng trong đội xe của nền tảng, khách chọn loại xe và xác nhận đặt, sau đó nhận thông tin tài xế được phân công. Nếu chọn đi bộ hoặc tự lái, hệ thống chỉ hiển thị ghi chú hướng dẫn bắt đầu hành trình.

**Bước 9 — Theo dõi hành trình.** Bản đồ và danh sách trạng thái cập nhật theo thời gian thực trong lúc khách di chuyển, giúp khách luôn biết đang ở đâu, điểm tiếp theo là gì và còn bao lâu nữa.

**Bước 10 — Sử dụng dịch vụ và hậu mãi.** Trong và sau khi trải nghiệm, khách có thể dùng trợ lý chat hoặc form liên hệ nếu gặp sự cố; với gói trả phí, lượt sử dụng được hệ thống tự cập nhật để khách theo dõi hạn mức của chu kỳ hiện tại. Hành vi lưu lịch trình và tương tác với từng điểm đến tiếp tục được ghi nhận, khép lại một vòng dữ liệu để làm đầu vào cho lần gợi ý kế tiếp được chính xác hơn.

![Sơ đồ quy trình giao dịch 10 bước](docs/report-images/16-flow-diagram.png)
*Hình 2.16: Sơ đồ tổng hợp quy trình giao dịch trên website WanderHUB.*
> Đây là hình **bạn tự vẽ** (PowerPoint/Canva), dạng sơ đồ khối nối tiếp 10 ô vuông tương ứng 10 bước đã trình bày, có thể nhóm 3 màu theo 3 giai đoạn: Tiếp cận–Xác thực (xanh), Chọn gói–Thanh toán (vàng), Sử dụng dịch vụ–Hậu mãi (xanh đậm) để trực quan và dễ chấm điểm.

Nhìn chung, mười bước trên cho thấy website không chỉ là một trang giới thiệu dịch vụ, mà là một hệ thống giao dịch hoàn chỉnh và khép kín — từ tiếp cận, xác thực, chọn gói, thanh toán, đến tạo và vận hành sản phẩm dịch vụ lõi, cùng với cơ chế hậu mãi và cải thiện liên tục dựa trên dữ liệu hành vi thực tế của khách hàng.

## 2.6. Bản đồ Pain Point – Giải pháp (Pain Point Mapping)

Để chứng minh website không chỉ "có chức năng" mà từng chức năng đều giải quyết một nỗi đau cụ thể của khách hàng mục tiêu, bảng dưới đây ánh xạ trực tiếp từng pain point đã nhận diện sang tính năng tương ứng trên website:

| Pain point của khách hàng | Biểu hiện cụ thể | Tính năng WanderHUB giải quyết | Vị trí trên website |
|---|---|---|---|
| Mất nhiều thời gian tự lên kế hoạch | Lưu hàng chục địa điểm từ TikTok/Google Maps nhưng không biết sắp xếp thành lịch trình | AI tạo lịch trình hoàn chỉnh trong vài giây từ 5 tiêu chí đầu vào | Trang Lên lịch trình (`/planner`) |
| Lịch trình không đúng sở thích cá nhân (tour đại trà) | Tour có sẵn trên Klook/KKday giống nhau cho mọi khách | Lựa chọn mood/vibe cá nhân hóa (chill, hẹn hò, foodie, nightlife, văn hóa, hidden gem…) làm đầu vào cho AI | Form chọn mood trong Planner |
| Sợ rủi ro, không biết chỗ nào đáng tin khi đến nơi lạ | Lo chọn nhầm quán, review không đúng thực tế | Mỗi điểm dừng có điểm AI (0–100), mô tả, ảnh thật và chi phí cụ thể — dữ liệu lấy từ đối tác thật, không phải AI tự sinh | Thẻ điểm dừng trong kết quả lịch trình |
| Khó di chuyển, sợ kẹt xe/lạc đường, đặc biệt khách quốc tế | TP.HCM đông xe, khách không quen khu vực, phải tự đặt xe nhiều chặng | Đặt xe/Tour Guide tích hợp + bản đồ theo dõi hành trình thời gian thực | Vehicle booking + Journey Tracker |
| Phải nhắn tin chờ tư vấn thủ công với local tour | Mất thời gian chờ phản hồi, chất lượng phụ thuộc kinh nghiệm người tư vấn | AI tự động phản hồi ngay + trợ lý chat AI hỗ trợ 24/7 thay tư vấn viên | Planner + Floating Chatbot |
| Không biết nên chọn gói nào, sợ tốn tiền oan | Nhiều nền tảng không rõ giá trị từng mức giá | Mô hình freemium minh bạch: so sánh ✓/✗ theo từng gói, dùng thử Free trước khi trả phí | Trang Gói dịch vụ (`/pricing`) |
| Lo ngại thanh toán không minh bạch, sợ lừa đảo | E ngại chuyển khoản cho một nền tảng mới, chưa có thương hiệu lâu năm | Mã QR riêng theo từng giao dịch, hiển thị đầy đủ thông tin ngân hàng và mã đối soát, có bước xác minh trước khi kích hoạt gói | Payment Modal |

Cách trình bày pain point → giải pháp → vị trí cụ thể giúp chứng minh mỗi quyết định thiết kế trên website đều bắt nguồn từ một nhu cầu thật của khách hàng mục tiêu, không phải tính năng được thêm vào tùy tiện.

## 2.7. Hành trình khách hàng trên website (Customer Journey Map)

Khác với "quy trình giao dịch 10 bước" ở mục 2.5 (mô tả luồng thao tác kỹ thuật), bản đồ hành trình khách hàng dưới đây nhìn từ góc độ cảm xúc và nhận thức của khách qua 5 giai đoạn, làm cơ sở để tối ưu trải nghiệm và giảm tỷ lệ rời bỏ ở từng điểm chạm:

| Giai đoạn | Điểm chạm (Touchpoint) | Hành động của khách | Cảm xúc / Suy nghĩ | Rủi ro rời bỏ | Giải pháp của WanderHUB |
|---|---|---|---|---|---|
| **1. Nhận biết** (Awareness) | Bài đăng Facebook, video TikTok, giới thiệu từ bạn bè | Thấy nội dung gợi ý lịch trình, click vào link dẫn về website | Tò mò nhưng còn nghi ngờ ("liệu có đúng nhu cầu của mình không?") | Rời trang nếu landing page tải chậm hoặc không khớp kỳ vọng từ nội dung social | Trang chủ tái hiện đúng nội dung đã thấy trên social (route mẫu, giọng văn nhất quán), tải nhanh nhờ kiến trúc SPA |
| **2. Tìm hiểu** (Consideration) | Trang chủ, Về WanderHUB, Khám phá, Gói dịch vụ | Đọc về mô hình AI, xem gói giá, so sánh với phương án tự đi/đặt Klook | Cân nhắc, so sánh giá trị nhận được so với chi phí và thời gian bỏ ra | Rời bỏ nếu không thấy rõ sự khác biệt so với tự lên kế hoạch miễn phí | Hero section minh họa cụ thể đầu ra AI; bảng giá có gói Free để dùng thử không rủi ro |
| **3. Quyết định** (Decision) | Trang Đăng nhập/Đăng ký, Pricing, Payment Modal | Tạo tài khoản, chọn gói, thanh toán (nếu chọn gói trả phí) | Hồi hộp khi nhập thông tin thanh toán, cần cảm giác an toàn | Rời bỏ ở bước đăng ký (friction) hoặc nghi ngờ ở bước thanh toán | Form đăng ký ngắn (3 trường), thanh toán hiển thị đầy đủ thông tin đối soát, có trạng thái xác minh rõ ràng |
| **4. Sử dụng** (Onboarding & Usage) | Planner, kết quả lịch trình, đặt xe, Journey Tracker | Nhập nhu cầu, nhận lịch trình, chọn điểm dừng, đặt xe, di chuyển theo bản đồ | Hào hứng nếu lịch trình đúng ý; lo lắng nếu sai tuyến/sai giờ khi đang di chuyển thực tế | Rời bỏ giữa luồng nếu lịch trình đầu tiên không khớp kỳ vọng, không tương tác lại lần sau | Cho phép chọn lại điểm dừng, yêu cầu đổi lộ trình (reroute); bản đồ theo dõi thời gian thực giảm lo lắng khi di chuyển |
| **5. Duy trì & Giới thiệu** (Retention & Advocacy) | Lượt sử dụng tiếp theo, trợ lý chat, trang Explore | Quay lại tạo lịch trình mới, đọc nội dung Explore, có thể chia sẻ trải nghiệm lên mạng xã hội | Hài lòng nếu gợi ý lần sau "hiểu mình hơn"; thất vọng nếu hệ thống lặp lại gợi ý cũ | Không quay lại nếu không thấy cá nhân hóa cải thiện theo thời gian | Dữ liệu tương tác (interaction tracking) làm gợi ý ngày càng sát nhu cầu; nội dung Explore giữ chân giữa các lần đặt dịch vụ |

Điểm mấu chốt của bản đồ này là chỉ ra **hai "điểm rơi" nhạy cảm nhất** trong toàn hành trình: (1) bước đăng ký/thanh toán ở giai đoạn Quyết định, và (2) trải nghiệm lần đầu với lịch trình AI ở giai đoạn Sử dụng — đây cũng là hai khu vực được phân tích sâu hơn ở mục 2.8 dưới góc độ chuyển đổi (conversion).

## 2.8. Đánh giá UX/UI và phân tích quy trình chuyển đổi (Conversion Funnel)

### Đánh giá UX/UI theo 10 nguyên tắc heuristic của Nielsen

| Nguyên tắc | Mức độ đáp ứng | Quan sát trên website |
|---|---|---|
| Hiển thị trạng thái hệ thống | Đạt | Có trạng thái "Đang tính toán...", "Đang xác minh...", trạng thái xe "loading/selecting/booked" rõ ràng theo từng bước |
| Phù hợp với thực tế người dùng | Đạt | Ngôn ngữ gần gũi ("vibe", "mood"), đơn vị tiền VNĐ, địa danh TP.HCM quen thuộc |
| Kiểm soát và tự do cho người dùng | Đạt một phần | Khách có thể đổi lựa chọn điểm dừng, yêu cầu reroute; chưa thấy nút "Quay lại bước trước" rõ ràng trong luồng Planner nhiều bước |
| Tính nhất quán và chuẩn hóa | Đạt | Nút CTA, màu sắc (xanh đậm/cam), bố cục thẻ sản phẩm lặp lại nhất quán giữa Pricing, Planner, Explore |
| Ngăn ngừa lỗi | Đạt một phần | Chưa thấy validate định dạng email hoặc độ mạnh mật khẩu phía giao diện trước khi gửi lên server |
| Nhận diện hơn là ghi nhớ | Đạt | Icon kèm nhãn chữ ở mọi lựa chọn (mood, transport, budget), không yêu cầu khách nhớ ý nghĩa icon |
| Linh hoạt và hiệu quả sử dụng | Đạt một phần | Người dùng mới và người dùng quay lại dùng cùng một luồng; chưa có cơ chế lưu mẫu lịch trình yêu thích để tạo nhanh lần sau |
| Thiết kế thẩm mỹ và tối giản | Đạt | Phong cách "premium hospitality" đồng bộ, nhiều khoảng trắng, ít chi tiết gây rối |
| Hỗ trợ nhận diện, chẩn đoán và khắc phục lỗi | Đạt một phần | Một số luồng có cơ chế dự phòng khi mất kết nối (Auth), nhưng Planner/Payment chưa thấy thông báo lỗi tường minh cho khách khi API thất bại |
| Trợ giúp và tài liệu | Đạt | Có FAQ, trang Điều khoản và chatbot AI hỗ trợ tức thời thay tài liệu tĩnh |

Kết quả: 7/10 nguyên tắc đạt mức tốt, 3/10 nguyên tắc đạt một phần — cho thấy giao diện đã đảm bảo tốt các nguyên tắc ảnh hưởng trực tiếp đến niềm tin giao dịch (trạng thái hệ thống, tính nhất quán, ngôn ngữ phù hợp người dùng), trong khi một số nguyên tắc liên quan đến kiểm soát luồng nhiều bước và xử lý lỗi vẫn còn có thể hoàn thiện thêm.

### Phân tích funnel chuyển đổi (Conversion Funnel)

| Bước trong funnel | Hành động của khách | Rủi ro rơi rụng (drop-off) |
|---|---|---|
| 1. Truy cập trang chủ | Khách xem hero, đọc giá trị cốt lõi | Rời ngay nếu không hiểu sản phẩm trong 5 giây đầu |
| 2. Vào trang Pricing/Planner | Khách xem gói hoặc thử nhập nhu cầu | Rời nếu bị yêu cầu đăng nhập ngay mà chưa thấy "giá trị" cụ thể |
| 3. Đăng ký/Đăng nhập | Tạo tài khoản | Rời nếu form dài hoặc lo ngại bảo mật |
| 4. Chọn gói dịch vụ | Chọn Free hoặc gói trả phí | Rời nếu không rõ sự khác biệt giữa các gói |
| 5. Thanh toán (nếu gói trả phí) | Quét QR, xác nhận | Rời nếu nghi ngờ độ tin cậy của giao dịch chuyển khoản |
| 6. Tạo lịch trình AI | Nhập nhu cầu, nhận kết quả | Rời nếu kết quả không khớp kỳ vọng ngay lần đầu |
| 7. Đặt xe / Hoàn tất trải nghiệm | Đặt Tour Guide hoặc tự di chuyển | Rời nếu xe hết chỗ hoặc không thấy lý do gắn bó tiếp |
| 8. Quay lại sử dụng lần sau | Tạo lịch trình mới, nâng cấp gói | Không quay lại nếu không thấy giá trị khác biệt giữa các lần dùng |

Nhìn theo toàn bộ funnel, hai điểm có rủi ro rơi rụng cao nhất là bước đăng ký/thanh toán (do liên quan trực tiếp đến thông tin cá nhân và tiền) và bước nhận kết quả lịch trình AI lần đầu (do quyết định ấn tượng đầu tiên về chất lượng cá nhân hóa) — trùng khớp với hai "điểm rơi" đã xác định ở bản đồ hành trình khách hàng (mục 2.7), qua đó củng cố rằng đây là hai khu vực cần được ưu tiên kiểm soát chất lượng trải nghiệm nhất trên toàn website.

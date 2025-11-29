# ĐỀ KIỂM TRA HTML/CSS TOÀN DIỆN (KHÔNG JAVASCRIPT)
**Môn học:** Web Basic  
**Thời gian làm bài:** 120 phút  
**Mục tiêu:** Đánh giá kiến thức từ cơ bản đến nâng cao về HTML5, CSS3, tư duy layout và khả năng ứng dụng AI trong lập trình.

---

## PHẦN 1: TRẮC NGHIỆM (4 Điểm)
*Chọn đáp án đúng nhất. Mỗi câu 0.25 điểm.*

**Câu 1 (Semantic HTML):** Thẻ nào sau đây **không** phải là thẻ Semantic trong HTML5?
A. `<article>`
B. `<div>`
C. `<nav>`
D. `<aside>`

**Câu 2 (CSS Selectors):** Selector nào có độ ưu tiên (specificity) cao nhất?
A. `.header .nav-link`
B. `#main-menu`
C. `div > p`
D. `body`

**Câu 3 (Box Model):** Nếu một phần tử có `width: 100px`, `padding: 20px`, `border: 5px`, và `box-sizing: content-box`. Tổng chiều rộng thực tế của phần tử là bao nhiêu?
A. 100px
B. 125px
C. 140px
D. 150px

**Câu 4 (Box Model):** Thuộc tính nào giúp tính `padding` và `border` vào trong kích thước `width` đã khai báo?
A. `box-sizing: border-box;`
B. `box-sizing: content-box;`
C. `box-sizing: padding-box;`
D. `display: block;`

**Câu 5 (Flexbox):** Để căn giữa một phần tử con theo cả chiều dọc và chiều ngang trong container Flexbox, ta dùng tổ hợp thuộc tính nào?
A. `justify-content: center; align-items: center;`
B. `text-align: center; vertical-align: middle;`
C. `justify-content: space-between; align-content: center;`
D. `flex-direction: column; align-items: center;`

**Câu 6 (Flexbox):** Thuộc tính `flex-grow: 1` có ý nghĩa gì?
A. Phần tử sẽ co lại nếu không đủ chỗ.
B. Phần tử sẽ giãn ra để lấp đầy khoảng trống còn thừa.
C. Phần tử giữ nguyên kích thước ban đầu.
D. Phần tử sẽ xuống dòng.

**Câu 7 (CSS Grid):** Để tạo một lưới gồm 3 cột có kích thước bằng nhau, ta dùng khai báo nào?
A. `grid-template-columns: 33% 33% 33%;`
B. `grid-template-columns: repeat(3, 1fr);`
C. `grid-template-columns: auto auto auto;`
D. Cả A, B, C đều có thể đúng (nhưng B là tối ưu nhất).

**Câu 8 (CSS Grid):** `gap: 20px;` trong Grid tương đương với?
A. `margin: 20px;`
B. `padding: 20px;`
C. `row-gap: 20px; column-gap: 20px;`
D. `grid-gap: 10px 10px;`

**Câu 9 (Position):** Giá trị nào của `position` làm cho phần tử trôi nổi theo cửa sổ trình duyệt (viewport) khi cuộn trang?
A. `absolute`
B. `relative`
C. `fixed`
D. `sticky`

**Câu 10 (Responsive):** Media query nào sau đây áp dụng cho màn hình có chiều rộng tối đa là 768px?
A. `@media (min-width: 768px) { ... }`
B. `@media (max-width: 768px) { ... }`
C. `@media (width: 768px) { ... }`
D. `@media screen and (device-width: 768px) { ... }`

**Câu 11 (Pseudo-classes):** Trạng thái `:hover` được kích hoạt khi nào?
A. Khi người dùng click vào phần tử.
B. Khi người dùng di chuột vào phần tử.
C. Khi phần tử đang được focus.
D. Khi trang web vừa tải xong.

**Câu 12 (CSS Units):** Đơn vị nào sau đây là đơn vị tuyệt đối (kích thước cố định)?
A. `rem`
B. `em`
C. `px`
D. `%`

**Câu 13 (Display):** `display: none` khác `visibility: hidden` như thế nào?
A. `display: none` vẫn giữ khoảng trống của phần tử, `visibility: hidden` thì không.
B. `display: none` xóa phần tử khỏi luồng layout, `visibility: hidden` chỉ ẩn đi nhưng vẫn giữ khoảng trống.
C. Không có gì khác nhau.
D. `visibility: hidden` không thể tương tác được, `display: none` vẫn click được.

**Câu 14 (Z-index):** Thuộc tính `z-index` dùng để làm gì?
A. Thay đổi độ trong suốt của phần tử.
B. Xác định thứ tự xếp chồng (lớp trên/lớp dưới) của các phần tử.
C. Di chuyển phần tử theo trục Z (3D).
D. Phóng to/thu nhỏ phần tử.

**Câu 15 (Image):** Để ảnh nền (background-image) phủ kín container mà không bị méo, ta dùng?
A. `background-size: contain;`
B. `background-size: cover;`
C. `background-size: 100% 100%;`
D. `background-repeat: no-repeat;`

---

## PHẦN 2: TỰ LUẬN & THỰC HÀNH (4 Điểm)

### Câu 1: Lý thuyết & Cơ chế (1.5 Điểm)
Cho đoạn mã HTML và CSS sau:

**HTML:**
```html
<div id="container" class="box">
    <p class="text" style="color: blue;">Hello World</p>
</div>
```

**CSS:**
```css
#container .text { color: red; }
p { color: green !important; }  
.box .text { color: yellow; }   
```

**Yêu cầu:**
1. Văn bản "Hello World" sẽ có màu gì? Tại sao?
2. Suy luận và cho biết thẻ **!important** dùng để làm gì? 

### Câu 2: Coding Layout (2.5 Điểm)
Viết mã HTML và CSS để tạo ra một **Card sản phẩm** đơn giản với các yêu cầu sau:
1. **Cấu trúc:**
   - Một container bao quanh.
   - Hình ảnh sản phẩm ở trên cùng.
   - Tiêu đề sản phẩm.
   - Giá tiền.
   - Nút "Mua ngay".
2. **Style:**
   - Card có viền, bo góc nhẹ, đổ bóng (box-shadow).
   - Hình ảnh chiếm 100% chiều rộng card.
   - Nút "Mua ngay" nằm ở dưới cùng, khi hover vào thì đổi màu nền.
3. **Responsive:**
   - Trên Desktop: Card có chiều rộng cố định (ví dụ 300px).
   - Trên Mobile (dưới 480px): Card chiếm 100% chiều rộng màn hình.

*(Học sinh viết code trực tiếp vào bài làm)*

---

## PHẦN 3: TƯ DUY SÁNG TẠO & AI (2 Điểm)

**Yêu cầu:**
1. **Xây dựng trang web giới thiệu bản thân (1 Điểm):** Xây dựng trang web có thông tin của bản thân, có ảnh đại diện, avatar.
2. **Prompt Engineering (1 Điểm):** Viết lại câu lệnh con đã dùng để hỏi AI giúp mình tạo trang web.

---
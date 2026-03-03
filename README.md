# VISUALIZER THUẬT TOÁN EXTERNAL MERGE SORT

---

## 📘 Thông Tin Bài Tập
- **Trường**: UIT-VNUHCM
- **Tên môn học:** Cấu Trúc Dữ Liệu và Giải Thuật Nâng Cao
- **Lớp:** CS523.Q21
- **Giảng viên giảng dạy:** MSc Nguyễn Thanh Sơn
- **Sinh viên thực hiện:** Ngô Hồng Vinh
- **MSSV:** 24522016

---

## 📌 Giới Thiệu Đề Tài

Đây là project xây dựng **trình mô phỏng (visualizer) thuật toán External Merge Sort** – một thuật toán sắp xếp ngoài (external sorting) được sử dụng khi dữ liệu quá lớn và không thể chứa toàn bộ trong bộ nhớ chính (RAM). Project dựa trên [baseline].(https://github.com/valeriodiste/ExternalMergeSortVisualizer)

Chương trình giúp minh họa trực quan:

- Quá trình tạo các "runs" ban đầu
- Quá trình trộn nhiều nhánh (k-way merge)
- Cách sử dụng buffer trong bộ nhớ
- Mô phỏng thao tác đọc/ghi theo từng page trên đĩa

Mục tiêu của project là nộp bài tập đầy đủ và kiếm điểm thực hành (Thứ cho em nói thẳng, tại vì ai cũng thế).

---

## 🚀 Chức Năng Chính

- Mô phỏng trực quan thuật toán External Merge Sort
- Điều chỉnh số lượng buffer frames (M)
- Biểu diễn dữ liệu theo từng page
- Hỗ trợ đọc file nhị phân (.bin)
- Hỗ trợ số thực 64-bit (Float64 – 8 bytes)
- Điều chỉnh tốc độ animation

---

## 📂 Định Dạng File Đầu Vào

Chương trình sử dụng file nhị phân (.bin) chứa:

- Các số thực 64-bit (mỗi số 8 byte)
- Định dạng Little-endian
- Không chứa ký tự xuống dòng hoặc khoảng trắng

### Cấu trúc file

```
[8 bytes][8 bytes][8 bytes]...
```

Ví dụ: nếu file có 50 phần tử

```
50 × 8 bytes = 400 bytes
```

### Ví dụ tạo file test bằng Python

```python
import struct
import random

with open("data.bin", "wb") as f:
    for _ in range(50):
        f.write(struct.pack("<d", random.uniform(-100, 100)))
```

---

## 🧠 Nguyên Lý Hoạt Động

### Giai đoạn 1 – Tạo Runs

- Đọc tối đa M pages vào bộ nhớ
- Sắp xếp trong bộ nhớ (internal sort)
- Ghi các runs đã sắp xếp xuống đĩa

### Giai đoạn 2 – Trộn K-Nhánh

- Sử dụng 1 buffer làm output
- Sử dụng M-1 buffer làm input
- Trộn các runs cho đến khi còn 1 file đã sắp xếp hoàn chỉnh

---

## 🛠 Công Nghệ Sử Dụng

- HTML / CSS / JavaScript

---

## Hướng Dẫn Sử Dụng
- Vui lòng tham khảo file:... để biết cách sử dụng (Sẽ update sau)
- Thêm kiểm tra header file để xác thực dữ liệu

---



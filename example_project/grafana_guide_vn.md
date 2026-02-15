# Hướng dẫn sử dụng Grafana toàn tập (Tiếng Việt)

Chào mừng bạn đến với hướng dẫn sử dụng Grafana. Tài liệu này sẽ giúp bạn đi từ con số 0 đến việc làm chủ các bản điều khiển (Dashboards) chuyên nghiệp.

---

## 1. Grafana là gì?

**Grafana** là một nền tảng mã nguồn mở dùng để **giám sát (monitoring)** và **trực quan hóa dữ liệu (visualization)**. 

### Tại sao nên dùng Grafana?
- **Đa kết nối:** Hỗ trợ hàng trăm nguồn dữ liệu khác nhau (Prometheus, MySQL, InfluxDB, CloudWatch...).
- **Dashboard đẹp mắt:** Cung cấp nhiều loại biểu đồ (Graph, Gauge, Table, Heatmap...).
- **Cảnh báo linh hoạt:** Tự động gửi thông báo khi có sự cố.
- **Cồng đồng lớn:** Bạn có thể tải về các mẫu Dashboard có sẵn từ trang chủ Grafana.

---

## 2. Hướng dẫn cài đặt

Cách nhanh nhất và phổ biến nhất hiện nay là sử dụng **Docker**.

### Cách 1: Sử dụng Docker (Khuyên dùng)
Bạn chỉ cần chạy một lệnh duy nhất trong terminal/PowerShell:

```bash
docker run -d -p 3000:3000 --name=grafana grafana/grafana
```

Sau khi chạy, hãy mở trình duyệt và truy cập: `http://localhost:3000`
- **Username mặc định:** `admin`
- **Password mặc định:** `admin`

### Cách 2: Cài đặt trên Windows (Standalone)
1. Truy cập [trang tải xuống của Grafana](https://grafana.com/grafana/download?platform=windows).
2. Tải file `.msi` và chạy bộ cài đặt.
3. Sau khi cài xong, dịch vụ Grafana sẽ tự khởi động. Truy cập `http://localhost:3000` để bắt đầu.

---

## 3. Kết nối Nguồn dữ liệu (Data Sources)

Dữ liệu của Grafana không nằm tại chính nó mà được lấy từ các nguồn khác. Một trong những nguồn phổ biến nhất là **Prometheus**.

### Các bước kết nối:
1. Click vào icon **Connections** (hình bánh răng hoặc hình vuông) ở thanh bên trái.
2. Chọn **Data Sources**.
3. Nhấn **Add data source**.
4. Tìm và chọn **Prometheus**.
5. Nhập URL của Prometheus (ví dụ: `http://localhost:9090`).
6. Kéo xuống dưới cùng và nhấn **Save & Test**. Nếu hiện màu xanh ("Data source is working") là thành công.

---

## 4. Xây dựng Bảng điều khiển (Dashboards)

Dashboard là nơi chứa các Panel (ô biểu đồ).

### Cách tạo Panel đầu tiên:
1. Click vào icon **Dashboards** -> **New** -> **New Dashboard**.
2. Nhấn **Add visualization**.
3. Chọn nguồn dữ liệu bạn vừa cấu hình (ví dụ: Prometheus).
4. Trong phần **Query**, nhập câu truy vấn (ví dụ: `up` để kiểm tra các service đang hoạt động).
5. Ở bảng bên phải, bạn có thể thay đổi:
   - **Title:** Tiêu đề biểu đồ.
   - **Visualization type:** Chọn kiểu biểu đồ (Bar chart, Time series...).
6. Nhấn **Apply** ở góc trên bên phải.
7. Nhấn icon **Save** (hình đĩa mềm) để lưu Dashboard.

---

## 5. Hệ thống Cảnh báo (Alerting)

Grafana có thể giúp bạn "ngủ ngon" bằng cách tự động cảnh báo khi có chỉ số bất thường.

### Cách thiết lập cảnh báo:
1. Quay lại Panel bạn đã tạo. Nhấn vào tiêu đề Panel -> **Edit**.
2. Chọn tab **Alert**.
3. Nhấn **Create alert rule from this panel**.
4. Cấu hình điều kiện: Ví dụ, nếu CPU > 80% trong vòng 5 phút.
5. **Contact Points:** Đây là nơi bạn chọn gửi tin nhắn đi đâu (Telegram, Slack, Email...).
   - Bạn cần vào mục **Alerting** -> **Contact points** bên menu trái để cấu hình kênh thông báo trước.

---

## 6. Tổng kết và Tài nguyên học tập

Grafana rất mạnh mẽ, và cách tốt nhất để học là **thực hành**.

### Các nguồn tham khảo thêm:
- **Grafana Play:** [Dùng thử Grafana online](https://play.grafana.org/) (không cần cài đặt).
- **Grafana Dashboards:** [Tìm các mẫu Dashboard đẹp](https://grafana.com/grafana/dashboards/).
- **Tài liệu chính thức:** [Grafana Documentation](https://grafana.com/docs/).

Chúc bạn sớm trở thành một chuyên gia quan sát hệ thống với Grafana!

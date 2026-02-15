# Dự án ví dụ Grafana đơn giản (Python + Prometheus + Grafana)

Dự án này giúp bạn thực hành kết nối Grafana với dữ liệu thực tế được sinh ra từ một script Python.

## Cấu trúc thư mục
- `app.py`: Script Python tạo dữ liệu nhiệt độ giả lập.
- `Dockerfile`: File cấu hình để đóng gói app Python vào Docker.
- `prometheus.yml`: Cấu hình để Prometheus lấy dữ liệu từ app Python.
- `docker-compose.yml`: File chạy cả 3 dịch vụ cùng một lúc.

## Cách chạy dự án

1. **Chuẩn bị:** Đảm bảo máy bạn đã cài đặt [Docker Desktop](https://www.docker.com/products/docker-desktop/).
2. **Khởi chạy:** Mở Terminal (PowerShell hoặc CMD) tại thư mục `d:\Grafana\example_project` và chạy lệnh:
   ```bash
   docker-compose up -d
   ```
3. **Kiểm tra các dịch vụ:**
   - **App Metrics:** Truy cập `http://localhost:8000` (Bạn sẽ thấy các dòng `room_temperature_celsius`).
   - **Prometheus:** Truy cập `http://localhost:9090` (Vào Status -> Targets để xem app đã 'UP' chưa).
   - **Grafana:** Truy cập `http://localhost:3000` (User/Pass: `admin/admin`).

## Cách tạo biểu đồ trên Grafana

1. **Thêm Data Source:**
   - Chọn **Connections** -> **Data Sources** -> **Add data source**.
   - Chọn **Prometheus**.
   - Nhập URL: `http://prometheus:9090` (Lưu ý: dùng tên service `prometheus` vì đang chạy trong Docker network).
   - Nhấn **Save & Test**.

2. **Tạo Dashboard:**
   - Vào **Dashboards** -> **New** -> **New Dashboard**.
   - Nhấn **Add visualization**.
   - Trong phần Query, nhập: `room_temperature_celsius`.
   - Nhấn **Run queries** để thấy dữ liệu.
   - Nhấn **Apply** để lưu Panel.

Bây giờ bạn sẽ thấy biểu đồ nhiệt độ thay đổi liên tục trên Grafana!

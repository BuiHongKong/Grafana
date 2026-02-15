from prometheus_client import start_http_server, Gauge
import random
import time

# Tạo một Gauge metric để mô phỏng nhiệt độ
TEMPERATURE = Gauge('room_temperature_celsius', 'Nhiệt độ phòng (độ C)')

if __name__ == '__main__':
    # Chạy server metrics ở port 8000
    start_http_server(8000)
    print("Metrics server started on port 8000")
    
    while True:
        # Giả lập nhiệt độ thay đổi từ 20 đến 30 độ C
        temp = random.uniform(20, 30)
        TEMPERATURE.set(temp)
        print(f"Current temp: {temp:.2f}")
        time.sleep(5)

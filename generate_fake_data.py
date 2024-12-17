import socket
import time
import random


def send_udp_message(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.sendto(message.encode(), (ip, port))


def generate_data():
    altitude = 0
    while True:
        altitude += 2
        speed = random.uniform(10, 20)
        accel = random.uniform(0, 5)
        # Define the latitude and longitude boundaries for Israel
        lat_min, lat_max = 29.5, 33.5
        lon_min, lon_max = 34.3, 35.9
        lat = random.uniform(lat_min, lat_max)
        lon = random.uniform(lon_min, lon_max)
        data = {
            'altitude': altitude,
            'speed': speed,
            'accel': accel,
            'lat': lat,
            'lon': lon
        }
        yield str(data)


def main():
    ip = '127.0.0.1'
    port = 5555
    data_generator = generate_data()
    while True:
        message = next(data_generator)
        send_udp_message(ip, port, message)
        time.sleep(0.3333)


if __name__ == "__main__":
    main()

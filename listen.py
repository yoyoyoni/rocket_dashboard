import socket
from influxdb_client import InfluxDBClient, Point, WriteOptions
from time import time
import json


def parse_data(data: dict) -> Point:
    p = Point("rocket_data").tag('env', 'test')
    p = p.field('altitude', data.get('altitude'))
    p = p.field('speed', data.get('speed'))
    p = p.field('accel', data.get('accel'))
    p = p.field('lat', data.get('lat'))
    p = p.field('lon', data.get('lon'))
    p = p.time(int(time() * 1000000000))
    return p


def listen_on_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
            server_socket.bind(('', port))
            print(f"Listening for UDP messages on port {port}...")

            with InfluxDBClient(url="http://localhost:8086",
                                token="czYroe-q1_agYK9zROZ2lsffRYBzLhSbpMp__CMLiqSHCOVOQb4wa9kEUgFD8-1QkZJLa_bIkQIu1J8RvmRPOA==",
                                org="Rocket") as _client:
                with _client.write_api(write_options=WriteOptions(batch_size=500,
                                                                  flush_interval=1_000,
                                                                  jitter_interval=500,
                                                                  retry_interval=5_000,
                                                                  max_retries=5,
                                                                  max_retry_delay=30_000,
                                                                  exponential_base=2)) as _write_client:
                    while True:
                        data, client_address = server_socket.recvfrom(512)
                        datapoint = parse_data(json.loads(data.decode().replace("'", '"')))
                        _write_client.write('Rocket', 'Rocket', record=datapoint)
                        print(f"Received from {client_address}: {data.decode()}")

    except KeyboardInterrupt:
        print("\nServer stopped by user.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    listen_on_port(5555)

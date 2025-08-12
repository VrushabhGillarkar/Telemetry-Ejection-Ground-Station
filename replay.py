# replay.py
# replay.py
import csv
import json
import socket
import time

CSV_FILE = "data/received_telemetry.csv"
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def replay_csv(filename, delay=0.2):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            packet = {k: try_float(v) for k, v in row.items()}
            sock.sendto(json.dumps(packet).encode('utf-8'), (UDP_IP, UDP_PORT))
            time.sleep(delay)

def try_float(value):
    try:
        return float(value)
    except ValueError:
        return value

if __name__ == "__main__":
    print(f"Replaying {CSV_FILE}...")
    replay_csv(CSV_FILE)
    print("Replay complete.")

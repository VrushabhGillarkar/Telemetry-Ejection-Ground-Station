import socket
import json
import time
import math
import random

# UDP settings
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# Create UDP socket for sending only
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("🚀 Flight Simulator started — sending telemetry data...")
start_time = time.time()

try:
    while True:
        # Elapsed time
        t = time.time() - start_time

        # Simulated flight data
        altitude = 100 * math.sin(t / 5) + 200 + random.uniform(-5, 5)  # m
        velocity = 20 * math.cos(t / 5) + random.uniform(-1, 1)         # m/s

        # Telemetry packet
        packet = {
            "time": t,
            "altitude": altitude,
            "velocity": velocity
        }

        # Send data
        sock.sendto(json.dumps(packet).encode(), (UDP_IP, UDP_PORT))

        # 200 ms delay between packets
        time.sleep(0.2)

except KeyboardInterrupt:
    print("\n🛑 Flight Simulator stopped.")
    sock.close()

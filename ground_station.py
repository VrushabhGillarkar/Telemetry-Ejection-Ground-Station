import sys
import socket
import json
import threading
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QMessageBox
)
from PySide6.QtCore import QTimer
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# UDP settings
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

class GroundStationGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Telemetry & Ejection Ground Station")

        # Data storage
        self.time_data = []
        self.altitude_data = []
        self.velocity_data = []

        # Create widgets
        self.start_button = QPushButton("Start Listening")
        self.stop_button = QPushButton("Stop Listening")
        self.eject_button = QPushButton("Manual Eject")

        self.time_label = QLabel("Time: 0.00 s")
        self.altitude_label = QLabel("Altitude: 0.00 m")
        self.velocity_label = QLabel("Velocity: 0.00 m/s")

        # Plot setup
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Altitude (m)")
        self.ax.grid(True)

        # Layout setup
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.eject_button)

        data_layout = QVBoxLayout()
        data_layout.addWidget(self.time_label)
        data_layout.addWidget(self.altitude_label)
        data_layout.addWidget(self.velocity_label)

        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addLayout(data_layout)
        main_layout.addWidget(self.canvas)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Networking (receiver)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, UDP_PORT))
        self.running = False

        # Button actions
        self.start_button.clicked.connect(self.start_listening)
        self.stop_button.clicked.connect(self.stop_listening)
        self.eject_button.clicked.connect(self.manual_eject)

        # Timer for GUI updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)

    def start_listening(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.receive_data, daemon=True).start()
            self.timer.start(200)  # update every 200 ms

    def stop_listening(self):
        self.running = False
        self.timer.stop()

    def manual_eject(self):
        QMessageBox.information(self, "Manual Eject", "Manual Ejection Command Sent!")
        print("Manual eject triggered!")

    def receive_data(self):
        while self.running:
            try:
                data, _ = self.sock.recvfrom(1024)
                packet = json.loads(data.decode())
                self.time_data.append(packet["time"])
                self.altitude_data.append(packet["altitude"])
                self.velocity_data.append(packet["velocity"])

                # Update labels
                self.time_label.setText(f"Time: {packet['time']:.2f} s")
                self.altitude_label.setText(f"Altitude: {packet['altitude']:.2f} m")
                self.velocity_label.setText(f"Velocity: {packet['velocity']:.2f} m/s")

            except Exception as e:
                print("Receive error:", e)

    def update_plot(self):
        self.ax.clear()
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Altitude (m)")
        self.ax.grid(True)
        if self.time_data:
            self.ax.plot(self.time_data, self.altitude_data, label="Altitude", color='blue')
            self.ax.legend()
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GroundStationGUI()
    window.show()
    sys.exit(app.exec())
import sys
import socket
import json
import threading
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel
from PySide6.QtCore import QTimer
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

class GroundStationGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Telemetry & Ejection Ground Station")
        self.setGeometry(100, 100, 800, 500)

        # Data storage
        self.time_data = []
        self.altitude_data = []
        self.velocity_data = []

        # Buttons
        self.start_button = QPushButton("Start Listening")
        self.stop_button = QPushButton("Stop Listening")
        self.eject_button = QPushButton("Manual Eject")

        # Labels
        self.time_label = QLabel("Time: 0.00 s")
        self.altitude_label = QLabel("Altitude: 0.00 m")
        self.velocity_label = QLabel("Velocity: 0.00 m/s")

        # Matplotlib figure
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Altitude (m)")
        self.ax.grid(True)

        # Layouts
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.eject_button)

        data_layout = QVBoxLayout()
        data_layout.addWidget(self.time_label)
        data_layout.addWidget(self.altitude_label)
        data_layout.addWidget(self.velocity_label)

        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addLayout(data_layout)
        main_layout.addWidget(self.canvas)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Networking
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((UDP_IP, UDP_PORT))
        self.running = False

        # Button actions
        self.start_button.clicked.connect(self.start_listening)
        self.stop_button.clicked.connect(self.stop_listening)

        # Timer for GUI updates
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)

        # Auto-start listening
        self.start_listening()

    def start_listening(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.receive_data, daemon=True).start()
            self.timer.start(200)  # update every 200 ms

    def stop_listening(self):
        self.running = False
        self.timer.stop()

    def receive_data(self):
        while self.running:
            try:
                data, _ = self.sock.recvfrom(1024)
                packet = json.loads(data.decode())

                self.time_data.append(packet["time"])
                self.altitude_data.append(packet["altitude"])
                self.velocity_data.append(packet["velocity"])

                # Update labels
                self.time_label.setText(f"Time: {packet['time']:.2f} s")
                self.altitude_label.setText(f"Altitude: {packet['altitude']:.2f} m")
                self.velocity_label.setText(f"Velocity: {packet['velocity']:.2f} m/s")

            except Exception as e:
                print("Receive error:", e)

    def update_plot(self):
        self.ax.clear()
        self.ax.set_xlabel("Time (s)")
        self.ax.set_ylabel("Altitude (m)")
        self.ax.grid(True)
        if self.time_data:
            self.ax.plot(self.time_data, self.altitude_data, label="Altitude", color="blue")
            self.ax.legend()
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GroundStationGUI()
    window.show()
    sys.exit(app.exec())

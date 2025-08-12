# 🚀 Telemetry & Ejection Ground Station

Real-time flight telemetry monitoring and control dashboard, built for **rockets, drones, and experimental vehicles**.  
It receives **live data via UDP** and displays it on a professional, interactive GUI.

---

## 📝 Introduction

In aerospace, drones, and rocketry projects, **real-time telemetry** is essential for monitoring key parameters such as altitude, velocity, and time of flight.  
This project aims to provide a **user-friendly ground station** that can:
- Receive telemetry data in real-time
- Display data visually and numerically
- Offer manual control triggers like **Ejection**

With **Python, PySide6, and Matplotlib**, this tool becomes a versatile solution for both simulation and real hardware setups.

---

## ❓ Problem Statement

Traditional telemetry dashboards are:
- Often **expensive**
- Difficult to set up for small experimental projects
- Lack **customization options**

This project solves the problem by:
- Offering a **free, open-source** telemetry solution
- Being **customizable** for any flight or sensor-based project
- Supporting **simulation and hardware integration**

---

## 🛠 Technology Stack

| Component        | Technology Used       | Purpose |
|------------------|-----------------------|---------|
| Programming Lang | Python 3.8+            | Core application logic |
| GUI Framework    | PySide6 (Qt for Python) | Modern, responsive GUI |
| Plotting Library | Matplotlib              | Real-time altitude plotting |
| Networking       | UDP Sockets             | Data transmission between sender and receiver |
| Data Format      | JSON                    | Easy-to-read structured telemetry packets |

---

## 📸 Screenshots & Demo

### Telemetry Simulation
![Flight Data Graph](Screenshot%202025-08-12%20200033.png)

### Ground Station Dashboard
![Dashboard Screenshot](Screenshot%202025-08-12%20195555.png)

### Flight Data Graph

![Telemetry Simulation](Screenshot%202025-08-12%20200105.png)

### Live Demo Video
[▶ Watch Demo](Screen%20Recording%202025-08-12%20200136.mp4)

---

## 📂 Project Structure

├── ground_station.py # Main GUI application for telemetry display and controls
├── flight_simulator.py # Simulates flight telemetry data for testing
├── README.md # Project documentation
└── requirements.txt # Python dependencies



---

## ✨ Features

- 📡 **Real-time UDP Telemetry Reception**
- 📊 **Dynamic Altitude Graph**
- ⏱ **Live Time & Velocity Readout**
- 🖱 **Manual Ejection Trigger Button**
- 🔄 **Simulation Mode with `flight_simulator.py`**
- 🖥 **Clean, Minimalistic UI for Quick Monitoring**

---

## ⚙ Installation

**Step 1:** Install Python 3.8+  
[Download Python](https://www.python.org/downloads/)

**Step 2:** Clone the repository
```bash
git clone https://github.com/YourUsername/telemetry-ground-station.git
cd telemetry-ground-station
```

Step 3: Install dependencies

```bash
Copy
Edit
pip install PySide6 matplotlib
```
▶ Usage

1️⃣ Start the Ground Station

```bash

python ground_station.py
```
This will open the GUI Dashboard.

2️⃣ Run the Flight Simulator

```bash

python flight_simulator.py
```
This sends mock telemetry data to the Ground Station.

📡 Live Telemetry
The dashboard updates in real-time with:
```
Time (seconds)
Altitude (meters)
Velocity (m/s)
Altitude vs Time graph
```
📦 UDP Data Format
The telemetry data is sent as JSON:
```
json
Copy
Edit
{
    "time": 5.32,
    "altitude": 123.45,
    "velocity": 12.78
}
```
💡 Notes
```
Ensure no other program is using the same UDP port (5005) to avoid socket binding errors.
If using real hardware, update the UDP_IP and UDP_PORT values in ground_station.py to match your setup.
The GUI is designed for expandability — you can add more parameters (e.g., GPS, battery voltage) easily.
```







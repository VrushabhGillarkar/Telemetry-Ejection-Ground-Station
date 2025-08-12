# 🚀 Telemetry & Ejection Ground Station  

A real-time telemetry monitoring and manual ejection trigger system for rockets, UAVs, or high-altitude projects. The system includes a **Ground Station GUI** to display live flight data and a **Flight Simulator** for testing without hardware.  

---

## 📖 Introduction  

During flight missions, **real-time telemetry** is crucial for tracking altitude, velocity, and other parameters. This project provides:  

- A **Ground Station** for visualizing data from a flight vehicle.  
- A **Flight Simulator** for generating test data over UDP.  
- An optional **manual ejection trigger** for parachute deployment or payload separation.  

---

## 🛠 Problem Statement  

In many student and hobbyist aerospace projects, telemetry systems are:  
- Expensive 💰  
- Difficult to integrate  
- Lack user-friendly monitoring tools  

**Goal:** Build an **affordable**, **easy-to-use**, and **extensible** ground station for real-time monitoring.  

---

## 🎯 Objectives  

1. Receive telemetry over **UDP**.  
2. Display **live time, altitude, velocity**.  
3. Plot altitude vs. time in real-time.  
4. Simulate flight data for development and testing.  

---

## 📷 Screenshots  

| Dashboard View | Live Graph View |
|----------------|-----------------|
| ![Dashboard](assets/dashboard_screenshot.png) | ![Graph](assets/demo_screenshot.png) |

---

## 🎥 Live Demo  

**YouTube Demo Video:** [📺 Watch Here](https://youtu.be/example)  

**GIF Preview:**  
![Demo GIF](assets/demo.gif)  

---

## 📂 Project Structure
```
📦 telemetry-ground-station
├── ground_station.py       # Main GUI application
├── flight_simulator.py     # Simulates flight data for testing
├── assets/
│   ├── dashboard_screenshot.png
│   ├── demo_screenshot.png
│   ├── demo.gif
├── README.md               # Documentation
```

---

## ✨ Features
- 📡 Real-time UDP Telemetry Reception  
- 📊 Dynamic Altitude Graph  
- ⏱ Live Time & Velocity Readout  
- 🖱 Manual Ejection Trigger Button  
- 🔄 Simulation Mode with `flight_simulator.py`  
- 🖥 Clean, Minimalistic UI for Quick Monitoring  

---

## 💻 Technology Stack
- Python 3.8+  
- PySide6 – GUI Framework  
- Matplotlib – Data visualization  
- Socket (UDP) – Network communication  
- Threading – Background data reception  

---

## ⚙ Installation

**Step 1:** Install Python 3.8+  
[Download Python](https://www.python.org/downloads/)  

**Step 2:** Clone the repository  
```bash
git clone https://github.com/YourUsername/telemetry-ground-station.git
cd telemetry-ground-station
```

**Step 3:** Install dependencies  
```bash
pip install PySide6 matplotlib
```

---

## ▶ Usage

**1️⃣ Start the Ground Station**  
```bash
python ground_station.py
```
This will open the GUI Dashboard.

**2️⃣ Run the Flight Simulator**  
```bash
python flight_simulator.py
```
This sends mock telemetry data to the Ground Station.

---

## 📡 Live Telemetry
The dashboard updates in real-time with:  
- Time (seconds)  
- Altitude (meters)  
- Velocity (m/s)  
- Altitude vs. Time graph  

---

## 📦 UDP Data Format
Telemetry packets are sent as JSON:  
```json
{
    "time": 5.32,
    "altitude": 123.45,
    "velocity": 12.78
}
```

---

## 📝 Notes
- Ensure no other program is using the same UDP port (5005) to avoid socket binding errors.  
- If using real hardware, update `UDP_IP` and `UDP_PORT` in `ground_station.py`.  
- Easily extendable for GPS, battery, temperature, etc.  

---

## 📜 License
This project is licensed under the MIT License.  
Feel free to use, modify, and distribute as long as proper credit is given.  

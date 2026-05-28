# Real-time Coal Quality Prediction System

This project is an advanced, real-time system for predicting the quality of coal. It integrates computer vision (CNN-LSTM) from a live conveyor belt feed and physical sensor data (ANN) for robust quality control.

## Project Structure
- `src/`: Python source code for data acquisition, preprocessing, and model inference.
  - `camera_stream.py`: Handles OpenCV video feed.
  - `dynamic_fps.py`: Logic for adjusting FPS based on conveyor speed.
  - `image_quality.py`: Image quality assessment (dust/occlusion detection).
  - `sensor_acquisition.py`: Simulator/Connector for OPC-UA/Modbus sensors.
- `data/`: Directory for storing raw and processed datasets (images, sensor logs).
- `models/`: Directory for saving trained AI model weights (CNN-LSTM, ANN).
- `web/`: Frontend dashboard for real-time monitoring and anomaly alerts.
- `other/`: Reference papers and initial project ideas.

## Getting Started

### 1. Prerequisites
- Python 3.8+
- Modern Web Browser (for the dashboard)

### 2. Installation
Create a virtual environment and install the required Python packages:

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate
pip install tensorflow opencv-python pandas numpy scikit-learn flask

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
pip install tensorflow opencv-python pandas numpy scikit-learn flask
```

### 3. Running the Web Dashboard (Frontend Simulation)
To preview the frontend UI simulation:
```bash
cd web
python -m http.server 8000
```
Then navigate to `http://localhost:8000` in your web browser.

## Contributing
Please refer to the `implementation_plan.txt` in the root directory for a detailed phase-by-phase breakdown of the ongoing project tasks.

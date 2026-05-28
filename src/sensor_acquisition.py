import random
import time

class SensorAcquisition:
    """
    Simulates physical sensor data acquisition from Modbus/OPC-UA endpoints.
    In a real implementation, this would connect to the PLC/SCADA systems.
    """
    def __init__(self):
        self.connected = False

    def connect(self):
        print("[SensorAcquisition] Connecting to sensors via Modbus/OPC-UA...")
        time.sleep(1)
        self.connected = True
        print("[SensorAcquisition] Connected successfully.")

    def read_sensors(self):
        """
        Reads values for Moisture, Ash, Volatile Matters, Fixed Carbon, GCV.
        Values are simulated.
        """
        if not self.connected:
            raise ConnectionError("Sensors not connected.")
        
        # Simulated sensor readings
        data = {
            "moisture_pct": round(random.uniform(5.0, 15.0), 2),
            "ash_pct": round(random.uniform(10.0, 30.0), 2),
            "volatile_matters_pct": round(random.uniform(20.0, 35.0), 2),
            "fixed_carbon_pct": round(random.uniform(35.0, 55.0), 2),
            "gcv_kcal_kg": round(random.uniform(4000, 6500), 0)
        }
        return data

    def disconnect(self):
        self.connected = False
        print("[SensorAcquisition] Disconnected.")

if __name__ == "__main__":
    sensor_sys = SensorAcquisition()
    sensor_sys.connect()
    try:
        for _ in range(5):
            print(sensor_sys.read_sensors())
            time.sleep(1)
    finally:
        sensor_sys.disconnect()

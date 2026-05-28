import cv2
import time

class CameraStream:
    def __init__(self, source=0, target_fps=30):
        self.source = source
        self.target_fps = target_fps
        self.cap = cv2.VideoCapture(self.source)
        # Set camera properties if possible
        # self.cap.set(cv2.CAP_PROP_FPS, self.target_fps)

    def set_fps(self, fps):
        """Dynamic FPS adjustment based on conveyor speed."""
        self.target_fps = fps
        # In a real industrial camera, we'd use vendor-specific SDKs here
        print(f"[CameraStream] Adjusting camera FPS to {self.target_fps}")

    def read_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            print("[CameraStream] Error: Failed to read frame.")
            return None
        return frame

    def release(self):
        self.cap.release()

if __name__ == "__main__":
    cam = CameraStream()
    try:
        while True:
            frame = cam.read_frame()
            if frame is not None:
                cv2.imshow("Conveyor Belt Feed", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cam.release()
        cv2.destroyAllWindows()

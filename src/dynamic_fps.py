class FPSController:
    """
    Dynamically adjusts the camera FPS based on conveyor belt speed.
    """
    def __init__(self, base_speed_m_s=2.0, base_fps=30):
        self.base_speed = base_speed_m_s
        self.base_fps = base_fps

    def calculate_optimal_fps(self, current_speed_m_s):
        """
        Maps current belt speed to optimal camera FPS to maintain consistent spatial resolution.
        """
        if current_speed_m_s <= 0:
            return 1  # Minimum FPS to keep stream alive
            
        ratio = current_speed_m_s / self.base_speed
        optimal_fps = int(self.base_fps * ratio)
        
        # Clamp FPS between 1 and 60
        optimal_fps = max(1, min(60, optimal_fps))
        return optimal_fps

if __name__ == "__main__":
    controller = FPSController()
    speeds = [0.0, 1.0, 2.0, 3.0, 4.0]
    for s in speeds:
        fps = controller.calculate_optimal_fps(s)
        print(f"Belt Speed: {s} m/s -> Optimal FPS: {fps}")

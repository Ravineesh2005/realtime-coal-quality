import cv2
import numpy as np

class ImageQualityAssessor:
    def __init__(self, blur_threshold=100.0):
        # Variance of Laplacian threshold for blur detection
        self.blur_threshold = blur_threshold

    def is_occluded_or_blurred(self, frame):
        """
        Detects if a frame is significantly blurred or occluded by dust.
        Returns a boolean (True if blurred/occluded) and the variance score.
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Calculate the variance of the Laplacian
        variance = cv2.Laplacian(gray, cv2.CV_64F).var()
        
        # If variance is less than the threshold, it is considered blurry/occluded
        is_bad_quality = variance < self.blur_threshold
        return is_bad_quality, variance

    def defog_image(self, frame):
        """
        Simple digital defogging/de-hazing via histogram equalization.
        For more complex dust occlusion, auto-encoders would be applied.
        """
        # Convert to YUV to equalize only the luminance channel
        yuv = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
        yuv[:, :, 0] = cv2.equalizeHist(yuv[:, :, 0])
        defogged = cv2.cvtColor(yuv, cv2.COLOR_YUV2BGR)
        return defogged

if __name__ == "__main__":
    iqa = ImageQualityAssessor()
    # Dummy test
    dummy_frame = np.ones((480, 640, 3), dtype=np.uint8) * 128
    is_bad, score = iqa.is_occluded_or_blurred(dummy_frame)
    print(f"Bad Quality: {is_bad}, Score: {score}")

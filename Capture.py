import time
from abc import ABC, abstractmethod
import cv2
import numpy


class Capture(ABC):
    @abstractmethod
    def open(self):
        return False
    @abstractmethod
    def close(self):
        pass
    @abstractmethod
    def get_frame(self):
        return None

class Webcam(Capture):
    def __init__(self):
        self.device = None

    def open(self):
        self.device = cv2.VideoCapture(0) #Camera at index 0 #cv2.VideoCapture("rtsp://username:password@CAMERA_IP:554/stream")
        if not self.device.isOpened():
            print("Error: Failed to open a webcam")
            return False
        return True

    def close(self):
        self.device.release()

    def get_frame(self):
        success, frame = self.device.read()
        return frame

class FakeCapture(Capture):
    def __init__(self):
        self.open_time = None

    def open(self):
        self.open_time = time.time()
        return True
    def close(self):
        pass
    def get_frame(self):
        frame = numpy.zeros((480, 640, 3), dtype=numpy.uint8)

        t = time.time() - self.open_time
        # Moving circle
        x = int((numpy.sin(t) * 0.5 + 0.5) * 600) + 20
        cv2.circle(frame, (x, 240), 30, (0, 255, 0), -1)

        # Label
        cv2.putText(
            frame,
            f"FAKE CAMERA  {t:0.1f}s",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2
        )

        return frame


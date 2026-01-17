from abc import ABC, abstractmethod

import cv2


class Camera(ABC):
    def __init__(self, capture, view):
        self.capture = capture
        self.view = view

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def close(self):
        pass

class StandardCamera(Camera):
    def __init__(self, capture, view):
        super().__init__(capture, view)

    def open(self):
        self.capture.open()
        self.view.open()
    def run(self):
        while True:
            frame, timestamp = self.capture.get_frame()
            self.view.display(frame, timestamp)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def close(self):
        self.capture.close()
        self.view.close()

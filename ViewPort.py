from abc import ABC, abstractmethod

import cv2


class ViewPort(ABC):
    def __init__(self, imageModifiers):
        self.imageModifiers = imageModifiers
    @abstractmethod
    def open(self):
        return False
    @abstractmethod
    def close(self):
        pass
    @abstractmethod
    def display(self, frame, timestamp):
        pass

class CVViewPort(ViewPort):
    def __init__(self, imageModifiers):
        super().__init__(imageModifiers)
    def open(self):
        return True
    def close(self):
        cv2.destroyAllWindows()
    def display(self, frame, timestamp):
        for im in self.imageModifiers:
            frame = im.modify(frame, timestamp)
        cv2.imshow("Frame", frame)
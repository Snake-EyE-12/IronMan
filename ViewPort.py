from abc import ABC, abstractmethod

import cv2


class ViewPort(ABC):
    @abstractmethod
    def open(self):
        return False
    @abstractmethod
    def close(self):
        pass
    @abstractmethod
    def display(self, frame):
        pass

class CVViewPort(ViewPort):
    def open(self):
        return True
    def close(self):
        cv2.destroyAllWindows()
    def display(self, frame):
        cv2.imshow("Frame", frame)
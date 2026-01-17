from Camera import StandardCamera
from Capture import FakeCapture, Webcam
from ViewPort import CVViewPort
from ImageModifier import *


def get_camera(capture, view):
    return StandardCamera(capture, view)

def get_capture():
    return Webcam

def get_viewport():
    return CVViewPort

def get_imageModifiers():
    return [ColorCorrection, HandTrackModifier]


if __name__ == '__main__':
    cam = get_camera(get_capture(), get_viewport(get_imageModifiers()))
    cam.open()
    cam.run()
    cam.close()

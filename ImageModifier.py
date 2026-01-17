from abc import ABC, abstractmethod

import cv2
import mediapipe as mp


class ImageModifier(ABC):
    @abstractmethod
    def modify(self, frame):
        return None

class NullModification(ImageModifier):
    def modify(self, frame):
        return frame

class ColorCorrection(ImageModifier):
    def modify(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

class GrayScale(ImageModifier):
    def modify(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
class HandTrackModifier(ImageModifier):
    def __init__(self):
        # Download the model file from the official documentation
        model_path = 'hand_landmarker.task'

        # 1. Create a Hand Landmarker object
        self.baseOptions = mp.tasks.BaseOptions
        self.handLandmarker = mp.tasks.vision.HandLandmarker
        self.handLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
        self.visionRunningMode = mp.tasks.vision.RunningMode

        self.options = self.handLandmarkerOptions(
            base_options=self.baseOptions(model_asset_path=model_path),
            running_mode=self.visionRunningMode.LIVE_STREAM,
            num_hands=2,  # Maximum number of hands to detect
            result_callback=lambda result, output_image, timestamp_ms: print(f'Hand landmarks: {result.hand_landmarks}')
        )

    def modify(self, frame, timestamp):
        with self.handLandmarker.create_from_options(self.options) as landmarker:
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            frame_timestamp_ms = int(timestamp)
            landmarker.detect_async(mp_image, frame_timestamp_ms)

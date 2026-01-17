from abc import ABC, abstractmethod

import cv2
import mediapipe as mp
import time


class ImageModifier(ABC):
    @abstractmethod
    def modify(self, frame, timestamp):
        pass

class NullModification(ImageModifier):
    def modify(self, frame, timestamp):
        return frame

class ColorCorrection(ImageModifier):
    def modify(self, frame, timestamp):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

class CVColorCorrection(ImageModifier):
    def modify(self, frame, timestamp):
        return cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

class GrayScale(ImageModifier):
    def modify(self, frame, timestamp):
        return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

class HandTrackModifier(ImageModifier):
    def __init__(self):
        model_path = 'hand_landmarker.task'

        self.options = mp.tasks.vision.HandLandmarkerOptions(
            base_options=mp.tasks.BaseOptions(model_asset_path=model_path),
            running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
            num_hands=2,
            result_callback=self._on_result
        )

        self.landmarker = mp.tasks.vision.HandLandmarker.create_from_options(
            self.options
        )

    def _on_result(self, result, output_image, timestamp_ms):
        print(f'Hand landmarks: {result.hand_landmarks}')

    def modify(self, frame, timestamp):
        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=frame
        )

        self.landmarker.detect_async(mp_image, int(time.monotonic() * 1000))
        return frame

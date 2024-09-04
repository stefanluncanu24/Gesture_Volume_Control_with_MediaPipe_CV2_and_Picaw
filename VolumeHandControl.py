import cv2
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

class VolumeHandControl:
    def __init__(self):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        self.volume = cast(interface, POINTER(IAudioEndpointVolume))
        self.volRange = self.volume.GetVolumeRange()
        self.minVol, self.maxVol = self.volRange[0], self.volRange[1]

    def process_frame(self, img, lmList1, lmList2):
        if lmList1 and lmList2:
            img = self.draw_hands(img, lmList1)
            length = self.calculate_length(lmList1[4], lmList1[8])
            self.set_volume(length)
            img = self.highlight_volume_control(img, length, lmList1[4], lmList1[8])
        else:
            cv2.putText(img, 'Two hands required', (10, 100), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return img

    def draw_hands(self, img, landmarks):
        for landmark in [landmarks[4], landmarks[8]]: 
            cv2.circle(img, (landmark[1], landmark[2]), 12, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (landmarks[4][1], landmarks[4][2]), (landmarks[8][1], landmarks[8][2]), (0, 255, 0), 3)
        return img

    def calculate_length(self, thumb, index):
        return math.sqrt((index[1] - thumb[1]) ** 2 + (index[2] - thumb[2]) ** 2)

    def set_volume(self, length):
        volume = np.interp(length, [20, 150], [self.minVol, self.maxVol])
        self.volume.SetMasterVolumeLevel(volume, None)

    def highlight_volume_control(self, img, length, thumb, index):
        center = ((thumb[1] + index[1]) // 2, (thumb[2] + index[2]) // 2)
        if length < 20:
            cv2.circle(img, center, 12, (0, 255, 0), cv2.FILLED)
        elif length > 150:
            cv2.circle(img, center, 12, (0, 0, 255), cv2.FILLED)
        return img

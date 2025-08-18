import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    frame, ret = cap.read()
    if not ret:
        break
    
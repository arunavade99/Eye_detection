import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    cv2.imshow('Eye Controlled Mouse', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
  
cap.release()
cv2.destroyAllWindows()
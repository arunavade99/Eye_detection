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
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks #landmarks of face
    frame_h, frame_w, ret = frame.shape
    if landmark_points:
        landmarks = landmark_points[0].landmark
        # Left eye full landmarks
        left_eye_indices = [33, 7, 163, 144, 145, 153, 154, 155, 133, 246, 161, 160, 159, 158, 157, 173]
        left_eye = [landmarks[i] for i in left_eye_indices]
        for landmark in left_eye:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        # Right eye full landmarks
        right_eye_indices = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
        right_eye = [landmarks[i] for i in right_eye_indices]
        for landmark in right_eye:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 0, 255))
    
    cv2.imshow('Eye Movenment Controller', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
  
cap.release()
cv2.destroyAllWindows()
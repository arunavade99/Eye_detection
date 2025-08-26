import cv2
import mediapipe as mp
import pyautogui

def draw_virtual_bounding_box(frame):
    frame_h, frame_w = frame.shape[:2]
    box_w = int(frame_w * 0.8)
    box_h = int(frame_h * 0.8)
    box_x1 = int((frame_w - box_w) / 2)
    box_y1 = int((frame_h - box_h) / 2)
    box_x2 = box_x1 + box_w
    box_y2 = box_y1 + box_h
    cv2.rectangle(frame, (box_x1, box_y1), (box_x2, box_y2), (255, 0, 0), 2)
    return frame, (box_x1, box_y1, box_x2, box_y2)

cap = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame, (box_x1, box_y1, box_x2, box_y2) = draw_virtual_bounding_box(frame)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks #landmarks of face
    frame_h, frame_w, ret = frame.shape
    if landmark_points:
        # Draw a simple bounding box over the detected face
        face_landmarks = landmark_points[0]
        xs = [lm.x for lm in face_landmarks.landmark]
        ys = [lm.y for lm in face_landmarks.landmark]
        min_x = int(min(xs) * frame_w)
        max_x = int(max(xs) * frame_w)
        min_y = int(min(ys) * frame_h)
        max_y = int(max(ys) * frame_h)
        cv2.rectangle(frame, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)

        landmarks = landmark_points[0].landmark
        # Left eyeball (pupil)
        left_pupil = landmarks[468]
        x = int(left_pupil.x * frame_w)
        y = int(left_pupil.y * frame_h)
        cv2.circle(frame, (x, y), 6, (0, 255, 255), -1)
        # Alert if left pupil is outside bounding box
        if x < box_x1 or x > box_x2 or y < box_y1 or y > box_y2:
            cv2.putText(frame, 'ALERT: Eye Out of Box!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        # Right eyeball (pupil)
        right_pupil = landmarks[473]
        x = int(right_pupil.x * frame_w)
        y = int(right_pupil.y * frame_h)
        cv2.circle(frame, (x, y), 6, (0, 0, 255), -1)
        # Alert if right pupil is outside bounding box
        if x < box_x1 or x > box_x2 or y < box_y1 or y > box_y2:
            cv2.putText(frame, 'ALERT: Eye Out of Box!', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        
    cv2.imshow('Eye Movenment Controller', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
  
cap.release()
cv2.destroyAllWindows()
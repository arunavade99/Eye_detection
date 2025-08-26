import cv2
import mediapipe as mp

def initialize_face_mesh():
    return mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

def detect_eye_movement(frame, face_mesh, bounding_box):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks

    if landmark_points:
        landmarks = landmark_points[0].landmark
        left_eye_landmarks = [landmarks[145], landmarks[159]]  # Left eye landmarks
        right_eye_landmarks = [landmarks[374], landmarks[386]]  # Right eye landmarks

        eye_positions = []
        for landmark in left_eye_landmarks + right_eye_landmarks:
            x = int(landmark.x * frame.shape[1])
            y = int(landmark.y * frame.shape[0])
            eye_positions.append((x, y))

        if is_eye_moving_outside_bounding_box(eye_positions, bounding_box):
            return True  # Eye movement detected outside the bounding box

    return False  # No significant eye movement detected

def is_eye_moving_outside_bounding_box(eye_positions, bounding_box):
    for (x, y) in eye_positions:
        if not (bounding_box[0] <= x <= bounding_box[2] and bounding_box[1] <= y <= bounding_box[3]):
            return True
    return False
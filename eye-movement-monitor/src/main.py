import cv2
import mediapipe as mp
from utils.detection import detect_eye_movement
from config.settings import BOUNDING_BOX, SENSITIVITY

def main():
    cap = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)

        if output.multi_face_landmarks:
            landmarks = output.multi_face_landmarks[0].landmark
            eye_movement_detected = detect_eye_movement(landmarks, BOUNDING_BOX, SENSITIVITY)

            if eye_movement_detected:
                cv2.putText(frame, "Eye movement detected!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.rectangle(frame, (BOUNDING_BOX[0], BOUNDING_BOX[1]), (BOUNDING_BOX[2], BOUNDING_BOX[3]), (0, 255, 0), 2)
        cv2.imshow('Eye Movement Monitor', frame)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
import cv2
import mediapipe as mp

from utils.eye_landmarks import get_eye_points
from utils.gaze_estimator import estimate_gaze
from utils.visualization import draw_gaze

mp_face_mesh = mp.solutions.face_mesh

cap = cv2.VideoCapture(0)

with mp_face_mesh.FaceMesh(
        max_num_faces=1,
        refine_landmarks=True) as face_mesh:

    while True:
        success, frame = cap.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        gaze_direction = "No Face"

        if results.multi_face_landmarks:
            landmarks = results.multi_face_landmarks[0]

            eye_data = get_eye_points(frame, landmarks)

            gaze_direction = estimate_gaze(eye_data)

            draw_gaze(frame, gaze_direction)

        cv2.imshow("Eye Gaze Direction", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()

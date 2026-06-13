import cv2


def draw_gaze(frame, gaze):

    cv2.putText(
        frame,
        f"Gaze: {gaze}",
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

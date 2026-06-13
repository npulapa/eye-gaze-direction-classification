def get_eye_points(frame, landmarks):

    h, w, _ = frame.shape

    # Left eye corners
    left_corner = landmarks.landmark[33]
    right_corner = landmarks.landmark[133]

    # Upper and lower eyelid
    upper_lid = landmarks.landmark[159]
    lower_lid = landmarks.landmark[145]

    # Iris center
    iris = landmarks.landmark[468]

    data = {
        "left_x": int(left_corner.x * w),
        "right_x": int(right_corner.x * w),
        "upper_y": int(upper_lid.y * h),
        "lower_y": int(lower_lid.y * h),
        "iris_x": int(iris.x * w),
        "iris_y": int(iris.y * h)
    }

    return data

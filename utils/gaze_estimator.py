def estimate_gaze(data):

    left_x = data["left_x"]
    right_x = data["right_x"]
    iris_x = data["iris_x"]

    upper_y = data["upper_y"]
    lower_y = data["lower_y"]
    iris_y = data["iris_y"]

    # Horizontal ratio
    ratio_x = (iris_x - left_x) / (right_x - left_x)

    # Vertical ratio
    ratio_y = (iris_y - upper_y) / (lower_y - upper_y)

    if ratio_y < 0.35:
        return "UP"

    if ratio_x < 0.35:
        return "LEFT"

    elif ratio_x > 0.65:
        return "RIGHT"

    else:
        return "CENTER"

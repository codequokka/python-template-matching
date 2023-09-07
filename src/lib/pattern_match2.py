import cv2


def pattern_match(image_path: str, template_path: str) -> None:
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)
    image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template_gs = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(image_gs, template_gs, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_val, max_val, min_loc, max_loc)

    w, h, _ = template.shape
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)

    cv2.imwrite("src/results/result.jpg", image)

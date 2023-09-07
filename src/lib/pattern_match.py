import cv2


def pattern_match(image_path: str, template_path: str) -> None:
    image = cv2.imread(image_path)
    template = cv2.imread(template_path)

    w, h, _ = template.shape

    result = cv2.matchTemplate(image, template, cv2.TM_CCORR_NORMED)

    # 検索結果の信頼度と位置座標の取得
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    print(min_val, max_val, min_loc, max_loc)

    # 検索結果の左上頂点の座標を取得
    top_left = max_loc

    # 検索結果の右下頂点の座標を取""
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 検索対象画像内に、検索結果を長方形で描画
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)

    cv2.imwrite("src/results/result.jpg", image)

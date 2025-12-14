# project3_shape_color_detective.py
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Webcam not opened.")
    raise SystemExit

# HSV range for a "bright green" object (you might need to tweak)
lower = np.array([35, 80, 60])
upper = np.array([85, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)

    # clean noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=1)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    best = None
    best_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 700:  # filter tiny detections
            continue
        if area > best_area:
            best_area = area
            best = cnt

    out = frame.copy()

    if best is not None:
        x, y, w, h = cv2.boundingRect(best)
        cv2.rectangle(out, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # bonus: shape guess (very basic)
        peri = cv2.arcLength(best, True)
        approx = cv2.approxPolyDP(best, 0.03 * peri, True)
        corners = len(approx)

        if corners == 3:
            shp = "triangle"
        elif corners == 4:
            shp = "quad"
        elif corners > 4:
            shp = "circle-ish"
        else:
            shp = "unknown"

        cv2.putText(out, f"area={int(best_area)} shape={shp}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.drawContours(out, [best], -1, (255, 0, 0), 2)

    cv2.imshow("mask", mask)
    cv2.imshow("detective", out)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

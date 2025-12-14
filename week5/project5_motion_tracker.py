# project5_motion_tracker.py
import cv2
import numpy as np
from collections import deque

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Webcam not opened.")
    raise SystemExit

bg = cv2.createBackgroundSubtractorMOG2(history=400, varThreshold=30, detectShadows=True)

trail = deque(maxlen=40)

# security zone (middle rectangle)
zone = None
alert_on = False

kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]
    if zone is None:
        zone = (w//3, h//3, w//3, h//3)  # x,y,zw,zh

    fg = bg.apply(frame)

    # clean up
    fg = cv2.medianBlur(fg, 5)
    fg = cv2.erode(fg, kernel, iterations=1)
    fg = cv2.dilate(fg, kernel, iterations=2)

    contours, _ = cv2.findContours(fg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    best = None
    best_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 800:
            continue
        if area > best_area:
            best_area = area
            best = cnt

    out = frame.copy()

    zx, zy, zw, zh = zone
    cv2.rectangle(out, (zx, zy), (zx+zw, zy+zh), (255, 255, 255), 2)

    alert_on = False

    if best is not None:
        x, y, ww, hh = cv2.boundingRect(best)
        cv2.rectangle(out, (x, y), (x+ww, y+hh), (0, 0, 255), 2)

        cx = x + ww // 2
        cy = y + hh // 2
        trail.appendleft((cx, cy))

        # zone check (simple)
        if zx <= cx <= zx+zw and zy <= cy <= zy+zh:
            alert_on = True

    # draw trail
    for i in range(1, len(trail)):
        if trail[i-1] is None or trail[i] is None:
            continue
        cv2.line(out, trail[i-1], trail[i], (0, 255, 0), 2)

    if alert_on:
        cv2.putText(out, "ALERT: movement in zone!", (15, 35),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)

    cv2.imshow("fgmask", fg)
    cv2.imshow("motion tracker", out)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

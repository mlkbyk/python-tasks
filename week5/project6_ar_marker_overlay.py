# project6_ar_marker_overlay.py
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Webcam not opened.")
    raise SystemExit

# Virtual content (an image) to place on top of marker
overlay_path = "overlay.png"  # put a small logo/image here
overlay = cv2.imread(overlay_path)
if overlay is None:
    # fallback: make a simple overlay if file missing
    overlay = np.zeros((240, 320, 3), dtype=np.uint8)
    cv2.putText(overlay, "AR", (90, 140), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)

oh, ow = overlay.shape[:2]

# Detect a colored marker paper (example: blue-ish)
lower = np.array([95, 80, 60])
upper = np.array([130, 255, 255])

def order_points(pts):
    # pts: 4x2
    pts = np.array(pts, dtype=np.float32)
    s = pts.sum(axis=1)
    diff = np.diff(pts, axis=1).reshape(-1)
    tl = pts[np.argmin(s)]
    br = pts[np.argmax(s)]
    tr = pts[np.argmin(diff)]
    bl = pts[np.argmax(diff)]
    return np.array([tl, tr, br, bl], dtype=np.float32)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    out = frame.copy()

    # find a quadrilateral marker
    marker_quad = None
    best_area = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 3000:
            continue
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.03 * peri, True)
        if len(approx) == 4 and area > best_area:
            best_area = area
            marker_quad = approx.reshape(4, 2)

    if marker_quad is not None:
        pts_dst = order_points(marker_quad)

        # source points are overlay corners
        pts_src = np.array([[0, 0], [ow - 1, 0], [ow - 1, oh - 1], [0, oh - 1]], dtype=np.float32)

        H, _ = cv2.findHomography(pts_src, pts_dst)
        warped = cv2.warpPerspective(overlay, H, (out.shape[1], out.shape[0]))

        # create mask from warped overlay (non-black)
        warped_gray = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
        _, warped_mask = cv2.threshold(warped_gray, 1, 255, cv2.THRESH_BINARY)

        inv = cv2.bitwise_not(warped_mask)

        bg_part = cv2.bitwise_and(out, out, mask=inv)
        fg_part = cv2.bitwise_and(warped, warped, mask=warped_mask)
        out = cv2.add(bg_part, fg_part)

        # draw marker outline
        cv2.polylines(out, [pts_dst.astype(np.int32)], True, (0, 255, 0), 3)

    cv2.imshow("mask", mask)
    cv2.imshow("AR marker", out)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# project4_smart_selfie_app.py
import cv2

# For many installs this works; if not, give the full path to haarcascade_frontalface_default.xml
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Webcam not opened.")
    raise SystemExit

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60)
    )

    out = frame.copy()

    # count faces
    cv2.putText(out, f"faces: {len(faces)}", (15, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)

    for (x, y, w, h) in faces:
        # privacy blur
        roi = out[y:y+h, x:x+w]
        if roi.size != 0:
            blur = cv2.GaussianBlur(roi, (35, 35), 0)
            out[y:y+h, x:x+w] = blur

        # "glasses" (simple rectangles, not perfect but okay)
        gy = y + int(h * 0.38)
        gh = int(h * 0.18)
        g1x1 = x + int(w * 0.10)
        g1x2 = x + int(w * 0.45)
        g2x1 = x + int(w * 0.55)
        g2x2 = x + int(w * 0.90)

        cv2.rectangle(out, (g1x1, gy), (g1x2, gy + gh), (0, 0, 0), 3)
        cv2.rectangle(out, (g2x1, gy), (g2x2, gy + gh), (0, 0, 0), 3)
        cv2.line(out, (g1x2, gy + gh//2), (g2x1, gy + gh//2), (0, 0, 0), 3)

    cv2.imshow("smart selfie", out)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

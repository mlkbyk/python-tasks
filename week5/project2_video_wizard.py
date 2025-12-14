# project2_video_wizard.py
import cv2

# 1) webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Webcam not opened.")
    raise SystemExit

drawing = False
last_pt = None

def mouse_cb(event, x, y, flags, param):
    global drawing, last_pt
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_pt = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        # draw as you move (paint)
        cv2.line(param, last_pt, (x, y), (0, 255, 0), 3)
        last_pt = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        last_pt = None

cv2.namedWindow("webcam")
frame_for_draw = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # keep a draw layer on top of current frame
    if frame_for_draw is None:
        frame_for_draw = frame.copy()

    # blend a bit so it doesn't look too harsh
    show = cv2.addWeighted(frame, 0.8, frame_for_draw, 0.2, 0)

    # shapes + text
    cv2.rectangle(show, (20, 20), (180, 80), (255, 0, 0), 2)
    cv2.circle(show, (260, 50), 25, (0, 0, 255), 2)
    cv2.putText(show, "Press s to save, q to quit", (10, show.shape[0] - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.setMouseCallback("webcam", mouse_cb, frame_for_draw)
    cv2.imshow("webcam", show)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("s"):
        cv2.imwrite("screenshot.png", frame)
        print("Saved screenshot.png")
    if key == ord("c"):
        frame_for_draw = frame.copy()  # clear drawing
        print("Cleared drawing")
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# 2) play a video file (optional)
# If you want: uncomment and set path
"""
video_path = "video.mp4"
cap2 = cv2.VideoCapture(video_path)
while True:
    ret, fr = cap2.read()
    if not ret:
        break
    cv2.imshow("video", fr)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
cap2.release()
cv2.destroyAllWindows()
"""

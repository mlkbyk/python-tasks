# project1_digital_darkroom.py
import cv2
import numpy as np

img_path = "image.jpg"  # put your image file here
img = cv2.imread(img_path)

if img is None:
    print("Could not read image. Check the path:", img_path)
    raise SystemExit

h, w, c = img.shape
print("shape (H,W,C):", img.shape)
print("height:", h, "width:", w, "channels:", c)

cv2.imshow("original", img)

# split channels
b, g, r = cv2.split(img)
cv2.imshow("blue channel", b)
cv2.imshow("green channel", g)
cv2.imshow("red channel", r)

# swap R and B (BGR -> RGB-like)
swapped = cv2.merge([r, g, b])
cv2.imshow("channel swapped (R<->B)", swapped)

# crop (center crop)
cy, cx = h // 2, w // 2
crop = img[max(0, cy - 150): min(h, cy + 150), max(0, cx - 200): min(w, cx + 200)]
cv2.imshow("crop", crop)

# resize
resized = cv2.resize(img, (w // 2, h // 2))
cv2.imshow("resized", resized)

# grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)

# warm filter (simple)
warm = img.copy().astype(np.float32)
warm[:, :, 2] *= 1.15  # R up
warm[:, :, 0] *= 0.90  # B down
warm = np.clip(warm, 0, 255).astype(np.uint8)
cv2.imshow("warm", warm)

# vintage-ish (low contrast + sepia-ish)
v = img.copy().astype(np.float32)
v = v * 0.9 + 10
sepia = np.array([[0.272, 0.534, 0.131],
                  [0.349, 0.686, 0.168],
                  [0.393, 0.769, 0.189]], dtype=np.float32)
v = cv2.transform(v, sepia)
v = np.clip(v, 0, 255).astype(np.uint8)
cv2.imshow("vintage", v)

print("Press any key to close windows...")
cv2.waitKey(0)
cv2.destroyAllWindows()

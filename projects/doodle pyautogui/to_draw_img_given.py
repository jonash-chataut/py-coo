import pyautogui
import cv2
import numpy as np
import time
import os

# ====== SETTINGS ======
img_path = r"C:\skills\python\projects\doodle pyautogui\dog.webp"  # your image path
canvas_x, canvas_y = 600, 400  # top-left corner of Paint canvas
skip_pixels = 5                 # smaller = more detail, slower
move_duration = 0.001           # mouse movement speed

# ====== LOAD IMAGE ======
if not os.path.exists(img_path):
    raise FileNotFoundError(f"Image not found at {img_path}")

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
if img is None:
    raise ValueError("Failed to load image. Use PNG/JPG format.")

img = cv2.resize(img, (400, 400))
edges = cv2.Canny(img, 100, 200)
edges = cv2.bitwise_not(edges)  # invert so lines are black

points = np.column_stack(np.where(edges > 0))

# ====== DRAWING ======
print("Switch to Paint and make sure the Pencil tool is selected. Drawing starts in 5 seconds...")
time.sleep(5)

# Optional: click inside Paint to activate Pencil tool
pyautogui.click(canvas_x, canvas_y)

# Start holding click to draw
pyautogui.mouseDown()

# Move along all edge points
for (y, x) in points[::skip_pixels]:
    pyautogui.moveTo(canvas_x + x, canvas_y + y, duration=move_duration)

# Release mouse after drawing
pyautogui.mouseUp()

print("✅ Drawing complete!")

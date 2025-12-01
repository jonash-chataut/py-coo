import cv2

image = cv2.imread("learnings\libraries learning\OpenCV\basics\py_img.jpg")

if image is None:
    print("Error: Image not found")
else:
    print("Image loaded successfully")


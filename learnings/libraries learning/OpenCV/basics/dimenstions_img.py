import cv2

image = cv2.imread("learnings\libraries learning\OpenCV\py_img.jpg")

if image is not None:
    h,w,c = image.shape
    print(f"Height: {h}\n Width: {w} \n Channels: {c} ")
else:
    print("Could not load image")
    
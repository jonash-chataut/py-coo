import cv2

image = cv2.imread(r"learnings\libraries learning\OpenCV\basics\py_img.jpg")

if image is not None:
    h,w,c = image.shape
    print(f"Height: {h}\n Width: {w} \n Channels: {c} ")
else:
    print("Could not load image")
    
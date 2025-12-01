import cv2

image = cv2.imread("learnings\libraries learning\OpenCV\py_img.jpg")

if image is not None:
    success = cv2.imwrite("Output_python.png",image)
    if success:
        print("Image saved successfully")
    else:
        print("Failed to save")
else:
    print("Error: Could not load image")



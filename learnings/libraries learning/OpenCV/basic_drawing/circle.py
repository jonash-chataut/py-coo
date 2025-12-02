import cv2

image = cv2.imread(r"learnings\libraries learning\OpenCV\basics\py_img.jpg")

if image is None:
    print("Could not load image")
else:
    print("Img loaded successfully")

    color=(0,0,255)
    thickness=4

    cv2.circle(image,(200,200), 100,color,thickness)
    cv2.imshow("Cicle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    




    
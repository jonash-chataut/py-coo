import cv2

image = cv2.imread(r"learnings\libraries learning\OpenCV\basics\py_img.jpg")

if image is None:
    print("Could not load image")
else:
    print("Img loaded successfully")
    pt1=(100,100) #top left
    pt2=(800,450) #bottom right

    color=(0,255,0) #bgr
    thickness=7

    cv2.rectangle(image,pt1,pt2,color,thickness)
    cv2.imshow("Rectangle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    




    
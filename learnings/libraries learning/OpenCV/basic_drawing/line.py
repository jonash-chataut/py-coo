import cv2

image = cv2.imread(r"learnings\libraries learning\OpenCV\basics\py_img.jpg")

if image is None:
    print("Could not load image")
else:
    print("Img loaded successfully")
    p1=(50,100)
    pt2=(300,150)

    color=(255,0,0)
    thickness=4

    cv2.line(image,p1,pt2,color,thickness)
    cv2.imshow("Line",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    




    
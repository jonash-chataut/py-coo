import cv2

image = cv2.imread(r"learnings\libraries learning\OpenCV\basics\py_img.jpg")

if image is None:
    print("Could not load image")
else:
    print("Img loaded successfully")
    cv2.putText(image,"Hello Python",(100,150),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,255,0),5)
    cv2.imshow("Text",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    




    
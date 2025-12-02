import cv2

image = cv2.imread(r"learnings\libraries learning\OpenCV\basics\py_img.jpg")

if image is not None:
    cropped = image[100:200,50:150] #y(y-axis) start to end, x(x-axis) start to end
    cv2.imshow("Cropped image",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    


    
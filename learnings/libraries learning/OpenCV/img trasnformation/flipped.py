import cv2

image = cv2.imread(r"learnings\libraries learning\OpenCV\basics\py_img.jpg")

if image is None:
    print("Could not load image")
else:
    flipped_horizontal=cv2.flip(image,1)
    flipped_vertical=cv2.flip(image,0)
    flipped_both=cv2.flip(image,-1)
    cv2.imshow("Original",image)
    cv2.imshow("flipped horizontal",flipped_horizontal)
    cv2.imshow("flipped vertical",flipped_vertical)
    cv2.imshow("flipped both",flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    



    
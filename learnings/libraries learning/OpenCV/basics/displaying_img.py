import cv2

image = cv2.imread(r"learnings\libraries learning\OpenCV\basics\py_img.jpg")

if image is not None:
    cv2.imshow("Image showing", image) #open the window
    cv2.waitKey(0) #wait for a key
    cv2.destroyAllWindows() #close the window
else:
   print("Error: Image not load" )


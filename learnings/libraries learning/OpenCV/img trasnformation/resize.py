import cv2

image = cv2.imread(r"learnings\libraries learning\OpenCV\basics\py_img.jpg")

if image is None:
    print("Image is not found")
else:
    print("Image found")
    resized = cv2.resize(image,(300,300))
    cv2.imshow("Original image",image)
    cv2.imshow("Resized image",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_output.png",resized)


    
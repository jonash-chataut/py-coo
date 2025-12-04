import cv2
image = cv2.imread(r"C:\skills\python\learnings\libraries learning\OpenCV\filtering and blurring\free-nature-images.jpg")
blurred= cv2.GaussianBlur(image,(9,9),1)

cv2.imshow("Original image",image)
cv2.imshow("blurred image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

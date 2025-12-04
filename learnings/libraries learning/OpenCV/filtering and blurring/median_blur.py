import cv2
image = cv2.imread(r"C:\skills\python\learnings\libraries learning\OpenCV\filtering and blurring\noisy_f.png")

blurred= cv2.medianBlur(image,11)

cv2.imshow("Original image",image)
cv2.imshow("blurred image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

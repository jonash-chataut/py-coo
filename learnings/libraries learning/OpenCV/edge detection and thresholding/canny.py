import cv2
 
img = cv2.imread(r"C:\skills\python\learnings\libraries learning\OpenCV\edge detection and thresholding\flower.png",cv2.IMREAD_GRAYSCALE)
  
edges=cv2.Canny(img,50,150)

cv2.imshow("Original Image",img)
cv2.imshow("Edges",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


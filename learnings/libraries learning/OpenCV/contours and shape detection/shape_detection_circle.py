import cv2

img=cv2.imread(r"C:\skills\python\learnings\libraries learning\OpenCV\contours and shape detection\circle.png")
gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_ , thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)

# find contours
contours, heirarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# to show all the edges detected by contours
cv2.drawContours(img,contours,-1,(0,255,0),3)

for contour in contours:
    apporx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)

    corners=len(apporx)

    if corners==3:
        shape_name="Triangle"
    elif corners==4:
        shape_name="Rectangle"
    elif corners==5:
        shape_name="Pentagon"
    elif corners==6:
        shape_name="Hexagon"
    elif corners>6:
        shape_name="Circle"
    else:
        shape_name="Unknown"

# to show the edges of approx
cv2.drawContours(img,[apporx],0,(0,255,0),2)
x=apporx.ravel()[0]
y=apporx.ravel()[1]-10
cv2.putText(img,shape_name,(x,y),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,0,0),1)

cv2.imshow("Contours",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

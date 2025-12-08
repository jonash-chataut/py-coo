import cv2
face_cascade=cv2.CascadeClassifier("C:\skills\python\learnings\libraries learning\OpenCV\Face and object detection\haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("C:\skills\python\learnings\libraries learning\OpenCV\Face and object detection\haarcascade_eye.xml")
smile_cascade=cv2.CascadeClassifier("C:\skills\python\learnings\libraries learning\OpenCV\Face and object detection\haarcascade_smile.xml")

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,10)

    for (x,y,w,h) in faces: #used for loop bcoz there can be multiple faces 
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    #roi=region of interest
    roi_gray=gray[y:y+h,x:x+w] #face lai matra leko
    roi_color=frame[y:y+h,x:x+w]
    
    eyes=eye_cascade.detectMultiScale(roi_gray,1.1,10)
    if len(eyes)>0:
        cv2.putText(frame,"Eyes Detected",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)

    smiles=smile_cascade.detectMultiScale(roi_gray,1.7,22)
    if len(smiles)>0:
        cv2.putText(frame,"Smiling",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)


    cv2.imshow("Smart face detection",frame)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

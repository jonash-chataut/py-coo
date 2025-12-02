import cv2
cap =  cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() #ret=true/false frame =image

    if not ret:
        print("Could not read frame")
        break
    cv2.imshow("Webcam feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # wait for 1 millisecond and q press gare close hunxa
        print("Quitting....")
        break
 
cap.release()
cv2.destroyAllWindows()


    

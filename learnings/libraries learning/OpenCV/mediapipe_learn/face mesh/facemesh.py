import cv2
import mediapipe as mp
import time

mpDraw=mp.solutions.drawing_utils
mpfaceMesh=mp.solutions.face_mesh
faceMesh=mpfaceMesh.FaceMesh(max_num_faces=2)
drawSpecs=mpDraw.DrawingSpec(thickness=1,circle_radius=1)


pTime=0
cap=cv2.VideoCapture(0)
# cap=cv2.VideoCapture("C:\skills\python\learnings\libraries learning\OpenCV\mediapipe_learn\pose_tracking\pose_videos\V2.mp4")

while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=faceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img,faceLms,mpfaceMesh.FACEMESH_CONTOURS,drawSpecs,drawSpecs)

            for id,lm in enumerate(faceLms.landmark):
                ih,iw,ic=img.shape
                x,y=int(lm.x*iw),int(lm.y*ih)
                

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),2)
    cv2.imshow("Face mesh",img)
    cv2.waitKey(1)
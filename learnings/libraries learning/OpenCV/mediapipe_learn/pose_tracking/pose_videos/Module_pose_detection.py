import cv2
import mediapipe as mp
import time

mpDraw=mp.solutions.drawing_utils
mpPose=mp.solutions.pose
pose=mpPose.Pose()


class poseDetector():
    def __init__(self,mode=False,upBody=False,smoothness=True,detectionCon=0.5,trackingCon=0.5):
        self.mode=mode
        self.upBody=upBody
        self.smoothness=smoothness
        self.detectionCon=detectionCon
        self.trackingCon=trackingCon
        self.mpDraw=mp.solutions.drawing_utils
        self.mpPose=mp.solutions.pose
        self.pose=self.mpPose.Pose(static_image_mode=self.mode,
            smooth_landmarks=self.smoothness,
            min_detection_confidence=self.detectionCon,
            min_tracking_confidence=self.trackingCon)

    def findPose(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
        return img
    
    def findPosition(self,img,draw=True):
        lmlist=[]
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h)
                lmlist.append([id,cx,cy])
                if draw:  
                    cv2.circle(img,(cx,cy),3,(255,0,0),cv2.FILLED)
        return lmlist    


def main():
    pTime=0
    cap=cv2.VideoCapture("C:\skills\python\learnings\libraries learning\OpenCV\mediapipe_learn\pose_tracking\pose_videos\V1.mp4")
    detector=poseDetector()
    
    while True:
        success,img=cap.read()
        img=detector.findPose(img)
        lmlist=detector.findPosition(img,draw=False)
        if len(lmlist) != 0:
            print(lmlist[14])
            cv2.circle(img,(lmlist[14][1],lmlist[14][2]),15,(0,0,255),cv2.FILLED)
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("Pose",img)
        cv2.waitKey(1)


if __name__=="__main__":
    main()

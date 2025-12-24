import cv2
import mediapipe as mp
import time

  
class faceDetector():
    def __init__(self,minDetectionCon=0.5):
       self.minDetectionCon=minDetectionCon
       self.mpDraw=mp.solutions.drawing_utils
       self.mpFaceDetection=mp.solutions.face_detection
       self.faceDetection=self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.faceDetection.process(imgRGB)
        bboxes=[]
        if self.results.detections:
            for id,detection in enumerate(self.results.detections):
                bboxC=detection.location_data.relative_bounding_box
                ih,iw,ic=img.shape
                bbox=int(bboxC.xmin*iw),int(bboxC.ymin*ih), int(bboxC.width*iw),int(bboxC.height*ih)

                bboxes.append([id,bbox,detection.score])
                if draw:
                    img=self.fancyDraw(img,bbox)
                # cv2.rectangle(img,bbox,(255,0,255),2)
                    cv2.putText(img,f"{int(detection.score[0]*100)}%",(bbox[0]-20,bbox[0]-20),cv2.FONT_HERSHEY_PLAIN,2,(255,0,255),2)

        return img,bboxes
    
    def fancyDraw(self,img,bbox,l=30,t=5,rt=1):
        x,y,w,h=bbox
        x1,y1=x+w,y+h   #diagonal points
        cv2.rectangle(img,bbox,(255,0,255),rt)
        # for top left corner thick i.e x,y
        cv2.line(img,(x,y),(x+l,y),(255,0,255),t)
        cv2.line(img,(x,y),(x,y+l),(255,0,255),t)

        # for top right corner i.e x1,y
        cv2.line(img,(x1,y),(x1-l,y),(255,0,255),t)
        cv2.line(img,(x1,y),(x1,y+l),(255,0,255),t)

        # for bottom left corner i.e x,y1
        cv2.line(img,(x,y1),(x+l,y1),(255,0,255),t)
        cv2.line(img,(x,y1),(x,y1-l),(255,0,255),t)

        # for bottom right corner i.e x1,y1
        cv2.line(img,(x1,y1),(x1-l,y1),(255,0,255),t)
        cv2.line(img,(x1,y1),(x1,y1-l),(255,0,255),t)


        return img


def main():
    pTime=0
    cap=cv2.VideoCapture(0)
    detector=faceDetector()
    while True: 
        success,img=cap.read()
        img,bboxes=detector.findFaces(img)
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),2)
        cv2.imshow("Face Detecton",img)
        cv2.waitKey(1)


if __name__=="__main__":
    main()
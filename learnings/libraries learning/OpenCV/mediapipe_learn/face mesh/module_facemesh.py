import cv2
import mediapipe as mp
import time



                
class faceMeshdectector:
    def __init__(self,staticMode=False,maxFaces=2,minDetectionCon=0.5,minTrackCon=0.5):
        self.staticMode=staticMode
        self.maxFaces=maxFaces
        self.minDetectionCon=minDetectionCon
        self.minTrackCon=minTrackCon
        self.mpDraw=mp.solutions.drawing_utils
        self.mpfaceMesh=mp.solutions.face_mesh
        self.faceMesh = self.mpfaceMesh.FaceMesh(
    static_image_mode=self.staticMode,
    max_num_faces=self.maxFaces,
    min_detection_confidence=self.minDetectionCon,
    min_tracking_confidence=self.minTrackCon
)

        self.drawSpecs=self.mpDraw.DrawingSpec(thickness=1,circle_radius=1)

    def findFaceMesh(self,img,draw=True):
        self.imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.faceMesh.process(self.imgRGB)

        if self.results.multi_face_landmarks:
            faces=[]
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,faceLms,self.mpfaceMesh.FACEMESH_CONTOURS,self.drawSpecs,self.drawSpecs)
                face=[]

                for id,lm in enumerate(faceLms.landmark):
                    ih,iw,ic=img.shape
                    x,y=int(lm.x*iw),int(lm.y*ih)
                    # cv2.putText(img,str(id),(x,y),cv2.FONT_HERSHEY_PLAIN,0.7,(0,255,0),1)
                    face.append([x,y])
                faces.append(face)
        return img,faces


def main():
    pTime=0
    # cap=cv2.VideoCapture(0)
    cap=cv2.VideoCapture(r"C:\skills\python\learnings\libraries learning\OpenCV\mediapipe_learn\face mesh\sample videos\vdo8.mp4")
    detector=faceMeshdectector()
    while True:
        success,img=cap.read()
        img,faces=detector.findFaceMesh(img)
        if len(faces)!=0:
            print(len(faces))
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),2)
        cv2.imshow("Face mesh",img)
        cv2.waitKey(1)


if __name__=="__main__":
    main()
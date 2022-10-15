import cv2
import time
import math
xs = []
ys = []
video = cv2.VideoCapture("C:/Users/JISHNU D/Downloads/PRO-120-Project/C120-Project/footvolleyball.mp4")
#load tracker 
tracker = cv2.TrackerCSRT_create()

#read the first frame of the video
success,img = video.read()

#selct the bounding box on the image
bbox = cv2.selectROI("Track",img,False)

#initialise the tracker on the img and the bounding box
tracker.init(img,bbox)
print(bbox)

def goal_track(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1 = x + int(w/2)
    c2 = y + int(h/2)
    cv2.circle(img,(c1,c2),2,(0,0,255),5)
    xs.append(c1)
    ys.append(c2)
    for i in range(len(xs)-1):
       cv2.circle(img,(xs[i],ys[i]),2,(0,0,255),5)

def drawBox(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1)
    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)


while True:
    check,img = video.read()   
    success,bbox = tracker.update(img)

    if success:
        txt = f"{bbox[0]}, {bbox[1]}"
        cv2.putText(img,txt,(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)   
        drawBox(img,bbox)
    else:
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)

    goal_track(img,bbox)
    cv2.imshow("result",img)
            
    key = cv2.waitKey(50)
    if key == 32:
        print("Closing")
        break

video.release()
cv2.destroyALLwindows() 
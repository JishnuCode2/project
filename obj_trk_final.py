import math
#Activity 1
#declare p1 and p2
p1 = 
p2 = 
p1 = 579
p2 = 320

xs = []
ys = []
@@ -21,29 +21,24 @@

#initialise the tracker on the img and the bounding box
tracker.init(img,bbox)

def goal_track(img,bbox):
    x,y,w,h = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1 = x + int(w/2)
    c2 = y + int(h/2)

    #Activity 2
    #Uncomment the correct code 
    #cv2.circle(img,(c1,c2),2,(0,0,255),5)
    #cv2.circle(img,(c2,c1),2,(0,5,255),0)
    #cv2.circle(img,(c2,c1),2,(0,0,255),5)
    #cv2.circle(img,(c1,c2),2,(0,5,255),0)
    cv2.circle(img,(c1,c2),2,(0,0,255),5)

    cv2.circle(img,(int(p1),int(p2)),2,(0,255,0),3)
    cv2.circle(img,(int(p1),int(p2)),3,(0,255,0),3)
    dist = math.sqrt(((c1-p1)**2) + (c2-p2)**2)
    print(dist)

    if(dist<=20):
    if(dist<=50):
        cv2.putText(img,"Goal",(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)

    xs.append(c1)
    ys.append(c2)

    for i in range(len(xs)-1):
        cv2.circle(img,(xs[i],ys[i]),2,(0,0,255),5)

@@ -64,7 +59,7 @@ def drawBox(img,bbox):

    #Activity 3
    #call the function to track the goal

    goal_track(img,bbox)
    cv2.imshow("result",img)

    key = cv2.waitKey(1)
@@ -73,4 +68,4 @@ def drawBox(img,bbox):
        break

video.release()
cv2.destroyALLwindows() 
cv2.destroyALLwindows() 

import cv2
import os

width,height=1280,720
folderPath="presentation"


cap=cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

#get the list of presentation images
pathImages=sorted(os.listdir(folderPath),key=len)
print(pathImages)
#variables
imgnumber=4
hs,ws=int(120*1),int(213*1)  #dimensions of the smaller webcam img
while True:
    success,img=cap.read()
    pathFullImage=os.path.join(folderPath,pathImages[imgnumber])
    imgCurrent=cv2.imread(pathFullImage)

    #Adding webcam in the ppt display
    imgsmall=cv2.resize(img,(ws,hs))
    h,w,_=imgCurrent.shape
    imgCurrent[0:hs,w-ws:w]=imgsmall

    cv2.imshow("Image",img)
    cv2.imshow("Slides",imgCurrent)
    key=cv2.waitKey(1)
    if key==ord("v"):
        break


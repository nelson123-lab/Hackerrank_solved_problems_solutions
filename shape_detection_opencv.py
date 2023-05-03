import cv2
import numpy as np

def getcontours(img):
    countours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in countours:
        area = cv2.contourArea(cnt)
        print(area)
        cv2.drawContours(img_contours,cnt,-1,(255,0,0),2)
        per1 = cv2.arcLength(cnt,True)
        print(per1)
        approx = cv2.approxPolyDP(cnt, 0.02*per1,True)
        print(len(approx))
        objCor= len(approx)
        x, y, w, h = cv2.boundingRect(approx)

        if objCor ==3: objectType = "Tri"
        else: objectType = "None"

        cv2.rectangle(img_contours, (x,y), (x+w,y+h),(0,255,0),2)
        cv2.putText(img_contours,objectType,
                    (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,
                    (0,0,0),2)
path = "C://Users//NELSON JOSEPH//Desktop//blaze-athletics.png"
img = cv2.imread(path)
img_contours = img.copy()
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_grey, (7,7),1)
imgCanny = cv2.Canny(img_blur,50,50)
getcontours(imgCanny)
hor_img = np.hstack((img, img_contours))
hor_img2 = np.hstack((img_blur, imgCanny))
cv2.imshow("image2", hor_img2)
cv2.imshow("stacked image", hor_img)
cv2.waitKey(0)

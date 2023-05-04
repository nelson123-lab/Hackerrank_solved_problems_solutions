import cv2
import numpy as np

def empty(j):
    pass


cv2.namedWindow("Trackbar")
cv2.resizeWindow("Trackbar",640,240)
cv2.createTrackbar("Hue Mn","Trackbar",32,179,empty)
cv2.createTrackbar("Hue Mx","Trackbar",42,179,empty)
cv2.createTrackbar("sat Mn","Trackbar",15,255,empty)
cv2.createTrackbar("sat Mx","Trackbar",255,255,empty)
cv2.createTrackbar("val Mn","Trackbar",158,179,empty)
cv2.createTrackbar("val Mx","Trackbar",255,255,empty)
while True:
    img = cv2.imread("C://Users//NELSON JOSEPH//Desktop//note_book.jpeg")
    img_res = cv2.resize(img, (300, 600))
    imghsv = cv2.cvtColor(img_res,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Mn","Trackbar")
    h_max = cv2.getTrackbarPos("Hue Mx", "Trackbar")
    s_min = cv2.getTrackbarPos("sat Mn", "Trackbar")
    s_max = cv2.getTrackbarPos("sat Mx", "Trackbar")
    v_min = cv2.getTrackbarPos("val Mn", "Trackbar")
    v_max = cv2.getTrackbarPos("val Mx", "Trackbar")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max, v_max])
    mask = cv2.inRange(imghsv,lower,upper)
    imgResult = cv2.bitwise_and(img_res,img_res,mask=mask)
    h_stack = np.hstack((img_res,imgResult))

    #cv2.imshow("original",img_res)
   # cv2.imshow("HSV ", imghsv)
    #cv2.imshow("mask", mask)
    #cv2.imshow("result",imgResult)
    cv2.imshow("combination",h_stack)
    cv2.waitKey(1)

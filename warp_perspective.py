import cv2
import numpy as np

img = cv2.imread("C://Users//NELSON JOSEPH//Desktop//cards.jpg")

width,height = 250,350
pts1 = np.float32([[250,122],[398,154],[346,392],[198,363]])
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgoutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("image", img)
cv2.imshow("output",imgoutput)
cv2.waitKey(0)

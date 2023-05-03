# import cv2
# import matplotlib.pyplot as plt

# # Reading the image file
# path = 'C:/Users/NELSON JOSEPH/Desktop/'
# img = cv2.imread(path + 'blaze-athletics.png')

# # Applying canny transformation
# edges = cv2.Canny(img, 100, 200, 3, L2gradient=True)

# # Visualization
# plt.figure()
# plt.title('Blaze Logo')
# plt.imsave(path + 'Blaze Logo.png', edges, cmap='gray', format='png')
# plt.imshow(edges, cmap='gray')
# plt.show()

import cv2
import numpy as np

# this function is needed for the createTrackbar step downstream
def nothing(x):
    pass

# read the experimental image
path = 'C:/Users/NELSON JOSEPH/Desktop/'
img = cv2.imread(path + 'blaze-athletics.png', 0)
img_contours = img.copy()
# create trackbar for canny edge detection threshold changes
cv2.namedWindow('canny')

# add ON/OFF switch to "canny"
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'canny', 0, 1, nothing)

# add lower and upper threshold slidebars to "canny"
cv2.createTrackbar('lower', 'canny', 0, 255, nothing)
cv2.createTrackbar('upper', 'canny', 0, 255, nothing)

# Infinite loop until we hit the escape key on keyboard
while(1):

    # get current positions of four trackbars
    lower = cv2.getTrackbarPos('lower', 'canny')
    upper = cv2.getTrackbarPos('upper', 'canny')
    s = cv2.getTrackbarPos(switch, 'canny')

    if s == 0:
        edges = img
    else:
        edges = cv2.Canny(img, lower, upper, L2gradient=True)

    # display images
    hor_img = np.hstack((img, edges))
    cv2.imshow('Original and canny', hor_img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:   # hit escape to quit
        break

cv2.destroyAllWindows()
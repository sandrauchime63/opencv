import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img1=cv.imread('1112670651724157450.jpeg')
img2=cv.imread('img2.jpeg')
assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"
'''
def nothing(x):
    pass
img=np.zeros((300, 512, 3), dtype=np.uint8)
cv.namedWindow('image')
cv.createTrackbar('R', 'image', 0, 255, lambda x: None)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)
switch='1:ON \n0:OFF'
cv.createTrackbar(switch, 'image', 0, 1, lambda c: None)
while True:
    cv.imshow('image', img)
    k=cv.waitKey(1) & 0xFF
    if k==27:
        break
    r=cv.getTrackbarPos('R', 'image')
    g=cv.getTrackbarPos('G', 'image')
    b=cv.getTrackbarPos('B', 'image')
    s=cv.getTrackbarPos(switch, 'image')
    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]
cv.destroyAllWindows()
'''
"""
import cv2 as cv
events = [i for i in dir(cv) if 'EVENT' in i]
print( events )
"""
'''

import numpy as np
import cv2 as cv

## mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),100,(255,0,0),-1)

## Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle)

while(1):
    cv.imshow('image',img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
'''
"""
# img = cv.imread('1112670651724157450.jpeg')
#assert img is not None, "file could not be read, check with os.path.exists()"
#px=img[100, 100]
#cv.imshow('image', img)
#cv.waitKey(0)
#cv.detroyAllWindows()
#print(img.shape)
#print(img.size)
#ball = img[280:340, 330:390]
#print(ball.shape)
#####splitting the image 
#b,g,r=cv.split(img)
##  OR
r=img[:,:,0]
"""

#new_img2=cv.resize(img2, (img1.shape[1], img1.shape[0]))
#blend=cv.addWeighted(img1, 0.5, new_img2, 0.8, 0)
#part=img1[440:500, 490:550]
#img1[284:344, 100:160]=part
"""
img1 = cv.imread('blended_image.jpg')
assert img1 is not None, "file could not be read, check with os.path.exists()"

e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()

print(cv.useOptimized())
"""
"""
cap=cv.VideoCapture(0)
if not cap.isOpened():
    print("camera not opened successfully.")
while True:
    ret, frame=cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
    hsv=cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])

    # Second red range
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    # Detect pixels in each red range
    mask1 = cv.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv.inRange(hsv, lower_red2, upper_red2)

    # Combine both red masks
    mask = cv.bitwise_or(mask1, mask2)
    res=cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("my live feed", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)

    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
"""

"""
shape=cv.resize(img1, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

while True:
    cv.imshow('resized image', shape)
    cv.imshow('normal', img1)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break

cv.destroyAllWindows()
"""
"""
live=cv.VideoCapture(0)
if not live.isOpened():
    print('could not open webcam')
while True:
    ret, frame=live.read()
    if not ret:
        print('could not read frame')
        break
    blurred_frame = cv.GaussianBlur(frame, (15, 15), 0)
    #cv.imshow('blurred', blurred_frame)
    hsv=cv.cvtColor(blurred_frame, cv.COLOR_BGR2HSV)
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])
    
    
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    mask1 = cv.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv.inRange(hsv, lower_red2, upper_red2)
    mask = cv.bitwise_or(mask1, mask2)
    res=cv.bitwise_and(blurred_frame, blurred_frame, mask=mask)
    
    cv.imshow('live', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
cv.destroyAllWindows()


"""
"""
laplacian=cv.laplacian(img1, cv.CV_64F)
sobelx=cv.Sobel(img1, cv.CV_64F, 1, 0, ksize=5)
sobely=cv.Sobel(img1, cv.CV_64F, 0, 1, ksize=5)
plt.subplot(2,2,1),plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian')
plt.subplot(2,2,2),plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X')
plt.subplot(2,2,3),plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y')
plt.show()
"""
"""
blur=cv.GaussianBlur(img1, (5, 5), 0)
canny=cv.Canny(blur, 50, 150)
while True:
    cv.imshow("blurred", blur)
    cv.imshow("canny", canny)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.DestroyAllWindows()
"""




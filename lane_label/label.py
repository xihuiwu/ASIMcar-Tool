import glob
import os
import cv2

if not os.path.exists('label'):
    os.mkdir('label')

white_low = cv2.Scalar(0,0,0)
white_high = cv2.Scalar(0,0,255)
yellow_low = cv2.Scalar(20,100,100)
yellow_high = cv2.Scalar(30,255,255)

path = "data\\*.jpg"
for file in glob.glob(path):
    raw = cv2.imread(file)
    hsv = cv2.cvtColor(raw, cv2.COLOR_BGR2HSV)
    white_mask = cv2.inRange(hsv, white_low, white_high)
    yellow_mask = cv2.inRange(hsv, yellow_low, yellow_high)
    mask = white_mask + yellow_mask
    
    filename = os.path.splittext(file)[0]
    cv2.imwrite("label\\"+filename+".png", 255*mask)

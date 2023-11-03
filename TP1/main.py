import os
from time import sleep
import cv2
import numpy as np
import matplotlib.pyplot as plt

workdir = os.path.join('.','silhouette45','003')

def detect_pt_fuit(img):
    x = (np.argwhere(img == (255,255,255)))[0]
    y = (np.argwhere(img == (255,255,255)))[-1]
    print(x,y)

    cv2.circle(img, (x[1],x[0]), 4, (0,0,255), 1)
    cv2.circle(img, (y[1],y[0]), 4, (0,0,255), 1)

    cv2.imshow('',img)


for file in os.listdir(workdir)[:-1]:
    img = cv2.imread(workdir+'\\'+file, 1)
    detect_pt_fuit(img)
    cv2.waitKey(80)

cv2.waitKey(0)
cv2.destroyAllWindows()
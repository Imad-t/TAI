import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('grayscale.png', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.figure()
plt.title("Grayscale Image Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

threshold= np.argmax(hist)
_, thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
result = cv2.hconcat([image, thresholded_image])
cv2.imshow('Combined Images', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

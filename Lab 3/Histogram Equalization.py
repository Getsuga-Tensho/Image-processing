import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread(r'C:\Users\Hemanta Dongol\Desktop\Image Processing\Lab 3\Image.png', 0)
cv.imshow('Original Image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()

hist, bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()
plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

equ = cv.equalizeHist(img)
cv.imshow('Equalized Image', equ)
cv.waitKey(0)
cv.destroyAllWindows()

import numpy as np
import cv2 as cv

img = cv.imread("./im/1.bmp")
img_median = np.hstack([
    cv.medianBlur(img, 3),
    cv.medianBlur(img, 5),
    cv.medianBlur(img, 7)
])
cv.imwrite("median_1.jpg", img_median)
img_gaussian = np.hstack([
    cv.GaussianBlur(img, (3, 3), 0),
    cv.GaussianBlur(img, (5, 5), 0),
    cv.GaussianBlur(img, (7, 7), 0)
])
cv.imwrite("gaussian_1.jpg", img_gaussian)

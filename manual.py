import cv2 as cv
import numpy as np
# import os

# cwd = os.getcwd()
# file_list = os.listdir(cwd + '/im')
# file_list = ['4.bmp', '14.bmp', '24.bmp']
file_list = ['4.bmp']

for file in file_list:
    # 读取图片
    origin = cv.imread('./im/' + file, 0)
    # cv.imshow('origin', img)
    # 去噪
    img = cv.medianBlur(origin, 5)
    img = cv.equalizeHist(img)
    img = cv.bilateralFilter(img, 9, 75, 75)
    # cv.imshow('fil', img)
    # 改善对比度和亮度
    for y in range(img.shape[0]):
        for x in range(img.shape[1]):
            img[y, x] = np.clip(0.9 * img[y, x] + (-100), 0, 255)
    # cv.imshow('light', img)
    cl = cv.createCLAHE(clipLimit=30, tileGridSize=(8, 8))
    img = cl.apply(img)
    # cv.imshow('output', img)
    # 二值化
    img = cv.GaussianBlur(img, (3, 3), 0)
    ret1, img = cv.threshold(img, 50, 255, cv.THRESH_OTSU)
    # cv.imshow('bi1', img)
    # 写出图片
    cv.imwrite('./op/ridges_' + file, img)
    cv.imshow('before & after', np.hstack([origin, img]))
    # 结束展示
    cv.waitKey(0)
    cv.destroyAllWindows()

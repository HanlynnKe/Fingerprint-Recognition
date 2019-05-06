import cv2 as cv
import numpy as np


def skeleton():
    img = cv.imread('./im/4.bmp', 0)
    cv.imshow('origin', img)
    # 中值滤波去噪+大津法二值化
    img = cv.medianBlur(img, 3)
    ret, img = cv.threshold(img, 0, 255, cv.THRESH_OTSU)
    img = cv.medianBlur(img, 5)
    cv.imshow('bef', img)

    # 确定参数，将图像取反
    element3c = cv.getStructuringElement(cv.MORPH_CROSS, (3, 3))
    element5e = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    img = cv.bitwise_not(img)

    # 提取图像骨架
    size = np.size(img)
    skel = np.zeros(img.shape, np.uint8)
    done = False
    while (not done):
        eroded = cv.erode(img, element3c)
        temp = cv.dilate(eroded, element3c)
        temp = cv.subtract(img, temp)
        skel = cv.bitwise_or(skel, temp)
        img = eroded.copy()

        zeros = size - cv.countNonZero(img)
        if zeros == size:
            done = True
    cv.imshow('skeleton', skel)

    # 平滑
    img = cv.GaussianBlur(skel, (5, 5), 11)
    img = cv.erode(img, element3c)
    img = cv.dilate(img, element5e)
    ret1, img = cv.threshold(img, 0, 255, cv.THRESH_OTSU)
    img = cv.bitwise_not(img)
    cv.imshow('gaussian skeleton', img)

    cv.waitKey(0)
    cv.destroyAllWindows()


def attempt():
    img = cv.imread('task2img/backgroundimg/9.jpg', 0)
    cv.imshow("before", img)
    # win_size = (10, 10)
    # block_size = (4, 4)
    # block_stride = (2, 2)
    # cell_size = (2, 2)
    # n_bins = 9
    # hog = cv.HOGDescriptor(win_size, block_size, block_stride, cell_size, n_bins)
    # hist = hog.compute(img, winStride=(4, 4), padding=(4, 4))
    # for item in hist:
    #     for elem in item:
    #         print(elem)
    rectangle = np.zeros(img.shape[0:2], dtype="uint8")
    cv.rectangle(rectangle, (5, 5), (14, 14), 255, -1)
    cv.imshow("Rectangle", rectangle)

    img = cv.bitwise_and(img, rectangle)
    cv.imshow("after", img)

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    attempt()

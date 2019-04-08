import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

# cwd = os.getcwd()
# file_list = os.listdir(cwd + '/im')
file_list = ['4.bmp', '14.bmp', '24.bmp']


# file_list = ['4.bmp']


# 填补汗孔函数
def manual_fill(img, iteration, threshold):
    b_count = 0
    w_count = 0
    i_height = img.shape[0]
    i_width = img.shape[1]
    for i in range(iteration):
        for y in range(1, i_height - 1):
            for x in range(1, i_width - 1):
                if img[y][x] == 255:
                    if img[y - 1][x - 1] == 0:
                        b_count += 1
                        # w_count -= 1
                    else:
                        # b_count -= 1
                        w_count += 1
                    if img[y - 1][x] == 0:
                        b_count += 1
                        # w_count -= 1
                    else:
                        # b_count -= 1
                        w_count += 1
                    if img[y - 1][x + 1] == 0:
                        b_count += 1
                        # w_count -= 1
                    else:
                        # b_count -= 1
                        w_count += 1
                    if img[y][x + 1] == 0:
                        b_count += 1
                        # w_count -= 1
                    else:
                        # b_count -= 1
                        w_count += 1
                    if img[y + 1][x + 1] == 0:
                        b_count += 1
                        # w_count -= 1
                    else:
                        # b_count -= 1
                        w_count += 1
                    if img[y + 1][x] == 0:
                        b_count += 1
                    else:
                        # b_count -= 1
                        w_count += 1
                    if img[y + 1][x - 1] == 0:
                        b_count += 1
                        # w_count -= 1
                    else:
                        # b_count -= 1
                        w_count += 1
                    if img[y][x - 1] == 0:
                        b_count += 1
                        # w_count -= 1
                    else:
                        # b_count -= 1
                        w_count += 1
                    if b_count > threshold:
                        img[y][x] = 0
                    if w_count > threshold:
                        img[y][x] = 255
                    b_count = 0
                    w_count = 0
    return img


def enhance_contrast(src, a, b):
    i_height = src.shape[0]
    i_width = src.shape[1]
    blank = np.zeros([i_height, i_width], src.dtype)
    dst = cv.addWeighted(src, a, blank, 1 - a, b)
    return dst


def show_hist(src):
    # 图像直方图
    hist = cv.calcHist(src, [0], None, [256], [0, 256])
    plt.figure()  # 新建一个图像
    plt.title("Grayscale Histogram")  # 图像的标题
    plt.xlabel("Bins")  # X轴标签
    plt.ylabel("# of Pixels")  # Y轴标签
    plt.plot(hist)  # 画图
    plt.xlim([0, 256])  # 设置x坐标轴范围
    plt.show()  # 显示图像


for file in file_list:
    # 读取图片
    img = cv.imread('./im/' + file, 0)
    # cv.imshow('origin', img)
    # # 中值滤波去噪
    # img = cv.medianBlur(img, 5)
    # cv.imshow('medi', img)
    img = cv.equalizeHist(img)
    img = cv.bilateralFilter(img, 9, 75, 75)
    # cv.imshow('fil', blur)
    # # 提高对比度和亮度
    # blur = enhance_contrast(blur, 0.8, 50)
    # cv.imshow('con', blur)
    # 二值化
    img = cv.GaussianBlur(img, (5, 5), 0)
    # cv.imshow('g', blur)
    ret1, img = cv.threshold(img, 180, 255, cv.THRESH_OTSU)
    # cv.imshow('bi1', blur)
    # # 手动填补
    # img = manual_fill(blur, 10, 4)
    # cv.imshow('pores', img)
    # 写出图片
    cv.imwrite('./op/ridges_' + file, img)
    # # 结束展示
    # cv.waitKey(0)
    # cv.destroyAllWindows()

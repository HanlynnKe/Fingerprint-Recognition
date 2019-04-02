import cv2 as cv
import os


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
                    else:
                        # b_count -= 1
                        w_count += 1
                    if img[y][x - 1] == 0:
                        b_count += 1
                    else:
                        # b_count -= 1
                        w_count += 1
                    if b_count >= threshold:
                        img[y][x] = 0
                    if w_count >= threshold:
                        img[y][x] = 255
                    b_count = 0
                    w_count = 0
    return img


# cwd = os.getcwd()
# file_list = os.listdir(cwd + '/im')
file_list = ['4.bmp', '14.bmp', '24.bmp']
# file_list = ['24.bmp']
for file in file_list:
    # 读取图片
    img = cv.imread('./im/' + file, 0)
    # cv.imshow('origin', img)
    # 中值滤波去噪
    img = cv.medianBlur(img, 3)
    # 直方图均衡化
    img = cv.equalizeHist(img)
    # cv.imshow('hist', img)
    # 二值化
    ret, img = cv.threshold(img, 180, 255, cv.THRESH_OTSU)
    # cv.imshow('bi', img)
    # 手动填补
    img = manual_fill(img, 6, 5)
    # cv.imshow('pores', img)
    # 写出图片
    cv.imwrite('./op/ridges_' + file, img)
    # # 结束展示
    # cv.waitKey(0)
    # cv.destroyAllWindows()

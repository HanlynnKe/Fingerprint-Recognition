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
                        w_count -= 1
                    else:
                        b_count -= 1
                        w_count += 1
                    if img[y - 1][x] == 0:
                        b_count += 1
                        w_count -= 1
                    else:
                        b_count -= 1
                        w_count += 1
                    if img[y - 1][x + 1] == 0:
                        b_count += 1
                        w_count -= 1
                    else:
                        b_count -= 1
                        w_count += 1
                    if img[y][x + 1] == 0:
                        b_count += 1
                        w_count -= 1
                    else:
                        b_count -= 1
                        w_count += 1
                    if img[y + 1][x + 1] == 0:
                        b_count += 1
                        w_count -= 1
                    else:
                        b_count -= 1
                        w_count += 1
                    if img[y + 1][x] == 0:
                        b_count += 1
                    else:
                        b_count -= 1
                        w_count += 1
                    if img[y + 1][x - 1] == 0:
                        b_count += 1
                    else:
                        b_count -= 1
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
file_list = ['27.bmp']
seq = 1
for file in file_list:
    # 读取图片
    img = cv.imread('./im/' + file, 0)
    # cv.imshow('origin', img)
    # 中值滤波去噪
    img = cv.medianBlur(img, 3)
    # cv.imshow('med', img)
    # 大津法二值化
    ret, img = cv.threshold(img, 0, 255, cv.THRESH_OTSU)
    cv.imshow('bi', img)
    # 手动填补
    img = manual_fill(img, 5, 3)
    cv.imshow('pores', img)
    # 先闭后开
    img = cv.bitwise_not(img)
    element5e = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    element3c = cv.getStructuringElement(cv.MORPH_CROSS, (7, 7))
    img = cv.morphologyEx(img, cv.MORPH_CLOSE, element3c)
    cv.imshow('close', img)
    img = cv.morphologyEx(img, cv.MORPH_OPEN, element5e)
    cv.imshow('open', img)
    img = cv.bitwise_not(img)
    # 写出图片
    # cv.imwrite('./op/ridges_' + file, img)
    # seq += 1
    # 结束展示
    cv.waitKey(0)
    cv.destroyAllWindows()

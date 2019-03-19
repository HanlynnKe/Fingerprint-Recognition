import os
import cv2 as cv

cwd = os.getcwd()
file_list = os.listdir(cwd + '/im')
seq = 1
for file in file_list:
    # 读取图片
    img = cv.imread('./im/' + file)
    # 转换为灰度图
    img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    # 使用中值滤波去除噪声
    img_median = cv.medianBlur(img_gray, 3)
    # 大津法二值化
    ret, img_bi = cv.threshold(img_median, 0, 255, cv.THRESH_OTSU)
    # 再次使用中值滤波去除边缘毛噪和大部分汗孔
    img_x = cv.medianBlur(img_bi, 5)
    # 写出图片
    cv.imwrite('./op/median_bi_' + file, img_x)
    seq += 1

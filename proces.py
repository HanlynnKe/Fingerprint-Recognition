import cv2 as cv

# 读取图片
img = cv.imread("./im/7.bmp")
# 转换为灰度图
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# 使用中值滤波来去除噪声
img_median = cv.medianBlur(img, 3)
# 统计图片各个像素灰度值
grey = []
for row in img:
    for px in row:
        grey.append(px)
grey.sort()
# 求灰度值中值用于二值化
n = len(grey)
median = grey[int(n / 2)]
# 二值化
ret1, img_bi = cv.threshold(img_median, median, 255, cv.THRESH_BINARY)
# 写出图片
cv.imwrite("median_bi_median.jpg", img_bi)

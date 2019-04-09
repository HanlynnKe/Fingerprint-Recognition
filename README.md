# Fingerprint-Recognition

This is a ***Digital Image Processing*** project

Fingerprint Recognition based on Python along with OpenCV

#### 小心得：

在manual.py中使用中值滤波过滤椒盐噪声，再此基础上用双边滤波能够在保留边缘信息的
情况下过滤高斯噪声。在二值化之前采用OpenCV中的CLAHE来提升对比度，再用高斯滤波过滤
个别细小噪声。最后采用otsu法二值化，完成实验。

希望有时间的话能够研究一下GitHub上面Utkarsh-Deshmutkh的代码仓库。

[https://github.com/Utkarsh-Deshmukh/Fingerprint-Enhancement-Python]

我仓库里skeleton.py是一点骨架提取的代码，前期有点帮助，后来还是舍弃了这种办法。
助教不是很给力，寻求帮助的时候一点有用的提示都没有 :-(
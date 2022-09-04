#轮廓检测
import cv2
import numpy as np

img = np.zeros((200,200),dtype=np.uint8)
img[50:150,50:150] = 255

img = cv2.imread('1.jpg')
#生成一个白色的背景
background = np.full_like(img,255,np.uint8)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 

# 图像的二值化(一般在灰度图上处理有意义)
thresh_value,thresh_img =cv2.threshold(gray_img,128,255,0)
print(thresh_value)

#OpenCV(4.1.0)版返回两个参数contours：轮廓的点集（python列表） hierarchy：各层轮廓的索引（numpy.ndarray）
#三个输入参数：输入图像（必须单通道图像也需做二值化操作），轮廓检索方式，轮廓近似方法
contours,hierarchy = cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours[0].shape,hierarchy.shape,type(hierarchy))
#还原为三通道做背景与定义彩色画笔对应（灰度图背景只能使用灰色值画笔）
# color_img = cv2.cvtColor(thresh_img,cv2.COLOR_GRAY2BGR)
# drawContours() 五个输入参数：原始图像，轮廓（python列表），
# 轮廓的索引（当设置为-1时，绘制所有轮廓），画笔颜色(对应输入图像格式的颜色类型)，画笔大小
# 输入图像和轮廓列表可以不是同一来源
final_img = cv2.drawContours(background,contours,-1,(255,0,0),2)
cv2.imshow('contours',final_img)
cv2.waitKey()
cv2.destroyAllWindows()

'''
threshold函数的使用: src：源图像，可以为8位的灰度图，也可以为32位的彩色图像。
					maxval：返回图像中最大值  thresh：阈值  type：阈值类型

阈值类型: 常用值为0（cv2.THRESH_BINARY）参考下述网址：
https://blog.csdn.net/a19990412/article/details/81172426
https://blog.csdn.net/u012566751/article/details/77046445


如果采用彩色图像进行计算会得到彩色效果，而不是预期的二值化结果（三通道分别进行阈值转换，再合并） 

图像的二值化就是将图像上的像素点的灰度值设置为0或255，这样将使整个图像呈现出明显的黑白效果。
图像的二值化使图像中数据量大为减少，从而能凸显出目标的轮廓。

'''

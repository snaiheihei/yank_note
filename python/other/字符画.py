from PIL import Image   # 处理图片

# 打开图片
im = Image.open('1.jpg')     # type: Image.Image
# im.show()           # 图片打开
print(im.mode)
print(im.format)
om = im.convert("L")
x,y = im.size
for y in range(y):
        for x in range(x):  # 循环每一行的像素点位置
            px = im.getpixel((x,y))
            # print(px) 




# RGB转化为灰度图片
# L = R * 299/1000 + G * 587/1000 + B * 114/1000
om = im.convert("L")        # 转化图片的类型  L:灰度图

# om.thumbnail((im.size[0]//4,im.size[1]//4))

# print(om.size)
# (129, 170)

width, height = om.size

chars = "$$$$BBB8888EEEHHHHDDDDUUUUUYYYYYY1111111LLLLLLLL>>>>>-----.....__        "

# write 写
with open("chart.txt",'w') as f:
    for y in range(height):
        for x in range(width):  # 循环每一行的像素点位置
            px = om.getpixel((x,y))     # 获取像素点位置的灰度值
            # 100 / 255 = index / 字符长度
            index = int(px * len(chars) / 256)
            s = chars[index]
            f.write(s)
        f.write('\n')   # 换行

print("\a")
print(ascii("h"))
#

import pyautogui  #控制鼠标键盘
import time
#http://www.4399.com/flash/154247_3.htm
#可控 安全策略
pyautogui.FAILSAFE=True
def test():
	time.sleep(5)
	while 1:
		im = pyautogui.screenshot(region=(493,722,480,20))
		for i in range(4):
			x,y=60+120*i,10
			px=im.getpixel((x,y))
			if px[0]==1:   #判断像素点是否为黑色
				pyautogui.click((x+493,y+722))



if __name__ == '__main__':
	test()
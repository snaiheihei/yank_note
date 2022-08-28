#微信   控制   电脑
'''1和微信建立联系 import itchat 库

   2获取微信消息，权限给微信助手，匹配信息（1关机2截屏3拍照） 发送指令控制电脑

   3控制电脑函数1关机 os标准库  2截屏 ImageGrab [PIL]  3拍照 CV2库  '''

import itchat
import os
from PIL import ImageGrab
import cv2

def cmd():
	os.system('shutdown /s /t 0')

def screen():
	im = ImageGrab.grab()
	im.save("screen.jpg")
	itchat.send_image("screen.jpg","filehelper")

def photo():
	try:
		 # 调用电脑的第一个摄像头
		cap = cv2.VideoCapture(0)
		# 是否成功读取到摄像头 True Flase
	    # 读取到的资源
		ret,image=cap.read()
		if ret  :
			# 将摄像头的资源变成一张照片
			cv2.imwrite('afu.jpg',image)
			itchat.send_image("afu.jpg","filehelper")

		else :
			itchat.send('摄像头打开失败','filehelper')
		cap.release()
	except Exception as err:
		exit('摄像头有问题')

# 消息注册机制
#只要接收到任何的文本消息，就自动调用下方的函数
# 必须携带一个参数   msg		
@itchat.msg_register(['Text'])	
def message(msg):
	# 消息文本的内容  优化的小处理  去除左右的空格
	print(msg)
	data=msg["Text"].strip()
	print(data)
    # 当你自己给你自己发一条消息的时候，就让文件传输助手自动跳出来
	if  msg["FromUserName"]== msg["ToUserName"] :
		itchat.send('您现在可以操控电脑了','filehelper')
    # 判断消息是不是发给文件助手 权限分配
	if msg["ToUserName"] =='filehelper':
		if data == "关机":
			cmd()
		if data == "截屏":
			screen()
		if data == "拍照":
			photo()


def main():
	itchat.auto_login(hotReload=True)
	itchat.run()

if __name__ == '__main__':
	main()
	print(__name__)




			







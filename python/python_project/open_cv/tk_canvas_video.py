import cv2

videoCpature = cv2.VideoCapture('baidu.gif')

fps = videoCpature.get(cv2.CAP_PROP_FPS)
size = int(videoCpature.get(cv2.CAP_PROP_FRAME_WIDTH)),int(videoCpature.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(fps,size)


'''
#tk中label标签实现动态加载视频，摄像头录取

from tkinter import *
import cv2
from PIL import Image,ImageTk
from cameo import CaptureManager

def take_snapshot():
    print("有人给你点赞啦！")

def video_loop():
    if True:
        cv2.waitKey(40)
        frameManager.enterFrame()
        img = frameManager.frame
        print(type(img))
        cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)#转换颜色从BGR到RGBA
        current_image = Image.fromarray(cv2image)#将图像转换成Image对象
        imgtk = ImageTk.PhotoImage(image=current_image)
        panel.imgtk = imgtk 
        panel.config(image=imgtk)
        frameManager.exitFrame()
        root.after(40, video_loop)

frameManager = CaptureManager(cv2.VideoCapture('baidu.gif') )    #摄像头
root = Tk()
root.title("opencv + tkinter")
#root.protocol('WM_DELETE_WINDOW', detector)

panel = Label(root)  # initialize image panel
panel.pack(padx=10, pady=10)
# root.config(cursor="arrow")
btn = Button(root, text="点赞!", command=take_snapshot)
btn.pack(fill="both", expand=True, padx=10, pady=10)

# root.after(1,video_loop)
video_loop()
root.mainloop()
# cv2.destroyAllWindows()
'''

#tk中Canvas画布实现动态加载视频，摄像头录取
from cameo import CaptureManager
from tkinter import *
from PIL import Image,ImageTk
import numpy as np

class Win(object):

    def __init__(self):

        self.win = Tk()
        self.win.title('gif动图')
        self.win.geometry("600x500+100+100")
        self.win.resizable(width=False,height=False)
        self._captureManager = CaptureManager(cv2.VideoCapture('baidu.gif'))
        self.cv= Canvas(self.win, width = 600, height =500, bg = "white")
        self.cv.pack()

    def show(self):

        self._captureManager.enterFrame()

        img_data = self._captureManager.frame
        # mirroredFrame = np.fliplr(img_data).copy()      #数组镜像加载呈现,需显示复制
        cv2image = cv2.cvtColor(img_data, cv2.COLOR_BGR2RGBA) #转换颜色从BGR到RGBA
        current_image = Image.fromarray(cv2image)             #将图像转换成Image对象

        self.imgtk = ImageTk.PhotoImage(image=current_image)
        self.cv.create_image(270,190,image = self.imgtk)
        self._captureManager.exitFrame()
        self.win.after(90, self.show)

    def run(self):
        self.show()
        self.win.mainloop()
        

app = Win()
app.run()




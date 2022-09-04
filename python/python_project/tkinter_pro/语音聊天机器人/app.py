import tkinter as tk
import re
import chat_robot

class App:
    # 魔术方法
    # 可以通过重写的形式 自定义类属性 构造方法
    def __init__(self, width=500, height=300):
        self.w = width
        self.h = height
        self.title = '小小伙伴'

        # 软件名
        self.root = tk.Tk(className=self.title)
        # VIP视频播放地址 字符串类型
        self.text = ''

        # 定义播放源 整形类型
        self.v = tk.IntVar()

        # 默认选择第一个
        self.v.set(1)

        '''定义软件布局以及空间'''
        # Frame空间
        frame_1 = tk.Frame(self.root)
        frame_2 = tk.Frame(self.root)

        # 控件内容设置
        group = tk.Label(frame_1, text='聊天roboter：', padx=10, pady=10)
        tb = tk.Radiobutton(frame_1, text='我们开始聊天玩吧', variable=self.v, value=1, width=10, height=3)

        label = tk.Label(frame_2, text='请输入你要对我说的话：')
        # 输入框定义
        entry = tk.Entry(frame_2, textvariable=self.text, highlightcolor='Fuchsia', highlightthickness=1)

        # command 绑定函数
        play = tk.Button(frame_2, text='提交', font=('宋体', 12), width=2, height=1, command=self.chat_speaker)

        # 空间布局
        frame_1.pack()
        frame_2.pack()

        # 确定控件在软件中的位置 row 行 column 列
        group.grid(row=0, column=0)
        tb.grid(row=0, column=1)
        label.grid(row=0, column=0)
        entry.grid(row=0,column=1)
        play.grid(row=0, column=3, ipadx=10, ipady=10)

    def chat_speaker(self):
        data = self.text
        print(data)
        print(type(data))
        robot = chat_robot.Robot_Chat(data)
        response = robot.chat()
        print(response)
        chat_robot.baidu_speaker(response)



    def loop(self):
        self.root.resizable(True,True)
        self.root.mainloop()

# 脚本启动入口
if __name__ == "__main__":
    print(3)
    app = App()
    app.loop()  
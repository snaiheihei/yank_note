 #  *_* coding:utf8 *_*
# pip install baidu-aip
from json.tool import main
from tkinter import mainloop
from aip import AipSpeech
from playsound import playsound

""" 你的 APPID AK SK """
APP_ID ="16903182"
API_KEY = "q0FmTkCjr8yb1zxT23ysTqRE"
SECRET_KEY = "Nw7GcEsIv0nL8b2YeeZGKS5vgc3ZvXo1"

speech_client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def get_speech_from_file(text_path):

    with open(text_path, "r", encoding="utf8") as f:
        text_list = []
        while True:
            text_content = f.read(1024)
            if not text_content:
                break
            text_list.append(text_content)

    result_audio = b""
    # 第一个是文本， 第二个是语言， 第三个是平台，第四个是声音
    for text in text_list:
        print(text)
        result = speech_client.synthesis(text, "zh", 1, {
            "vol": 5,  # 音量
            "spd": 5,  # 语速
            "pit": 9,  # 语调
            "per": 0,  # 0：女 1：男 3：逍遥 4：小萝莉
        })
        if not isinstance(result, dict):
            result_audio += result
        else:
            print(result_audio)

    with open('audio.mp3', 'wb') as f:
        f.write(result_audio)

def get_speech_from_text(text):

    # print(text)
    text_part = len(text) // 200 + 1
    text_list = [text[200 * i: 200 * (i + 1)] for i in range(text_part)]

    result_audio = b""
    # 第一个是文本， 第二个是语言， 第三个是平台，第四个是声音
    for text in text_list:

        result = speech_client.synthesis(text, "zh", 1, {
            "vol": 5,  # 音量
            "spd": 5,  # 语速
            "pit": 6,  # 语调
            "per": 0,  # 0：女 1：男 3：逍遥 4：小萝莉
        })
        if not isinstance(result, dict):
            result_audio += result
        else:
            print(result_audio)

    with open('audio.mp3', 'wb') as f:
        f.write(result_audio)

if __name__ == "__main__":

    get_speech_from_text("你好啊，我们今天来讲故事")  #测试声音
    playsound("audio.mp3")






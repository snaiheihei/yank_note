import requests
import os
import json
from aip_speech_text import get_speech_from_text
from playsound import playsound

class Robot_Chat(object):

	url = 'http://openapi.tuling123.com/openapi/api/v2'
	header = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"}

	def __init__(self, text):

		self.text = text

		self.data = {
			# "reqType":0,   #0文本默认，（1图片地址，2音频 地址 不能使用）               
		    "perception": {     
		        "inputText": {
		            "text": self.text
		        }
		    },
		    "userInfo": {
		        "apiKey": "a2787309aaf749f184631e5600a1aba3",
		        "userId": "0002"
		    }
		}

	def chat(self):
		try:
			response = requests.post(self.url,headers=self.header,data =json.dumps(self.data))
			code = response.json()['intent']['code']
			content = response.json()['results'][0]['values']['text']
			if code == 4003:
				return "亲,今日聊天已结束,客官请回吧~~" 
			else:
				return content
		except:
			pass

def baidu_speaker(text):
	get_speech_from_text(text)
	playsound("audio.mp3")
	os.remove("audio.mp3")


if __name__ == '__main__':
        while True:
                robot = Robot_Chat(input('me:'))
                data=robot.chat()
                print('robot',data)
                # baidu_speaker(data)



'''
windows语音
	# from win32com import client
	# speaker = client.Dispatch('SAPI.Spvoice')
	# speaker.Speak(text)

'''

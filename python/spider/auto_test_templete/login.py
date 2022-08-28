from common_driver import CommonDriver

class Login(CommonDriver):
	"""docstring for Login"""
	def login(self,user,pwd):
		# 目标地址明确，测试功能明确
		url = 'https://www.51zxw.net'
		self.open_url(url)
		self.click('css_selector','body > div:nth-child(1) > div > div.user-info > div.user.pos-r > a')
		self.input_data('id','loginStr',user)
		self.input_data('id','pwd',pwd)
		self.click('class_name','btn')


if __name__ == '__main__':
	log = Login()
	log.login(user='19957061942',pwd='niu514647318')
	log.quit()

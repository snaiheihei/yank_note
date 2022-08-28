import re
import requests
import time
songId=[]
songname=[]
page=5#int(input("请输入要爬取的页数"))
header={"user-agent":"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.5 Safari/534.55.3"}  
for n in range (0,page):
    #歌曲URL
	# http://www.htqyy.com/play/33   
	# <span class="artistName"><a href="/artist/1" title="班得瑞" target="_blank">班得瑞</a></span>
	url='http://www.htqyy.com/top/musiclist/hot?pageIndex={}&pageSize=20'.format(n)
	print (url, end='\n')
	html = requests.get(url,headers=header)   #获取音乐榜单网页的信息
	# print(html.text)
	strr=html.text
	pat1=r'<a href=".*?" target="play" title="(.*?)" sid=".*?">'
	pat2=r'sid="(.*?)"'
	resultid=re.findall(pat2,strr)
	resultname=re.findall(pat1,strr)
	songId.extend(resultid)       #合并列表
	songname.extend(resultname)


print(songId) 
print(songname)    
# 歌曲URL  http://f2.htqyy.com/play/21     资源所在URL http://f2.htqyy.com/play7/21/mp3/4  URL时间变化 爬虫定期维护
for m in range(0,len(songId)):                      # http://f2.htqyy.com/play7/33/mp3/7   http://f2.htqyy.com/play7/33/mp3/8
	songurl='http://f2.htqyy.com/play7/{}/mp3/8'.format(songId[m])
	songName=songname[m]
	print (songurl,end='\n')
	print ('正在下载第{}首。。。'.format(m+1))
	response=requests.get(songurl,headers=header).content
	f=open('F:\\潭州课程录播及源码\\手势音乐播放\\music\\{}.mp3'.format(songname[m]),'wb') # format 填充
	f.write(response)	
	f.close()
	time.sleep(0.5)
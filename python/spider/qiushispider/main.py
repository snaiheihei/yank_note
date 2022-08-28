from scrapy import cmdline

cmdline.execute('scrapy crawl text --nolog'.split())

'''
scrapy 中 response对象介绍：

text属性来源
response.text = response.body.decode()

response.url 产生响应的URL地址 str类型
response.status HTTP响应的状态码 int类型
response.body  HTTP响应正文，bytes类型
response.text  HTTP响应正文，str类型
response.encoding HTTP响应正文的编码
response.request 产生改HTYTP响应的request对象
response.meta 构造request对象，可以将要传递给响应处理函数的信息通过meta参数传入 dict类型
response.selector <Selector xpath=None data='<html><head><style>\r\n    #musicList {\r\n '>
##response.xpath    <bound method TextResponse.xpath of <200 http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20>>
##response.css      <bound method TextResponse.css of <200 http://www.htqyy.com/top/musicList/hot?pageIndex=0&pageSize=20>>
##reponse.urljoin 用来构造绝对url,(爬取页面跳转到第二页的时候需要重新构造request，用到这个属性)

不在爬虫中存储文件，会降低效率 交给管道处理
'''

'''
 信息传递技术
带宽：
所谓带宽，是“频带宽度”的简称，原是通讯和电子技术中的一个术语，指通讯线路或设备所能传送信号的范围。
而网络中的带宽是指在规定时间内从一端流到另一端的信息量，即数据传输率。

车道的数量好比是带宽，车辆的数目就好比是网络中传输的信息量。
我们再用城市的供水网来比喻，供水管道的直径可以衡量运水的能力，
主水管直径可能有2m，而到家庭的可能只有2cm。在这个比喻中，水管的直径好比是带宽，水就好比是信息量。
使用粗管子就意味着拥有更宽的带宽，也就是有更大的信息运送能力。

在实际上网应用中，下载软件时常常看到诸如下载速度显示为176KB/s，103KB/s等宽带速率大小字样，
因为ISP提供的线路带宽使用的单位是比特（bit），而一般下载软件显示的是字节（Byte）（1Byte=8bit），
所以要通过换算，才能得实际值。
2M宽带理论上传输 256Kb/s
'''


'''
IP:

1、宽带基本上是家家户户都有，通过了向营运商付费，我们获得了宽带的使用权，
然而这只是表面现象，实际上使用者是拥有了一个接入互联网的资格和凭证，
计算机正是通过这种凭证获得了向互联网共享资源的权限，这个权限就是依赖IP，换言之，通过购买宽带，获得了IP。
2、一般来说，IP分为固定IP和可变IP两种，固定IP一般用在服务器上面，例如我们经常访问的淘宝、百度、新浪等，
他们的服务器IP是固定的，因为他们需要向用户提供持续的带宽输出，要是IP经常变化，肯定是不得行的。
另外，家用计算机和普通用户来说，都是使用的共享可变的IP，因为我们自身的PC机并不需要对外提供服务，
另外要想使用固定IP是需要额外付费的，并且费用不低。
对于拨号连接的宽带来说，网络断开或者重新拨号，IP就会发生变化。

3、如何查看自己的IP，方式一通过百度关键字“我的IP”就可以知道啦，当然还有更为专业一点的操作方式，
依次操作（win+R，输入“cmd”进入dos，输入“ipconfig”即可查看自己的ip）。

4、如何查看服务器的IP，在3的操作中进入dos窗口，然后使用ping命令，例如ping www.qq.com，
既可以看到qq服务器当前的IP地址，不过有的服务器可能ping不通，这个也要具体看改服务器是否开启了ping的权限。

5、内网IP和外网IP，内网IP通俗的讲，直接链接路由器的IP就是内网IP，例如家里一台路由器，然后3个人连上，
路由器采用拨号登录营运商，然后路由器通过路由分发供3个人上网。路由器对外链接的是外网IP与外界互联网通信，
内部分发内网IP供内部使用，如果不涉及到外网访问，内部之间也可以数据传输，例如局域网内联机游戏。
如果你在路由器环境下查看ip，应该是一个以192.168开头的网段。

A类一般用于大的公司你可以在那上   B类一般用于中型小型公司    C类一般用于家庭网络 
A类1.x.y.z~126.x.y.z            B类128.x.y.z~191.x.y.z   C类192.x.y.z~223.x.y.z  
网络号加主机号 A类24位主机号 B 18  C 8位（0~255）
192.168.X.X是私有地址。（192.168.0.0---192.168.255.255)

局域网内的计算机 通过物理层和数据链层，设置同一网络号的不同主机（例如 192.168.0.11，192.168.0.2）实现了
实现了IP协议 （ping 对方主机号测试连接）共享文件进行数据交换（共享文件方法） 
internet网中也是通过IP端口定位进行数据传递

'''
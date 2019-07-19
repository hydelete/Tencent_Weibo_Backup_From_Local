import re
from imgDownloader import imgDownload
import time

file = open("sample\我的广播_腾讯微博.html", "r", encoding='utf-8')

htmlstr = file.read()

#image url sample
#	http://t1.qpic.cn/mblogpic/158528cbeae42015f4b0/2000   t1
#	http://t2.qpic.cn/mblogpic/78ca1717d1218445bec8/2000   t2
#	http://t3.qpic.cn/mblogpic/4e01d5e164a5fd36203c/2000   t3

list = re.findall("(http://t[1-3].qpic.cn/mblogpic/[a-zA-Z0-9]*/460)", htmlstr)

small, large = "460", "2000"

#print("size = " , len(list))

def namingFile(url):
	return url.split('/')[-2]


allImages = set()
#array to set, make them distinct
for item in list:
	allImages.add(item)

#print("size = " , len(allImages))
	
for item in allImages:
	tarUrl = item[0:-len(small)] + large
	print("image url = " + tarUrl + ", downloading...")
	imgDownload(tarUrl, namingFile(item))
	time.sleep(0.2)

file.close()
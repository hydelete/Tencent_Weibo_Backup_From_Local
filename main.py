import re
from imgDownloader import imgDownload
import time

file = open("sample\我的广播_腾讯微博.html", "r", encoding='utf-8')

htmlstr = file.read()

file.close()

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
imagesToDownloadAgain = set()
#array to set, make them distinct
for item in list:
	allImages.add(item)

#print("size = " , len(allImages))

redownloadCount = 0
redownloadMax = 400

def processDownload(images):
	global redownloadCount, redownloadMax
	
	for item in images:

		tarUrl = item[0:-len(small)] + large
		print("image url = " + tarUrl + ", downloading...")
		dnloadRet = imgDownload(tarUrl, namingFile(item))
		
		if not dnloadRet:
			imagesToDownloadAgain.add(item)
				
		time.sleep(0.2)
		
	if(redownloadCount < redownloadMax): #check a limitation of redownloading
		if(len(imagesToDownloadAgain) > 0):
			allImages.clear()
			for item in imagesToDownloadAgain:
				allImages.add(item)
				redownloadCount+=1
			imagesToDownloadAgain.clear()
			processDownload(allImages)

processDownload(allImages)

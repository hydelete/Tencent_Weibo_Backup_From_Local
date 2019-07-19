import os
import logging
from urllib import request

urlTar = "https://abload.de/img/untitled2p3kyz.png"

dirName = "images"

logging.basicConfig(filename="debug.log",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

def isPostfixWith(str, postfixer):
	return str.find("." + postfixer) != -1

def imgDownload(urlTar, filename = "", folder = "images"):
	logging.info("URL = " + urlTar)
	
	#create folder save image
	if not os.path.exists(folder):
		os.mkdir(folder)
		print("Directory " , folder ,  " Created ")
	
	
	if('' != filename):
		file_name = filename +  ".png" 
	else:
	
		#filter url contain parameters
		file_name = urlTar.find('?')
		if(file_name != -1):
			file_name = urlTar.split('?')[0].split('/')[-1]
		else:
			file_name = urlTar.split('/')[-1]
		#u = request.urlopen(url = urlTar, timeout = 3)
		
		#deal with postfix of filename 
		postfixCheck = ['png', 'jpg', 'jepg', 'gif', 'webp']
		hasPostfix = False
		for item in postfixCheck:
			if(isPostfixWith(file_name, item)):
				file_name += "." + item
				hasPostfix = True
				break
		
		if not hasPostfix:
			file_name += ".png" 
	
	f = None
	try:
		u = request.urlopen(url = urlTar)
		f = open( folder + "\\" + file_name, 'wb')
	except Exception as e: 
		print(e)
		print("地址不对，或者网络故障")
		logging.info("error occurring, URL: " + urlTar)
	else:
		#meta = u.info()
		#file_size = int(meta.getheaders("Content-Length")[0])
		file_size = u.headers['content-length']
		print("Downloading: " + file_name + " Bytes: " + file_size) 

		file_size_dl = 0
		block_sz = 8192
		while True:
			buffer = u.read(block_sz)
			if not buffer:
				break

			file_size_dl += len(buffer)
			f.write(buffer)
			status = round(file_size_dl * 100. / float(file_size), 1) #(file_size_dl, file_size_dl * 100. / file_size)
			print(str(status) + "%")

	finally:
		if f is not None:
			f.close()
		

if __name__ == "__main__":
	imgDownload(urlTar, dirName)
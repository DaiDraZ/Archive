# https://online.fliphtml5.com/qkkki/rvfm/files/large/1.jpg
from idm import IDMan

downloader = IDMan()
for i in range(1,270):
	url = f"https://online.fliphtml5.com/qkkki/rvfm/files/large/{i}.jpg"

	downloader.download(url, r"c:\DOWNLOADS", output=None, referrer=None, cookie=None, 
		postData=None, user=None, password=None, 
		confirm=False, lflag=None, clip=False)
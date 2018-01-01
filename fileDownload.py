from urllib import request

url = ''


def file_download(url):
	'''Want to download file from website with use of python?
		here is the solution
	'''
    get_url = request.urlopen(url)
    get_readed = get_url.read()
    url_readed_str  = str(get_readed)
    url_separeted = url_readed_str.split()

    file_name = 'data.html'
    fw = open(file_name , 'w')

    for line in url_separeted:
        fw.write(line + '\n')

    fw.close()


try:
	urll = input("Url :: ")
	file_download(urll)
except:
	print("Url should be string!")

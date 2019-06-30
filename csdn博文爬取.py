import urllib.request
import re
url="https://www.csdn.net/"
headers=("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders=[headers]
#安装为全局/
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
pat='''<div class="title">
                        <h2>
                            <a href="(.*?)"'''
alllink=re.compile(pat).findall(data)

print(alllink)
for i in range(0,len(alllink)):
    try:

        thislink=alllink[i]
        localpath="C:\\Users\\Staywitmmee\\Desktop\\py\\"+str(i)+".html"
        urllib.request.urlretrieve(thislink,filename=localpath)
        print("当前文章第("+str(i)+")篇爬取成功")
    except Exception as err:
        print(err)

import urllib.request
import re
#response=urllib.request.urlopen("http://edu.csdn.net/huiyiCourse/detail/253")

array=["beijing","shanghai","xian","nanjing","zhengzhou"]

#arrays=["https://movie.douban.com/cinema/nowplaying/beijing/",
  #      "https://movie.douban.com/cinema/nowplaying/nanjing/",
        #"https://movie.douban.com/cinema/nowplaying/xian/",
        #"https://movie.douban.com/cinema/nowplaying/shanghai/"]
i=0
for j in range(0,len(array)):
    response=urllib.request.urlopen('https://movie.douban.com/cinema/nowplaying/'+array[j]+'/')
    #response=urllib.request.urlopen(j)
    #print(response)
    #response=urllib.request.urlopen("https://movie.douban.com/cinema/nowplaying/beijing/")
    data=response.read().decode("utf-8")
    print(data)
    pat='''<a href="https://movie.douban.com/subject/(.*?)/?from=playing_poster"
                                    class="ticket-btn"
                                    target="_blank"
                                    title="(.*?)"
                                    data-psource="title">
                                    (.*?)
                                </a>'''
    result=re.compile(pat).findall(data)
    #print(result)
    byte=["北京","上海","西安","南京","郑州"]
    fh=open("C:\\Users\\Staywitmmee\\Desktop\\chubanshe.txt","a+")
    fh.write("===========================\n")
    fh.write(byte[j]+"\n")
   

    
    for i in range(0,len(result)):
        try:
                
            print(result[i][1])
            fh.write(result[i][1]+"\n")
        except Exception as err:
            print(err)
fh.close()

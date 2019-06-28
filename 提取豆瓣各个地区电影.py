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
    #pat='''<a href="https://movie.douban.com/subject/(.*?)/?from=playing_poster"
                                    #class="ticket-btn"
                                    #target="_blank"
                                    #title="(.*?)"
                                    #data-psource="title">
                                    #(.*?)
                                #</a>'''
    pat='''<li
                        id="(.*?)"
                        class="(.*?)"
                        data-title="(.*?)"
                        data-score="(.*?)"
                        data-star="(.*?)"
                        data-release="(.*?)"
                        data-duration="(.*?)"
                        data-region="(.*?)"
                        data-director="(.*?)"
                        data-actors="(.*?)"
                        data-category="(.*?)"
                        data-enough="(.*?)"
                        data-showed="(.*?)"
                        data-votecount="(.*?)"
                        data-subject="(.*?)"
                    >'''

           
    result=re.compile(pat).findall(data)
    #result1=re.compile(pat1).findall(data)
    #print(result)
    #print(result1)
    print(result[1])
    byte=["北京","上海","西安","南京","郑州"]
    fh=open("C:\\Users\\Staywitmmee\\Desktop\\chubanshe.txt","a+")
    fh.write("===========================\n")
    fh.write(byte[j]+"\n")
   
    for i in range(0,len(result)):
        try:
        
           fh.write(result[i][2]+"，")
           fh.write(result[i][3]+"，")
           fh.write(result[i][5]+"，")
           fh.write(result[i][6]+"，")
           fh.write(result[i][7]+"，")
           fh.write(result[i][8]+"\n")
        except Exception as err:
           print(err)
fh.close()

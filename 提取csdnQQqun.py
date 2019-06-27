import urllib.request
import re
response=urllib.request.urlopen("http://edu.csdn.net/huiyiCourse/detail/253")
#response=urllib.request.urlopen("https://www.baidu.com")
data=response.read().decode("utf-8")
pat="<p>(\d*?)</p>"
result=re.compile(pat).findall(data)
print(result)

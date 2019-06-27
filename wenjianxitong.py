import xlrd
import xlsxwriter
import numpy

allxls=["C:/Users/Staywitmmee/Desktop/text1.xlsx",
        "C:/Users/Staywitmmee/Desktop/text2.xlsx",
        "C:/Users/Staywitmmee/Desktop/text3.xlsx"]
endxls="C:/Users/Staywitmmee/Desktop/sum.xlsx"

def open_xls(file):
    try:
        fh=xlrd.open_workbook(file)
        return fh
    except Exception as e:
        print(str("打开出错，错误为："+e))

def getsheet(fh):
    return fh.sheets()


def getnrows(fh,sheet):
    table=fh.sheets()[sheet]
    #content=table.row_values
    content=table.nrows
    return content

def getfilect(fh,f1,shnum):
    fh=open_xls(f1)
    table=fh.sheet_by_name(shname[shnum])
    num=getnrows(fh,shnum)
    lenrvalue=len(rvalue)
    for row in range(0,num):
        rdata=table.row_values(row)
        rvalue.append(rdata)
    filevalue.append(rvalue[lenrvalue:])
    return filevalue

filevalue=[]
svalue=[]
rvalue=[]
shname=[]
fh=open_xls(allxls[0])
sh=getsheet(fh)
x=0
for sheet in sh:
    shname.append(sheet.name)
    svalue.append([])
    x+=1

for shnum in range(0,x):
    for f1 in allxls:
        print("正在读取文件："+str(f1)+"的第"+str(shnum)+"个标签的。。。")
        filevalue=getfilect(fh,f1,shnum)
    svalue[shnum].append(filevalue)

sn=x
fn=len(allxls)
endvalue=[]

def getsvalue(k):
    for z in range(k,k+fn):
        endvalue.append(svalue[0][0][z])
    return endvalue

wb1=xlsxwriter.Workbook(endxls)
ws=wb1.add_worksheet()
polit=0
linenum=0

for s in range(0,sn*fn,fn):
    thisvalue=getsvalue(s)
    tvalue=thisvalue[polit:]

    for a in range(0,len(tvalue)):
        for b in range(0,len(tvalue[a])):
            for c in range(0,len(tvalue[a][b])):
                data=tvalue[a][b][c]
                ws.write(linenum,c,data)
            linenum+=1
    polit=len(thisvalue)
wb1.close()
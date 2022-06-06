import os
from os import path
import xlwt

def scanner_filetoexcel(url):
    #创建工作表并初始化
    wb = xlwt.Workbook(encoding = 'utf-8')
    #北京
    ws1 = wb.add_sheet('beijing', cell_overwrite_ok = True)
    ws1.write(0,0,'品名')
    ws1.write(0,1,'规格（mm）')
    ws1.write(0,2,'材质')
    ws1.write(0,3,'产地')
    ws1.write(0,4,'价格（元）')
    ws1.write(0,5,'涨跌（元）')
    ws1.write(0,6,'备注')
    ws1.write(0,7,'日期')
    row = 1
    col = 0
    #遍历文件夹，找出目标文件
    file = os.listdir(url)
    for f in file:
        real_url = path.join(url, f)
        fi = open(real_url,'r',encoding='UTF-8')
        lines = fi.readlines()
        first_line = lines[0]
        date = first_line[5: 9]
        date = date.replace('月', '-')
        date = date.replace('日', '')
        #写入excel
        if ("北京冷轧板卷" in first_line 
         or "北京无缝管" in first_line 
         or "北京焊管" in first_line 
         or "北京中厚板" in first_line 
         or "北京彩涂板" in first_line):
            first_line = lines[0]
            for line in lines[3:]:
                a = line.split()
                ws1.write(row, 7, date)
                for i in range(len(a)):
                    ws1.write(row, col, a[i])
                    col += 1
                row += 1
                col = 0
            wb.save("gangyi.xls")
    #上海
    ws2 = wb.add_sheet('shanghai', cell_overwrite_ok = True)
    ws2.write(0,0,'品名')
    ws2.write(0,1,'规格（mm）')
    ws2.write(0,2,'材质')
    ws2.write(0,3,'产地')
    ws2.write(0,4,'价格（元）')
    ws2.write(0,5,'涨跌（元）')
    ws2.write(0,6,'备注')
    ws2.write(0,7,'日期')
    row = 1
    col = 0
    #遍历文件夹，找出目标文件
    file = os.listdir(url)
    for f in file:
        real_url = path.join(url, f)
        fi = open(real_url,'r',encoding='UTF-8')
        lines = fi.readlines()
        first_line = lines[0]
        date = first_line[5: 9]
        date = date.replace('月', '-')
        date = date.replace('日', '')
        #找到目标文件，写入excel表格中
        if ("上海冷轧板卷" in first_line 
         or "上海无缝管" in first_line 
         or "上海焊管" in first_line 
         or "上海中厚板" in first_line 
         or "上海彩涂板" in first_line):
            first_line = lines[0]
            for line in lines[3:]:
                a = line.split()
                ws2.write(row, 7, date)
                for i in range(len(a)):
                    ws2.write(row, col, a[i])
                    col += 1
                row += 1
                col = 0
            wb.save("gangyi.xls")

scanner_filetoexcel(r'C:\Users\gaox\Documents\Python\data')
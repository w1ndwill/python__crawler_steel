import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def line_chart(sheet_number,city):
  df = pd.read_excel(r"C:\Users\gaox\Desktop\python爬虫实践\gangyi1.xls", sheet_name=sheet_number)
  plt.figure(dpi=70,figsize=(24,8))
  plt.xticks(fontsize=10)
  plt.plot(df["日期"],df["流体管"],label="流体管",lw=2,color='red',marker='o',ms=1)
  plt.plot(df["日期"],df["焊管"],label="焊管",lw=2,color='blue',marker='o',ms=1)
  plt.plot(df["日期"],df["冷轧板卷"],label="冷轧板卷",lw=2,color='green',marker='o',ms=1)
  plt.plot(df["日期"],df["中厚板"],label="中厚板",lw=2,color='yellow',marker='o',ms=1)
  plt.plot(df["日期"],df["彩涂板卷"],label="彩涂板卷",lw=2,color='grey',marker='o',ms=1)
  plt.xlabel("日期")
  plt.ylabel("价格")
  plt.title(city+"五种钢材价格近两个月涨跌趋势图")
  plt.legend()
  plt.grid()
  plt.show()
line_chart(2,"北京")
line_chart(3,"上海")

def histogram_chart(types):
  df2 = pd.read_excel(r"C:\Users\gaox\Desktop\python爬虫实践\gangyi1.xls",sheet_name=2)
  df3 = pd.read_excel(r"C:\Users\gaox\Desktop\python爬虫实践\gangyi1.xls",sheet_name=3)
  for i in range(len(df2["日期"])):
    df2["日期"][i] = str(df2["日期"][i])[6:10]
  plt.figure(dpi=70,figsize=(24,8))
  plt.xticks(fontsize=10)
  x = list(range(len(df2[types])))
  width = 0.4
  plt.bar(x, height=df2[types],label="北京",width=width,color='red')
  for j in range(len(x)):
    x[j] = x[j] + width
  plt.bar(x, height=df3[types],label="上海",width=width,color='green')
  x = np.array(x)
  plt.xticks(x-width/2, df2["日期"])
  plt.title('北京上海两地'+types+'价格对比柱状图')
  plt.xlabel("日期")
  plt.ylabel("价格")
  plt.legend()
  plt.show()
histogram_chart('流体管')
histogram_chart('焊管')
histogram_chart('冷轧板卷')
histogram_chart('中厚板')
histogram_chart('彩涂板卷')

  
  
  



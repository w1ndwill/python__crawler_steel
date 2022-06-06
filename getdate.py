import requests
from lxml import etree
import os
from time import sleep
import matplotlib.pyplot as plt
import numpy as np
def get_data(num):
    if os.path.isfile(f"data/{num}"):
        return
    url = f"http://www.gtgqw.com/showhz{num}.html"
    print(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    print(res.status_code)
    if res.status_code == 200:
        tree = etree.HTML(res.text)
        title = tree.xpath("//h1/text()")
        print(title)
        f = open(f"data/{num}", "w", encoding="utf-8")
        f.write(title[0].strip()+"\n")
        for one in tree.xpath("//tr"):
            one_tr = one.xpath("td/text()")
            f.write("\t".join(one_tr) + "\n")
        f.close()

if __name__ == "__main__":
    # 1抓数据
    for i in range(1732662, 1741200):
        print("page: ", i)
        get_data(i)
        sleep(1)

    url = "http://www.gtgqw.com/showhz1100000.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
# -*- coding: utf-8 -*-
"""202121224_강지웅_우주이미지 크롤링

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eU98T4vIxi0UNw_7iROTdNFq9XjEzX94
"""

from google.colab import drive
drive.mount('/content/drive')

import urllib.request
from bs4 import BeautifulSoup

#처음 페이지로 접근할 번호
pagenum = 1
#저장할 이미지 경로와 이름(image1 폴더에 img.jpg로 저장)
imagenum = 0
imagestr = "/content/drive/MyDrive/Colab Notebooks/image1/img"

while pagenum < 9:
  url = "http://sdo.kasi.re.kr/gallery_list.aspx?pageNo=" # 숫자가 나오는 부분 삭제
  url = url + str(pagenum)

  fp = urllib.request.urlopen(url)
  source = fp.read();
  fp.close()

  soup = BeautifulSoup(source, 'html.parser')
  soup = soup.findAll("ul",class_ = "gallery_list_cont")

  # 이미지 경로를 받아서 저장하기
  for i in soup:
    imagenum += 1
    imgurl = "http://sdo.kasi.re.kr/"+i.find("img")["src"]
    urllib.request.urlretrieve(imgurl,imagestr + str(imagenum) +".jpg")
    print(imgurl)
    print(imagenum)

  pagenum += 1
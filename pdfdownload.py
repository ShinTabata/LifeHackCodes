#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 03:08:46 2017

@author: ShinTabata
"""

########webスクレイピング、pdfファイルのダウンロードを作成

import requests

url="http://eml.berkeley.edu//~saez/course/course.html"
response=requests.get(url)
response.status_code

from bs4 import BeautifulSoup
bs = BeautifulSoup(response.content,"lxml")

bs.select('span')[0]


#########別手法　python2向けだったためうまくいかず。。。

# 例）PDFファイルを一括ダウンロードしたい
import os, re, urllib, urllib.request, urllib.parse
##urllib.parse

url # ホームページのURL
Dir=os.path.expanduser('~/Dropbox/economics/pubeco/saez/GraduatePubEcon') # ローカルの保存先

#try:
#  os.mkdir(Dir) # 保存先ディレクトリがなければ作る
#except OSError:
#  pass

#t=urllib.request.urlopen(url)
#txt=t.readline()
#p = re.compile('href.*?pdf\"') # PDFファイルへのリンクを引っ掛ける
#m=p.findall(txt)# 全該当リンク
#for f in m:
#  File=urlparse.urljoin(Site,f[6:-1])# ファイルの絶対パス
#  Savename=os.path.join(Dir,os.path.basename(File)) # 保存名設定
#  urllib.urlretrieve(File,Savename)
   
  
##############ここから成功パターン

import requests
import time

#from BeautifulSoup import BeautifulSoup

BASE_URL = u"http://eml.berkeley.edu//~saez/course/"

download_urls = []
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")
links = soup.findAll('a')

    # URLの抽出
pdf=u".pdf"
for link in links:

    href = link.get('href')

    if href and pdf in href:
        download_urls.append(href)

    # ファイルのダウンロード
for download_url in download_urls[:50]:

    # 一秒スリープ
    time.sleep(1)
    file_name = download_url.split("/")[-1]

    if BASE_URL in download_url:
        r = requests.get(download_url)
    else:
        r = requests.get(BASE_URL + download_url)
        if r.status_code == 200:
            f = open(file_name, 'wb')
            f.write(r.content)
            os.chdir(Dir)
            f.close()
            
########これで完成

#texもダウンロード
tex=u".tex"
for link in links:

    href = link.get('href')

    if href and tex in href:
        download_urls.append(href)

    # ファイルのダウンロード
for download_url in download_urls[:50]:

    # 一秒スリープ
    time.sleep(1)
    file_name = download_url.split("/")[-1]

    if BASE_URL in download_url:
        r = requests.get(download_url)
    else:
        r = requests.get(BASE_URL + download_url)
        if r.status_code == 200:
            f = open(file_name, 'wb')
            f.write(r.content)
            os.chdir(Dir)
            f.close()

######次のHPへ
#http://gabriel-zucman.eu/econ230/

BASE_URL = u"http://gabriel-zucman.eu/econ230/"
Dir=os.path.expanduser('~/Dropbox/economics/pubeco/zucman')
url="http://gabriel-zucman.eu/econ230/"

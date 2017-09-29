#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 10:46:53 2017

@author: ShinTabata
"""

#criate statalec env

import os
import os.path

print(os.path.expanduser('~'))  
# => /Users/ユーザー名

os.mkdir(os.path.expanduser('~')+"/Desktop/Statafile/statalecture")

list=["dta","data_excel","data_csv","log","graph","do"]
for a in list:
    os.mkdir(os.path.expanduser('~')+"/Desktop/Statafile/statalecture/"+a)
#これでユーザー名を気にせずにディレクトリの作成が可能。

#内容をみてみる。
statalec = open("/Users/ShinTabata/Desktop/statalecture_20170919_master_win2.do", "w")
for line in statalec:
    print(line)

# with はopenしたファイルを、with構文内の処理をした後に自動で閉じてくれるコマンド .closeが不要になる！
with open("/Users/ShinTabata/Desktop/statalecture_20170919_master_win2.do", 'r') as statalec:
    # read a list of lines into data
    data = statalec.readlines()

#では"\"を"/"に置き換えてみる。
for i in range(len(data)):
    data[i] = data[i].replace('\\','/')

print(data)
# and write everything back
with open("/Users/ShinTabata/Desktop/statalecture_20170919_master_mac2.do", 'w') as file:
    file.writelines(data)






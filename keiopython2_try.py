# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# 関数
def fun_noreturn():
    print("only print out me")

fun_nonreturn()

def fun_modulo2(num):
    syou = int(num / 2)
    amari = num % 2
    return (syou, amari)

fun_modulo2(41)

a1,a2 = fun_modulo2(39)

# 必須引数
def addfun(a,b):
    print(a+b)

addfun(1,2)                #=> 3
addfun("I am ", "Tamura")  #=> I am Tamura
addfun([1,2], [3,4])       #=> [1,2,3,4]
addfun([1,2])              #=> エラー

##一つの引数になってしまっているため
'''
Traceback (most recent call last):

  File "<ipython-input-385-e0b95a109a9e>", line 6, in <module>
    addfun([1,2])

TypeError: addfun() missing 1 required positional argument: 'b'
'''

# オプション引数
def waru_n(num, bunbo=2):
    syou = int(num/bunbo)
    amari = num % bunbo
    return (syou, amari)

waru_n(13)          # waru_n(13, 2)と同じ
waru_n(13, 5)       # waru_n(13, 5)
waru_n(13, bunbo=5) # 同上

##デフォルトで使う引数を指定しておくことができる。pdfダウンロード.pyの場合はpdfにしておくか。
    
# シーケンス型
##複数の引数を指定することができる。　*　を使う。関数タプルと呼ぶ。
def print_elems(*args):
    print(args)

print_elems("a","b","c")    #=> ('a', 'b', 'c')
print_elems(["a","b","c"])  #=> (['a', 'b', 'c'],)
print_elems(*["a","b","c"]) #=> ('a', 'b', 'c')


#len(obj): 要素数を取得する
#max(obj), min(obj): 要素の最大・最小 
#sorted(obj ) :昇順(降順)ソート
#sorted(obj, reverse=True) :降順ソート

####練習問題

lst = [1,2,3] 
str = "abcdef"
dic = {"one"=>1, "two"=>2, "three"=>3}

#上記三つのオブジェクトに関数len(),max(),
#sorted()を適用した結果を確認しなさい。

len(lst)
max(lst)
lst.sort(reverse=True)
lst.sort()
lst

len(str)
max(str)
sorted(str)



# キーワード付き可変長引数
def print_myself(**args):
    print(args)

4
print_myself(name="noname", age=30)


# モジュール
sqrt(4) #=> エラー

# 基本数学関数が集まったmath module
import math
math.sqrt(4) # => 2
# 重要な数学定数にもアクセスできる
math.pi #=> 3.141592653589793


# 高階関数
def str_len(s):
    return len(s)

arg = ["a","ab", "abc", "Tamura"]
ans = map(str_len, arg)

'''
map()の中では次のような処理が行われる：
1. 最初の要素"a"をstr_len()に与え、str_len("a")の返り値を得る。
2. 次の要素"ab"をstr_len()に与え、str_len("ab")の返り値を得る。
3. 次の要素"abc"をstr_len("abc")に与え、str_len("abc")の返り値を得る。
4. 次の要素"Tamura"をstr_lenに与え、str_len("Tamura")の返り値を得る。
5. 次の要素はないので、処理は終了。
'''
# 処理結果をリストで返す
list(ans)

# 無名関数lambdaを使った簡潔な記述方法
ans = map(lambda s: len(s), arg)
list(ans)

def is_odd(n):
    ans = (n % 2 == 1)
    return ans

arg = [10, 21, 33]
ans = filter(is_odd, arg)
'''
filter()の中では次のような処理が行われる
1. 最初の要素10をis_odd()に与え、答えがTrueならばキープ（キープしない）
2. 次の要素21ををis_odd()に与え、答えがTrueならばキープ（キープ）
3. 次の要素33ををis_odd()に与え、答えがTrueならばキープ（キープ）
'''
list(ans)

# 無名関数lambdaを使った簡潔な記述方法
ans = filter(lambda n: n%2==1, arg)



import numpy as np
import pandas as pd

# 1次元配列
v = np.array([1,2,3,4,5,6,7,8,9])
# 2次元配列
m = np.array([[1,2,3], [4,5,6],[7,8,9]])
m3 = np.array([[1,2,3], [4,5,6],[7,8]])
lst1 = [1,2,3]
lst2 = [4,5,6]
# 数を要素とするNumpy配列
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
# リスト型の計算
lst1 + lst2
# こちらはより数学的に自然
a1 + a2


a1 / 10   # array([ 0.1,  0.2,  0.3])
lst1 / 10 # エラー！
'''
lst1 / 10
Traceback (most recent call last):

  File "<ipython-input-113-7c9956031cca>", line 1, in <module>
    lst1 / 10

TypeError: unsupported operand type(s) for /: 'list' and 'int'

（型のエラー）　（リスト型と整数型に対する除算は定義されていない）
'''


# スライシング

v = np.array([1,2,3,4,5,6,7,8,9])
v[0] #　先頭
v[-1]

v[:3]
v[3:]
v[]

# 6x6 行列
rw0 = np.arange(0,6)
rw1 = np.arange(10,16)
rw2 = np.arange(20,26)
rw3 = np.arange(30,36)
rw4 = np.arange(40,46)
rw5 = np.arange(50,56)
m66 = np.array([rw0, rw1, rw2, rw3, rw4, rw5])

# 次元を知る
m66.shape

# 背景が赤の部分行列
m66[:, [1,3,5]]
m66[:, 1:6:2]
# 青文字の部分行列
m66[3:6, 0:3]
# 緑文字の部分行列
m66[0:3, 3:6]
# オレンジ文字のセルの内容を
np.diag(m66)

# 次元の変換 6x6 => 4x9 
m49 = np.reshape(m66,[4,9])
m49f = np.reshape(m66,[4,9], "F")

m49.shape
(m49.T).shape

# import pandas as pd


# pandas Series
ser1 = pd.Series(np.arange(0,5), index=["a","b","c","d","e"])
print(ser1)
ser1.shape # 要素が5の列ベクトル

ser2 = pd.Series(np.random.rand(5), index=["b","c","d","e","f"])
ser3 = pd.Series([0, 1, "two", 3, 4], index=["a","b","c","d","e"])

m35 = pd.DataFrame(
                   np.array([
                             [0,1,2,3,4], 
                             [10,11,12,13,14],
                             [20,21,22,23,24]
                             ]),
                   index=["A","B","C"],
                   columns=["a","b","c","d","e"]
                   )

# selection by bool arrays
ser1[ser1<3] #=> 0,1,2

m35[m35["a"]>=10, :] # コラム"a"の値が10以上のB行とC行が表示される。



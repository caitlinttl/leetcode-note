# Python bytecode 3.7.3
# For learning note

vs code 快速鍵

Ctrl + /   #註解 
Alt + 上下鍵 #移動行
Tab #右移， 
shift+Tab #左移
Alt + z #自動換行
crtl + L #選取行
Ctrl + Shift + K #刪除行
Ctrl+Tab #檔案之間切換 


快速複製行
直接alt + shift + ↑ or ↓，#會在上方或下方馬上複製一行
若反白多行後按alt + shift + ↑ or ↓，#則是上方或下方複製多行。

crtl + c 中斷程式執行 # 要在terminal按                                        
shift + F5 停止 # debag按
F9 加入中斷點



# pip list   #顯示安裝了哪些套件或是framework
# python get-pip.py (要在文件目錄執行)
# pip install --upgrade  pip 
# pip install pylint 檢查語法
# pip install xlrd
# pip install xlwings
# pip freeze > requirements.txt


# path = r'路徑'     (r 不轉譯)
# pip install -r requirements.txt   (要在文件目錄執行)
# pip install --upgrade setuptools

# pip install pip-review  # 更新所有套件
# pip-review -v -a  

'''
python get-pip.py (要在文件目錄執行)
pip install --upgrade  pip 
pip install --upgrade setuptools
pip install -r requirements.txt   (要在文件目錄執行)
pip-review -v -a
python -m pip install --user  --upgrade pip

'''
'''
scipy
librosa
pyqtgraph
sounddevice
numpy
audioread
imageio
matplotlib
pyftdi
PyQt5
keras
ntplib
pydub
soundfile
pyserial
pyserial
scikit_learn
tensorflow==1.14
padasip
pylint
xlrd
pip-review
xlwings

'''


x = "abcde"
for index, els in enumerate(x):
    print(f'{index},{els}')


列印菱形星星

s = '*'
for i in range(1, 10, 2):
    print((s*i).center(9))
for i in reversed(range(1, 8, 2)):
    print((s*i).center(9))  

可以使用@符號和裝飾器函數的名稱，並將其放在要裝飾的函數的定義之上。 例如，

@make_pretty
def ordinary():
    print("I am ordinary")
Python
上面代碼相當於 -

def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)




class a():

    def printA(self): # class內的function要加self
        x = 1
        print(123)
        # self.printB()
        return x

    def printB(self):
        x = 2
        self.printA() # 調用同一個class的function用self.
        print(345)
        return x
    
class b():
     
    def printC(self):
        a().printA() # 調用其他class的function要加() class要括號, function也要括號


b().printC() #class要括號, fun也要括號 #執行, 不理會返回值
a.printA() #function printA如果沒有self, 那class a就不用括號
A = a().printA() #執行, 並把返回值存入A # function printA有self, 那class a就要括號
print(A) #print 返回值


from os import walk

# 指定要列出所有檔案的目錄
path = "testFolder/"

# 1.遞迴列出所有子目錄與檔案
for root, dirs, files in walk(path):
  print("路徑：", root)
  print("資料夾：", dirs)
  print("檔案：", files)
  print("\n")

# 2.遞迴列出所有檔案的絕對路徑
for root, dirs, files in walk(mypath):
  for f in files:
    fullpath = join(root, f)
    print(fullpath)







import os


datapath = str(input(r'請輸入檔案路徑: '))


dir = datapath


print(dir)
print(datapath)


datapath = str(input(r'請輸入檔案路徑: '))
print(datapath)

turndatapath = datapath.replace('\\' , r'\\')



with open("123.txt",mode="r",encoding="utf-8") as file:
    data=file.read()
    print(data)
    print(len(data))
with open("123.txt",mode="a",encoding="utf-8") as file:
    newdata=file.write("A")
with open("123.txt",mode="r",encoding="utf-8") as file:
    data=file.read()
    print(data)
    print(len(data))

import os

with open("123.txt", 'r+') as file:
    file.seek(0,2)  
    size=file.tell()  
    file.truncate(size-1)  
with open("123.txt",mode="r",encoding="utf-8") as file:
    data=file.read()
    now = len(data)
    print(data)
    print(now)


'''

除錯
進入除錯模式的條件：

開啟資料夾
a. 檔案/開啟資料夾
b. 選擇程式所在的資料夾（通常一個專案設立一個資料夾）
設定中斷點
按F5進入除錯模式
（將變數）加入監看
a. 框選該變數名稱
b. 點右鍵，點「偵錯：加入監看」
c. 按Enter
根據以下除錯快速鍵追蹤程式
點中間正上方的「紅色正方形」停止偵錯
若要在重新進入偵錯模式只要從第4步開始就可以
除錯快速鍵

功能	快速鍵
設定/取消 中斷點	F9
除錯/繼續 執行	F5
一步一步執行，遇到函數則直接執行完函數，在往下執行	F10
一步一步執行，遇到函數則進入函數執行	F11
直接執行完函數，回到當初呼叫函數的位置	Shift + F11
停止除錯	Shift + F5

'''


# print 

print(100,500, sep='and', end='結束字元')


name = 'Majalis'
score = 95.7
S2 = 10003

print('分數為\n%10.3f\n%10.3f\n分' % (score,S2))
print('{} 的分數為 {}'.format(name,score))

分數為
    95.700
 10003.000
分
Majalis 的分數為 95.7




print()    #print空白
print('1')
print()




# 輸入、輸出

name = input('輸入姓名')
print(name)

score = input('成績')
print(int(score)+20)



# 加減乘除

+
-
*
/
%  餘數
// 整除的商數
** 次方  7**2等於7的二次方  7**3 7的三次方




# if elif else 的邏輯  同一層的條件，滿足一之後，就會忽略後面的全部條件



a = 5
b = 6

ans = str(a + b)
alma = str(int(a+b+1))  
almb = str(int(a+b-1))  

key = input('請輸入5+6的答案:')

if  key == str(ans):                              #條件一
    print('yes!')    
elif  key == str(alma) or key == str(almb):       #或條件二 (順著第一個if走) 不符合1，那有符合2嗎? #如果這邊寫if，那會和第一個if一起走(符合1嗎?符合2嗎?)
    key = input('接近了, 再試試看: ')
    if key == str(ans):
        print('答對囉!')
    if key != str(ans):
        print('還是不對，加油好嗎!')     
else:                                             #不符合條件一也不符合條件二
    print('NO! 差太多了!')
     

break：強制跳出 ❮整個❯ 迴圈
continue：強制跳出 ❮本次❯ 迴圈，繼續進入下一圈
pass：不做任何事情，所有的程式都將繼續  pass  #提醒自己之後要來完成
https://medium.com/@chiayinchen/1-%E5%88%86%E9%90%98%E6%90%9E%E6%87%82-python-%E8%BF%B4%E5%9C%88%E6%8E%A7%E5%88%B6-break-continue-pass-be290cd1f9d8


# try except

try:
     file = open('aaaa','r+')   # r 只讀  r+ 讀寫
except Exception as e:                  # 如果有錯誤，用except裡面的語句
except FileNotFoundError:
    print(e)
    print('沒有這個文件')
    response = input('需要創建嗎? y/n')
    if response == 'y':
        file = open('aaaa','w')
    else:
        pass
else: file.write('ssss')              # 如果沒有錯誤，用else裡面的語句
file.close()


import os

try:
    print('open前')
    with open("123.txt",mode="r",encoding="utf-8") as file:
        data=file.read()
        now = len(data)
    print('open後')
except Exception as e: 
    print("沒找到")
    print(e)
# else:
#     print(now)
'''

如果沒錯誤，會執行(try的全部和else(寫在外面的else，也可以不寫那個else))
open前
open後
2

如果有錯誤，會執行(try的內容會執行到遇到錯誤之前，然後執行except)
open前
沒找到
[Errno 2] No such file or directory: '456.txt'
'''
# with open("456.txt",mode="r",encoding="utf-8") as file:
#     data=file.read()
#     now = len(data)
#     print(now)



zip
lambda
map

# ------------------------------------------


set 找不同
找出列表不同的東西
add >>>加東西
clear >>>清除
remove >>減掉指定
discard >>沒有這個元素也不會報錯
set1.difference(set2)    不同
set1.intersection(set2)  交集

type >>> 判斷型態


# import

import time
time.localtime

import time as t
t.localtime

from time import time, localtime
就可以直接使用time和localtime 不需要寫成 time.localtime


from time import *
import time裡面的所有功能
直接使用localtime





# range for in
# list
# dict 字典  #del 刪除 #clear 清空



listA = range(5)
print(list(listA))
# [0, 1, 2, 3, 4]

listB = range(1,9)
print(list(listB))
# [1, 2, 3, 4, 5, 6, 7, 8]

listC = range(6,30,2)
print(list(listC))
#[6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

listD = range(30,6,-2)
print(list(listD))
#[30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8]

listA = ['A', 'B', 'C', 'D', 'E']

print(listA[2])



listA = ['A', 'B', 'C', 'D', 'E']

for a in listA:
    #print(a)    #分行
    print(a, end='') #印在一起




for n in range(1,5):
    print(n, end='\n')

1
2
3
4




listA = ['A', 'B', 'C', 'D', 'E']

#print(len(listA)) #5

for i in range(len(listA)):
    print(listA[i])

A
B
C
D
E


#append insert remove pop 
#sort() 由小到大排列
#reverse() 序列反轉
#listB = sorted(listA,reverse=True) #不改變原序列 產生新序列 reverse=True是由大到小; False是由小到大; 都沒寫的預設是F(小到大)



listA = ['A', 'B', 'C', 'D', 'E','C']

print(listA[:3])  #從零到第三位  # A B C
print(listA[-4])  #c   倒數第四位
print(listA[:-4])  #從零到-4位  <<<用來扣掉副檔名

n = listA.index('B')  # 返回索引
m = listA.count('C')  # 出現的次數

print(n,m)          #1 2

listA.append('add')

print(listA)        #['A', 'B', 'C', 'D', 'E', 'C', 'add']
print(len(listA))   #7

listA.insert(0,'head')
print(listA)        #['head', 'A', 'B', 'C', 'D', 'E', 'C', 'add'] 在指定位置插入

listA.remove('B')
print(listA)        #['head', 'A', 'C', 'D', 'E', 'C', 'add'] 移除指定

listA.pop(3)
print(listA)        #['head', 'A', 'C', 'E', 'C', 'add'] 拿掉指定位置的
print(len(listA))   #6

listA.pop()
print(listA)        #['head', 'A', 'C', 'E', 'C'] 拿掉最後一個

listA.sort()  #從小到大排序
listA.sort(reverse=Ture)  # 反向排序





#del




listA = ['A', 'B', 'C', 'D', 'E','C','C','C','C','C']

del listA[1]
print(listA)    #['A', 'C', 'D', 'E', 'C', 'C', 'C', 'C', 'C']

del listA[1:5:2]
print(listA)    #['A', 'D', 'C', 'C', 'C', 'C', 'C']






#tuple 元祖 為不能改變的串列  list可以append, tuple不能。優點是執行速度快、安全

tupleA = (1,2,3,4,5)

listA = list(tupleA)
print(listA)    #[1, 2, 3, 4, 5]

listA.append(8)
print(listA)    #[1, 2, 3, 4, 5, 8]




字典
d= {'apple':1,'pear':2, 'orange':3}

del d['pear']   <<刪除水梨





# for


sum = 0

for i in range(1,5):
    sum += i
    print(sum)   #print在for的下一行會一個一個列出來

1
3
6
10



sum = 0
n = 4

for i in range(1,n+1):
    sum += i
    print(sum)


sum = 0
n = 4


for i in range(1,n+1):
    sum += i
print(sum)      #10   #print 要和for同一行是print最後結論

'''
# break 

'''
for i in range(1,10):
    if i == 6:
        break   #停止條件
    print(i)  # 1~5
print(i)   #6 



'''




# continue (排除)
'''

for i in range(1,10):
    if i == 6:
        continue   #排除六 (碰到六就會為到迴圈開始)
    print(i)
print(i)

1   #print和if同行 一個一個列出來
2
3
4
5
7
8
9
9   #print和for同行 列出結論

'''

# while loop

'''

total = n = 0

while(n<10):
    n +=1       #如果少了這行，會無法離開迴圈，當機 (手動停止)
    total+=n
print(total)    #55




# 移動檔案

import shutil
import os
from os import walk
from os.path import join

MyPath  = './' # 當下目錄
KeyWord = input = '請輸入檔案關鍵字:'

for root, dirs, files in walk(MyPath):
  for i in files:
    FullPath = join(root, i) # 獲取檔案完整路徑
    FileName = join(i) # 獲取檔案名稱

    if KeyWord in FullPath:
      if not os.path.exists(MyPath + '/' + KeyWord + '/' + FileName):
        if not os.path.exists(KeyWord):
          os.mkdir(KeyWord)
        shutil.move(FullPath, MyPath + '/' + KeyWord)
        print ('成功將', FileName, '移動至', KeyWord, '資料夾')
      else:
        print (FileName, '已存在，故不執行動作')





JSON格式簡單來說，就是這二句重點：

--------------------------------

物件(object)用大括號 { }

陣列(array)用中括號 [ ]


with open('D:\\LargeD\\Python_py\\auto_ppt\\jsonnn\\stethoscope-irb-soundinfo-export.json', 'r', encoding='utf-8-sig') as reader:
    dict = json.loads(reader.read())
    # print(dict)
    print(dict.keys())
    print()
    print(dict.values())


    對字典使用 list(d) 會得到一個包含該字典所有鍵（key）的 list，其排列順序為插入時的順序。
    （若想要排序，則使用 sorted(d) 代替即可）。如果想確認一個鍵是否已存在於字典中，可使用關鍵字 in 。

>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave

#coding: utf-8
import types
 
#獲取字典中的objkey對應的值，適用於字典巢狀
#dict:字典
#objkey:目標key
#default:找不到時返回的預設值
def dict_get(dict, objkey, default):
  tmp = dict
  for k,v in tmp.items():
    if k == objkey:
      return v
    else:
      if type(v) is types.DictType:
        ret = dict_get(v, objkey, default)
        if ret is not default:
          return ret
  return default
 
#如
dicttest={"result":{"code":"110002","msg":"裝置裝置序列號或驗證碼錯誤"}}
ret=dict_get(dicttest, 'msg', None)
print(ret)

len : 檢查Dict的個數
in / not in : 檢查是某個Key否存在該dictionary裡，回傳Boolean值
copy : 將Dict之內容複製至另一變數
has_key : 檢查是否有某個Key存在，回傳Boolean值
items : 將Dict的key/value拆成Tuple之組合，回傳List
keys : 將Dict的key部份回傳成List
values : 將Dict的value部份回傳成List
get : 取得指定key的值，第二個參數則是指定當找不到該key的導候所回傳的預設值

>>> my_dict = {'first_name': 'eddie', 'last_name': 'kao', 'age': 30, 'weight': 80}
>>> len(my_dict)
4
>>> "eddie" in my_dict
False
>>> "first_name" in my_dict
True
>>> my_dict.has_key("age")
True
>>> my_dict.items()
[('first_name', 'eddie'), ('last_name', 'kao'), ('age', 30), ('weight', 80)]
>>> my_dict.keys()
['first_name', 'last_name', 'age', 'weight']
>>> my_dict.values()
['eddie', 'kao', 30, 80]
>>> my_dict.get("age")
30
>>> my_dict.get("height", 180)
180


print(data3M)
print(data3M.keys())
print()
print(data3M.values())
print(data3M.items())

# in_json:需要处理的json数据, target_key:目标键
# value:输出的列表,元素为目标键值对应的值(必须为空列表)

dd = {'a': 'ok1', '1': {'1': 11, '2': ('a', 111, {'a': 'ok2'}, [{'a': 'ok3'}, 2222], {'a': [11111, 22222]})}, '2': '2'}  # json数据例子

def get_json_value_by_key(in_json, target_key, results=[]):
    if isinstance(in_json, dict):  # 如果输入数据的格式为dict
        for key in in_json.keys():  # 循环获取key
            data = in_json[key]
            get_json_value_by_key(data, target_key, results=results)  # 回归当前key对于的value

            if key == target_key:  # 如果当前key与目标key相同就将当前key的value添加到输出列表
                results.append(data)

    elif isinstance(in_json, list) or isinstance(in_json, tuple):  # 如果输入数据格式为list或者tuple
        for data in in_json:  # 循环当前列表
            get_json_value_by_key(data, target_key, results=results)  # 回归列表的当前的元素

    return results


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
 
print "dict['Name']: ", dict['Name']
print "dict['Age']: ", dict['Age']


# in_dict:需要处理的字典, target_key:目标键
# value:输出的列表,元素为目标键值对应的值(必须为空列表), not_ldt:获取的目标类型不为dict

dicts = {'1': 1, '2': 2, '3': 3, '4': {'5': 55, '6': 66, '7': 77}, '7': {'7': 777}}

def get_dict_value(in_dict, target_key, results=[], not_d=True):
    for key in in_dict.keys():  # 迭代当前的字典层级
        data = in_dict[key]  # 将当前字典层级的第一个元素的值赋值给data
        
		# 如果当前data属于dict类型, 进行回归
        if isinstance(data, dict):
            get_dict_value(data, target_key, results=results, not_d=not_d)
            
		# 如果当前键与目标键相等, 并且判断是否要筛选
        if key == target_key and isinstance(data, dict) != not_d:
            results.append(in_dict[key])

    return results
————————————————
版权声明：本文为CSDN博主「NeroAsmar」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/liaowhgg/article/details/88370472






for case in data3M:
    if 'steth_20190307_08_49_55' in ['8036a885518603528882b34e74d66ed3']['b1eede743128ad0cfb3915f55daa206d']['fileName']:
        print('find it!')
        # print(data3M['8036a885518603528882b34e74d66ed3']['b1eede743128ad0cfb3915f55daa206d']['bedNumber'])
        # print(data3M['8036a885518603528882b34e74d66ed3']['b1eede743128ad0cfb3915f55daa206d']['metaData'])
        break
    else:
        print('No data')
        break
        

# a = data3M['8036a885518603528882b34e74d66ed3']['b1eede743128ad0cfb3915f55daa206d']['fileName']
# b = data3M['8036a885518603528882b34e74d66ed3']['b1eede743128ad0cfb3915f55daa206d']['bedNumber']
# c = data3M['8036a885518603528882b34e74d66ed3']['b1eede743128ad0cfb3915f55daa206d']['metaData']

# print(a)
# print(b)
# print(c)

# print(data3M)
# print(data3M.keys())
# print()
# print(data3M.values())
# print()
# print(data3M.items())

print()
print('end')


# ----- get all wav name
target_key = 'fileName'
def getvalue(data3M, target_key, wavname=[], isdict=True):    # 在變數裡面有等號 就是默認 可以不用輸入值   !!!【沒有被定義的值，要放在前面】
    for key in data3M.keys():  # get key
        data = data3M[key] # data = 1set of 8wav
        if isinstance (data, dict):
            getvalue(data, target_key, wavname=wavname, isdict=isdict)  # back to key, value
        if key == target_key and isinstance(data, dict) != isdict:  # if key is target, add value 
            wavname.append(data)
    return wavname
         
name = getvalue(data3M, target_key) # name = all wav name
print(name)


# Python bytecode 3.7 (3392)
# 




列出資料夾名稱
#-------------------------------------------------------------------------------------

from os import listdir
from os.path import isfile, isdir, join

# 指定要列出所有檔案的目錄
#mypath = "C:\\Tzu-Ling\\pytry\\txt"
#mypath = "G:\\我的雲端硬碟\\臨床部\\[臨床部]-[FA1胸音計畫]\\[胸音計劃]-[聲音分析]\\[音訊] -[資料庫與院內收集]\\[臨床部]-[已標註聲音]\\[已標註]-[喉音]"
mypath = r'G:\我的雲端硬碟\臨床部\[臨床部]-[FA1胸音計畫]\[胸音計劃]-[聲音分析]\[音訊] -[資料庫與院內收集]\[臨床部]-[已標註聲音]\[已標註]-[喉音]'


# 取得所有檔案與子目錄名稱
files = listdir(mypath)

# 以迴圈處理
for f in files:
  # 產生檔案的絕對路徑
  fullpath = join(mypath, f)
  # 判斷 fullpath 是檔案還是目錄
  if isfile(fullpath):
    #print("檔案：", f)
    print(f)
  elif isdir(fullpath):
    #print("目錄：", f)
    print(f)




#-------------------------------------------------------------------------------------



from os import walk

# 指定要列出所有檔案的目錄
#mypath = "C:\\Tzu-Ling\\pytry\\txt"
mypath = "G:\\我的雲端硬碟\\臨床部\\[臨床部]-[FA1胸音計畫]\\[胸音計劃]-[聲音分析]\\[音訊] -[資料庫與院內收集]\\[臨床部]-[已標註聲音]\\[已標註]-[喉音]"


# 遞迴列出所有子目錄與檔案
for root, dirs, files in walk(mypath):
  print("路徑：", root)
  print("  目錄：", dirs)
  print("  檔案：", files)

#-------------------------------------------------------------------------------------




def 函數功能(變數)

每一次調用這個函數時，都要給定變數(argument)


# 文件讀寫

text = 'hello!'

myfile = open('123.txt','w')  # write
myfile.write(text)
myfile.close()

addtext = 'addadd'
myfile = open('123.txt','a') # append
myfile.write(addtext)
myfile.close()

file = open('123.txt','r') # read
content = file.read()   #<< read 讀全部  輸出結果和txt一樣
content = file.readline() #<< readline 讀一行
content = file.readlines() #<< readlines 讀每一行  輸出結果會是list ['aaa\n','bbb\n',]

print(content)



# class 類 的定義功能
首先定義calss

class Calculator:
    name = 'Good calculator'   # <<<<此類的屬性  (固有屬性(默認屬性))
    price = 18
    def add(self,x,y):
        print(self.name)
        result = x+y
        print(result)
    def minus(self,x,y):
        result = x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)


calcu = Calculator()   # <<<個體calcu = 屬性Calculator
calcu.name  #>>>'Good calculator'
calcu.price #>>>18

calcu.add(10,11) #>>>21



# init 初始

class Calculator:
    def __init__(self,name,price,hight,width,weight): # 給定屬性
        self.name = name
        self.p = price
        self.h = hight
        self.wi = width
        self.we = weight
        self.add(1,2)  #初始就先定義用這個功能
    def add(self,x,y):
        print(self.name)
        result = x+y
        print(result)
    def minus(self,x,y):
        result = x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)

https://www.youtube.com/watch?v=GxMm82yy2Ds&list=PLXO45tsB95cIRP5gCi8AlYwQ1uFO2aQBw&index=19



numpy 
pandas 矩陣運算


import pandas as pd

excelpath = "D:\\LargeD\\Python_py\\sound_database\\for_main_json.xlsx"

df = pd.read_excel(excelpath)

a = df.head(2) #只讀取前兩列資料

print(a)




# Test Web vsCode

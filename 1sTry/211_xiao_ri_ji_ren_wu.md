# 2.1.1 小日记任务

## 任务描述

> 完成一个极简交互式日记系统，需求如下：
> * 一次接收输入一行日记
* 保存为本地文件
* 再次运行系统时,能打印出过往的所有日记


### 挖坑：
      1. 如何向文本添加内容不删除或者覆盖原来内容
      
      2. 读写文件的基础知识
      
      3. 如何每次记录每次写完日记的时间，且在下次打开系统时能展示
      
      4. 文本换行
      
     

### 填坑


1.'a' 表示要向文件写入数据，但是添加到当前内容尾部
> 参考：https://www.ibm.com/developerworks/cn/opensource/os-python8/
                
 2 . 获取时间
 
 > 参考：http://justcoding.iteye.com/blog/901758
 
 
 
 
 
 
 
### 代码

> *# coding:utf-8   #解决中文字符问题
from sys import argv
import time #导入time 模块
import os
  
script, filename = argv
os.path.isfile(filename)  # txt = open(filename) #读取内容需先将其打开

print "这是 %r 的内容:" % filename
# print txt.read() #读取内容

print "If you don't want that, hit CTRL-C (^C)."
print "IF you do want this, hit return."

raw_input("?")
    
print "Opening the file..."
target = open(filename,"a") # 'a' 表示要向文件写入数据，但是添加到当前内容尾部


print "输入新的内容:"

content = raw_input("line 1: ")

T = time .strftime('%Y-%m-%d %A %X %Z', time.localtime()) # 显示当下时间

print T

print "I'm going to write these to the file."

target.write('\n' + content + '\n' + "---"+ T)


print "And finally, we close it."
target = open(filename)

print target.read()
target.close()
# txt.close() # close 能否不用?
# coding:utf-8   #解决中文字符问题
from sys import argv
import time #导入time 模块
import os
  
script, filename = argv
E = os.path.exists(filename) #判断filename是否存在 

if str(E) == 'True': #str 可将数据转化为字符串
    txt = open(filename) #读取内容需先将其打开
    print '这是 %r 的内容：' % filename 
    print txt.read()  # 每次运行自动打印之前的记录
else:
    print '尚无 %r ---创建之...' % filename
    
    # ---以下输入内容并保存---
    

print "If you don't want that, hit CTRL-C (^C)."
print "IF you do want this, hit return."

raw_input('> ')
    
print "Opening the file..."
target = open(filename,"a") # 'a' 表示要向文件写入数据，但是添加到当前内容尾部


print "输入新的内容:"

content = raw_input("line 1: ")

T = time .strftime('%Y-%m-%d %A %X %Z', time.localtime()) # 显示当下时间

print T

print "I'm going to write these to the file."

target.write('\n' + content + '\n' +  "---"+ T)


print "And finally, we close it."
target = open(filename)

print target.read()
target.close()
# txt.close() # close 能否不用?

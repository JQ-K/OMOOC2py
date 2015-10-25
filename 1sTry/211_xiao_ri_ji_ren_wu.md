# 2.1.1 小日记任务

## 任务描述

> 完成一个极简交互式日记系统，需求如下：
> * 一次接收输入一行日记
* 保存为本地文件
* 再次运行系统时,能打印出过往的所有日


### 挖坑：
      1. 如何向文本添加内容不删除或者覆盖原来内容
      
      2. 读写文件的基础知识
      
      3. 如何每次记录每次写完日记的时间，且在下次打开系统时能展示
      
      4. 文本换行
      
      5.打开系统自动打印之前的所有记录，如果没有这个文件进行创建
     

### 基本思路：

>* 代码不只是自己使用，别人第一次运行要确保其能创建一个新的日记文件并且保存 

> * 所以代码第一部分需要判断有没有这个日记文件，需要用到 os.path.exists()命令进行判断

> * 如果存在打开读取文件不存在创建文件使 if 函数，打开读取使用open/read 命令

> 代码如下

>     coding:utf-8  
    from sys import argv
    import time 
    import os    
    script, filename = argv
    E = os.path.exists(filename) 
    if str(E) == 'True': 
        print txt.read()  
    else:
        print '尚无 %r ---创建之...' % filename



>* 第二大块内容是写入需用 raw_input()

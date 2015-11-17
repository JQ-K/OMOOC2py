# 随手记

try
捕获由Python或程序本身引发的异常
raise
手工地引发一个异常
为什么要使用异常

错误处理，当python检查以程序运行时的错误就引发异常，你可以在程序里捕捉和处理这些错误，或者忽略它们。
事件通知，异常也可以作为某种条件的信号，而不需要在程序里传送结果标志或显式地测试它们。
特殊情形处理，有时有些情况是很少发生的，把相应的处理代码改为异常处理会更好一些。
奇特的控制流，异常是一个高层次的"goto"，可以把它作为实现奇特的控制流的基础。如反向跟踪等。
异常的基础知识

python的try语句有两种风格---一种是处理异常（try/except/else），一种是无论是否发生异常都将执行最后的代码（try/finally）。

try/except/else风格

      try:
      <语句>        #运行别的代码
      except <名字>：
      <语句>        #如果在try部份引发了'name'异常
      except <名字>，<数据>:
      <语句>        #如果引发了'name'异常，获得附加的数据
      else:
      <语句>        #如果没有异常发生
      
try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。

如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引发新的异常）。
如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印缺省的出错信息）。
如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。
try/finally风格

      try:
      <语句>
      finally:
      <语句>    #退出try时总会执行
      raise
      
python总会执行finally子句，无论try子句执行时是否发一异常。

如果没有发生异常，python运行try子句，然后是finally子句，然后继续。
如果在try子句发生了异常，python就会回来执行finally子句，然后把异常递交给上层try，控制流不会通过整个try语句。
当你想无论是否发生异常都确保执行某些代码时，try/finally是有用的。

raise

要引发异常，你需要写raise语句，它的形式很简单，raise后面跟着要引发的异常。

      raise <name>    #手工地引发异常
      raise <name>,<data>    #传递一个附加的数据
      
什么是异常名（name）呢？它也许是内置作用域内的内置异常（如IndexError），或者是你程序中的任意字符串对象。

缺省行为：显示错误信息。

      $ python test.py
      Traceback (innermost last):
      File "test.py", line 3, in ?
      a = 1 /0
      ZeroDivisionError: integer division or modulo
      
当一个未捕获的异常发生时，python将结束程序并打印一个堆栈跟踪信息，以及异常名和附加信息。

用try捕获内置异常

如果你不想在异常发生时结束你的程序，只需在try里捕获它。

      #!/usr/bin/python
      try:
          a = 1 /0
          print a
      except:
          print 'i get the error'
      
当程序运行是会捕获一个错误并执行except后面的代码。

异常的惯用法

异常并不总是坏事情，例如，文件对象的read方法在文件尾时返回一个空串，python也提供一个内置函数raw_input，它从标准输入流读入。与read方法不同，当遇到文件尾时，raw_input()引发内置的EOFError错误。所以可以这样用：

      while 1:
          try:
              line = raw_input()      #从stdin读入行
          except EOFError:
              break                #在文件末尾退出循环
          esle:
              # 其它处理代码
      
用异常传递成功的信号

      Found = 'item found'
      def search():
      引发或返回Found
        try:
            search()
         except Found:
            successful
         else:
            fail
      
可以使用try来调试代码，你可以用自已的异常处理替换python缺省的异常处理。把整个程序封装在一个外部try里面，你可以捕获运行时的任何异常。

异常捕获模式

      try语句子句形式表
      except:            捕获所有异常
      except name:        只捕获特定的异常
      except name,value:    捕获异常和它的附加数据
      except (name1,name2):    捕获任何列出的异常
      else:            如果没有异常
      finally:        总是执行
       
捕获多个异常中的一个，python从上到下地查看except子句，括号里列出多个异常与列出单独的异常是一样的，只是更简洁一些。

运行时嵌套的异常，python会匹配最近的except。

finally子句无论如何都会执行，所以它是做清除动作的好地方，如关闭一个文件的操作。

捕捉所有异常

try:
   # 你的代码
except BaseException, e:
   print(str(e))

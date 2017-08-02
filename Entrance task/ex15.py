#coding=utf-8
from sys import argv#引入sys模组


script,filename=argv#从用户侧获得脚本名和文件名

txt=open(filename)#打开用户输入的文件名的文件


print " Here's your file %r:" %filename#提示用户他输入的文件名
print txt.read()#输入用户指定文件名的文件内容
txt.close()
print "Type the filename again:"#输入请再次输入文件名
file_again=raw_input(">")#输入>并读入用户输入的文件名到变量file_again中

txt_again=open(file_again)#打开用户再次输入的文件名的文件

print txt_again.read()#输入用户指定文件名的文件内容
txt_again.close()
#输入代码的过程中，每一行要顶格书写，否则无法编译通过

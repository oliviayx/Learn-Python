#coding=utf-8
tabby_cat="\tI'm tabbed in."#\t是制表符
persian_cat="I'm split\non a line."#\n换行
backslash_cat="I'm \\a\\cat."#\\转义\

fat_cat='''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass 
'''
#转义符可以连续写
#使用双引号和单引号效果一样，在Python中单引号同双引号
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
tty="%r"
ttu='%s'
print tty % "table in"
print ttu % "table"
print '''
What\'t is your name
My name is Lilei
 haha
'''

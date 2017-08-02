#coding=utf-8
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" %cheese_count
    print "You have %d boxes of crackers!" %boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50 #定义两个变量并给它们赋值

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #调用函数，使用变量给函数参数赋值


print "We can even do math inside too:" #输出我们将算数结果作为函数的参数

cheese_and_crackers(10+20,5+6) #调用函数，函数的参数是通过算数计算得到的


print "And we can combine the two, variables and math:" #输出我们将变量和算数结合来作为函数的参数
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #调运函数，函数的参数赋值可以是变量和算数结合

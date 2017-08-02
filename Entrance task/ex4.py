# coding=utf-8 
# 需要加入注释是添加此行
# 定义cars变量
cars=100
# 定义每辆车的座位数
space_in_a_car=4.0
# 定义驾驶员数量
drivers=30
# 定义乘客数量
passengers=90
# 定义不能驾驶的汽车数量等于汽车总是减去驾驶员数量
cars_not_driven=cars-drivers
# 定义可以驾驶的汽车数量等于驾驶员数量
cars_driven=drivers
# 定义汽车容量等于可以驾驶的汽车数乘以每辆车的座位数
carpool_capacity=cars_driven*space_in_a_car
# 定义每辆车的平均乘客数等于乘客总数除以可驾驶的汽车数
average_passgers_per_car=passengers/cars_driven


# 输出可用汽车数量
print "There are",cars, "cars available."
# 输出只有多少个驾驶员
print "There are olny",drivers,"drivers available."
# 输出我们今天有多少量空车
print "There will be", cars_not_driven, "empty cars today."
# 输出我们今天能运输多少人
print "We can transport",carpool_capacity,"people today."
# 输出我们今天的乘客数
print "We have", passengers,"to carpool today."
# 输出平均每辆车多少人
print "We need to put about", average_passgers_per_car,"in each car."

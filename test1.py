money = 50
print("当前钱包余额：",money)
money = money - 10 - 10
print("购买了冰激凌，花费",10,"元")
print("购买了可乐，花费：",10,"元")
print("最终钱包剩余：",money,"元")

#print输出数据类型
print(type("购买冰激凌"))
print(type(money))
print(type(114.514))

#使用变量存储type（）语句的结果

string_type = type("特雷西娅")
int_type = type(618)
float_type = type(4.28)
print(string_type)
print(int_type)
print(float_type)

#使用type()语句，查看变量存储的数据类型信息

name = "特蕾西娅"
name_type = type(name)
print(name_type)

#将数字类型转换成字符串

num_str = str(114)
print(type(num_str),num_str)

#将字符串转数字

num = int("514")
print(type(num),(num))

num2 = float("11.45")
print(type(num2),(num2))

"""
标识符
1.内容限定，不能以数字开头，以英文为主
2.大小写敏感
3.不可使用关键字
"""
name_1 = "特蕾西娅"
print(name_1)

num = 1 + 2 * 3

num = 1
num += 1
print(num)
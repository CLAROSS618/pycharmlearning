"""
三种字符串定义法
-单引号定义法
-双引号定义法
-三引号定义法
"""
name = '特蕾西娅'
print(type(name))

name = "特蕾西娅"
print(type(name))

name = """
特
蕾
西
娅
"""
print(type(name))

#字符串的引号嵌套

name = '"特蕾西娅"'
print(name)
name = "'特蕾西娅'"
print(name)
name = "\"特蕾西娅\""
print(name)
name = '\'特蕾西娅\''
print(name)

name = "特蕾西娅"
message = "巴别塔领袖：%s" % name
print(message)

#占位符完成数字与字符串拼接
class_num = 23
avg_salary = 114514
message = "xjtlu生物信息学，苏州%s期，平均工资：%s" % (class_num, avg_salary)
print(message)

#格式化与精度控制
num1 = 11
num2 = 11.4514
print("数字11宽度限制5，结果是：%5d" % num1)
print("数字11宽度限制1，结果是：%1d" % num1)
print("数字11.4514宽度限制7，小数精度是2，结果是：%7.2f" % num2)
print("数字11.4514宽度不限制，小数精度是2，结果是：%.2f" % num2)

#格式化快速写法：f"{占位}"
name = "张政霖"
set_up_year = 2006
stock_price = 19.99
print(f"我是{name}，我成立于：{set_up_year}年，我今天的股价是：{stock_price}")

#表达式进行字符串格式化
print("1 * 1 的结果是：%d" % (1 * 1))
print(f"1 * 2的结果是：{1 * 2}")
print("字符串在python中的类型名是：%s" % type("字符串"))

#获取键盘的输入信息
name = input("输入名字以验证管理权限")
print("欢迎接入程序，管理员：%s" % name)

#输入数字类型
num = input("请输入你的银行卡密码：")
#数据类型转换
num = int(num)
print("你的银行卡密码的类型是：", type(num))
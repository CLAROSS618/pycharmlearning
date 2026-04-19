"""
str1 = "itheima"
str2 = "itcast"
str3 = "pychon"

count = 0
for i in str1:
    count += 1
print(f"字符串{str1}的长度是：{count}")

def welcome():
    print("欢迎来到防疫站")
    print("请出示你的健康证明及行程证明！")

welcome()
"""

"""
def add(x,y):
    result = x + y
    print(f"{x}+{y}的结果是：{result}")

add(9,8)
"""
def tem(x):
    if x <= 37.5:
        print(f"您的体温是:{x},请正常通行。")
    else:
        print(f"您的体温是:{x},需要隔离观察。")


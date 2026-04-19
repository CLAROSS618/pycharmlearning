def say_hi():
    print("hi")

result = say_hi()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")

#None用于if判断
def check_age(age):
    if age >= 18:
        return "SUCCESS"
    else:
        return None

result = check_age(20)
if not result:
    print("未满18岁，不可以进入酒吧")

#None声明无初始值的变量
name = None

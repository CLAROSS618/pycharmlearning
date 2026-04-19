# 定义一个函数，接收另一个函数作为传参
def test_func(computer):
    result = computer(1,2) # 确定comuter是函数
    print(f"computer参数的类型是：{type(computer)}")
    print(f"计算结果：{result}")

# 定义一个函数，准备作为参数传入另一个函数
def computer(x,y):
    return x + y
# 调用，并传参
test_func(computer)
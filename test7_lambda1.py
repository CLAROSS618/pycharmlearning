def test_func(computer):
    result = computer(1,2)
    print(f"结果是：{result}")
# 通过lambda的匿名函数的形式，将匿名函数传参
test_func(lambda x, y: x + y)

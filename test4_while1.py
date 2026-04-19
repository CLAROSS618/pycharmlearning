import random
num = random.randint(1,100)
#print(f"测试数据生成：{num}")
i = 0

while True:
    guess_num = int(input("请输入猜测的数字:"))
    i += 1

    if guess_num == num:
        print(f"猜对了，共猜了{i}次")
        break
    elif guess_num > num:
        print("猜大了，请再猜一次")
    else:
        print("猜小了，请再猜一次")
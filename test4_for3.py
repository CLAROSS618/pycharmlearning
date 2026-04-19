"""
for x in range(1,10):
    for y in range(1,x+1):
        print(f"{x}*{y}={x*y}",end="\t")
    print()
"""
"""
i = 0
j = 10000
for x in range(1,21):
    import random
    num = random.randint(1,10)
    if j == 0:
        print("工资发完了，下个月再领吧")
        break
    else:
        if num < 5:
            print(f"员工{i}，绩效分{num},低于5，不发工资，下一位。")
        else:
            j -= 1000
            print(f"向员工{i}发放工资1000元，账户余额还剩{j}元")

    i += 1
"""
import random  # 1. 放在最上面

money = 10000  # 账户余额

# 2. 直接用 i 代表员工编号，从 1 到 20
for i in range(1, 21):
    # 生成随机绩效
    score = random.randint(1, 10)

    # 3. 先判断钱够不够（关键修改：要判断是否小于1000，而不是等于0）
    if money < 1000:
        print("工资发完了，下个月再领吧")
        break  # 直接结束整个循环

    # 4. 判断绩效
    if score < 5:
        print(f"员工{i}，绩效分{score}，低于5，不发工资，下一位。")
        continue  # 跳过本次循环，去下一位员工
    else:
        # 发工资
        money -= 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩余{money}元")
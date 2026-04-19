import random
num = random.randint(1, 10)
print(f"调试用：答案是 {num}")

# --- 第 1 次 ---
guess = int(input("猜一个数字: "))  # 先存变量

if guess == num:
    print("猜对了！")
else:
    # 猜错了，利用变量判断大小
    if guess > num:
        print("大了")
    else:
        print("小了")

    # --- 第 2 次 ---
    guess = int(input("再猜一次: ")) # 再次存变量（覆盖旧值）

    if guess == num:
        print("猜对了！")
    else:
        # 再次判断大小
        if guess > num:
            print("大了")
        else:
            print("小了")

        # --- 第 3 次 ---
        guess = int(input("最后一次: "))

        if guess == num:
            print("猜对了！")
        else:
            if guess > num:
                print("大了")
            else:
                print("小了")
            print(f"游戏结束，答案是 {num}")

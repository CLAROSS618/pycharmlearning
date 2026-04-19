#if elif else 多条件判断语句的使用
if float(input("请输入你的身高（cm）")) < 120:
    print("身高小于120cm，可以免费。")
elif int(input("请输入你的VIP等级（1-5）")) > 3:
    print("vip级别大于3，可以免费。")
else:
    print("不好意思，您的免费条件不满足，需要缴纳30元")

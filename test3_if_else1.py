print("欢迎来到维多利亚蒸汽骑士展馆")
height_str = input("请输入您的身高(cm):")
height = float(height_str)
if height > 120:
    print("您的身高超出120cm，参观需缴纳20元。")
else:
    print("您的身高未超过120cm，可以免费游玩。")
print("祝您游玩愉快")

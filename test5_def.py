money = 5000000
name = str(input("请输入您的姓名："))

def check_money():
    print(f"{name},您好，您的余额剩余：{money}")

def input_money():
    global money
    i = int(input("请将存款放入存钱口中"))
    money += i
    print(f"{name},您好，您存款{i}元成功")
    return i

def draw_money():
    global money
    i = int(input("请输入想要取出的数额："))
    money -= i
    print(f"{name},您好，您取款{i}成功")
    return i

def main():
    while True:
        print(f"{name},您好，欢迎您来到龙门央行。请选择操作：")
        print("查询余额\t[输入1]")
        print("存款\t\t[输入2]")
        print("取款\t\t[输入3]")
        print("退出\t\t[输入4]")
        print("请输入您的选择：")
        choose = int(input())
        if choose == 1:
            check_money()
        elif choose == 2:
            input_money()
            check_money()
        elif choose == 3:
            draw_money()
            check_money()
        elif choose == 4:
            print("感谢您使用龙门央行系统，祝您生活愉快！")
            break
        else:
            print("输入错误，请按提示输入")
main()
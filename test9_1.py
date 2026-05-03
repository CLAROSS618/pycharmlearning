# 基本捕获语法
try:
    f = open("D:/abc.txt", "r", encoding="utf-8")
except:
    print("出现bug了，文件不存在,使用w模式打开")
    f = open("D:/abc.txt", "w", encoding="utf-8")

# 捕获指定的异常
try:
    print(name)
except NameError as e:
    print("出现了变量未定义的异常")
    print(e)
# 捕获多个异常
try:
    #1 / 0
    print(name)
except (NameError, ZeroDivisionError) as e:
    print("出现了变量未定义或者除以0的异常")
    print(e)

# 未正确设置捕获异常类型，将无法捕获异常
# 捕获所有异常
try:
    # print("name")
    print(name)
except Exception as e:
    print("出现异常了")
else:
    print("没有异常")
finally:
    f.close()

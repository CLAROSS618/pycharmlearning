# 打开文件
f = open("D:/测试.txt", "r", encoding="UTF-8", newline='')
print(type(f))

# 读取文件-read（）
print(f"读取十个字节的结果：{f.read(10)}")
print(f"read方法读取全部内容的结果是：{f.read()}")
print("-------------------------------------------")
f.seek(0)

# 读取文件-readlines()-读取文件全部行并封装到列表中
lines = f.readlines()
print(f"lines对象的类型是：{type(lines)}")
print(f"lines的对象内容是：{lines}")
f.seek(0)

# 读取文件-readline-一次读取一行
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行的数据是：{line1}")
print(f"第二行的数据是：{line2}")
print(f"第三行的数据是：{line3}")
f.seek(0)

# for循环读取文件行
for line in f:
    print(f"每一行数据是：{line}")
f.seek(0)

# 文件的关闭
f.close()

# with open 语法操作文件-执行完后自动关闭文件
with open("D:/测试.txt", "r", encoding="UTF-8", newline='') as f:
    for line in f:
        print(f"每一行数据是：{line}")


count = 0
with open("D:/测试.txt", "r", encoding="UTF-8") as f:
    for line in f:
        count += line.split().count('itheima')

print(f"itheima出现的次数为：{count}")

# 定义元组
t1 = (1,"hello",True)
t2 = ()
t3 = tuple()
print(f"t1的类型是：{type(t1)},内容是：{t1}")
print(f"t2的类型是：{type(t2)},内容是：{t2}")
print(f"t3的类型是：{type(t3)},内容是：{t3}")

# 定义单个元素的元组(加个单独逗号)
t4 = ("hello",)
print(f"t4的类型是：{type(t4)},内容是：{t4}")

# 元组的嵌套
t5 = ((1,2,3),(4,5,6))
print(f"t5的类型是：{type(t5)},内容是：{t5}")

# 下标索引取出内容
num = t5[1][2]
print(f"从嵌套元组中取出的数据是：{num}")

# 元组的操作
t6 = ("W","伊内斯","赫德雷")
index = t6.index("W")
print(f"在元组t6中查找W的下标是：{index}")

t7 = ("W","伊内斯","赫德雷","W","W","W","W")
num = t7.count("W")
print(f"在元组t7中统计W的数量有：{num}个")

t8 = ("W","伊内斯","赫德雷","W","W","W","W")
num = len(t8)
print(f"t8元组中的元素有：{num}个")

# 元组的遍历(while)(for)
index = 0
while index < len(t8):
    print(f"元组的元素有：{t8[index]}")
    index += 1

for element in t8:
    print(f"2元组的元素有：{element}")

# 元组定义后内容不可修改

t9 = ('周杰伦',11,['football','music'])
num = t9.index(11)
name = t9[0]
t9[2].remove('football')
t9[2].append('coding')
print(f"年龄所在的下标位置是：{num},查询学生的姓名是：{name},删除学生爱好中的football后列表的内容是：{t9}")
print(f"增加爱好coding后列表的内容是：{t9}")

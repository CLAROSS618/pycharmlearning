mylist = ["itcast","itheima","python"]
# 查找某元素在列表内的下标索引
index = mylist.index("itheima")
print(f"itheima在列表中的下标索引是：{index}")
# 查询的元素不存在则会报错

# 修改特定下标索引的值
mylist[0] = "lemon"
print(f"列表被修改元素后，结果是：{mylist}")

# 插入元素的写法
mylist.insert(1,"apple")
print(f"列表中插入元素后，结果是：{mylist}")

# 追加元素的写法
mylist.append("banana")
print(f"列表中追加元素后，结果是：{mylist}")

# 追加元素方法2
mylist2 = [1,2,3]
mylist.extend(mylist2)
print(f"列表中追加一个新的列表后，结果是{mylist}")

# 元素的删除
del mylist[3]
print(f"列表删除元素后的结果是：{mylist}")
element = mylist.pop(2)
print(f"通过pop方法取出元素后列表内容：{mylist},取出的元素是：{element}")

# 指定元素内容进行删除
mylist.remove(3)
print(f"通过remove方法移除元素后，列表的结果是：{mylist}")

# 清空列表
mylist.clear()
print(f"列表被清空了，结果是：{mylist}")

# 统计列表内某些元素的数量
mylist = ["itcast","itheima","python"]
count = mylist.count("itheima")
print(f"列表中itheima的数量是：{count}")

# 统计列表内的元素数量
mylist = ["itcast","itheima","python"]
count = len(mylist)
print(f"列表中的元素总量总共有{count}个")

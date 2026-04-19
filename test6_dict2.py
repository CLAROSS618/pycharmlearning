# 字典内新增元素
my_dict = {"W":40,"伊内斯":75,"赫德雷":95}
my_dict["42"] = 66
print(f"经过新增元素后结果是：{my_dict}")

# 更新元素
my_dict["W"] = 20
print(f"字典经过更新后结果是：{my_dict}")

# 删除元素
score = my_dict.pop("W")
print(f"字典中被移除一个元素后结果是：{my_dict},W的考试分数是：{score}")

# 清空元素clear
my_dict.clear()
print(f"字典清空了，结果是：{my_dict}")

# 获取全部的key
my_dict = {"W":40,"伊内斯":75,"赫德雷":95}
keys = my_dict.keys()
print(f"字典的全部key是：{keys}")

# 遍历字典
# 方法1：通过获取全部key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")
# 方法2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

# 统计字典内的元素数量
num = len(my_dict)
print(f"字典内的元素数量是：{num}")

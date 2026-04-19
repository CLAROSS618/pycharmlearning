# 定义字典
my_dict1 = {"W":40 , "伊内斯":75 , "赫德雷":95}
# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是：{my_dict1},类型：{type(my_dict1)}")
print(f"字典2的内容是：{my_dict2},类型：{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3},类型：{type(my_dict3)}")

# 字典无法重复
# 从字典中基于key获取value
my_dict1 = {"W":40 , "伊内斯":75 , "赫德雷":95}
score = my_dict1["W"]
print(f"w的考试分数是：{score}")

# 字典的key和value可以为任意数字类型（key不可为字典）
# 定义嵌套字典
stu_score_dict = {
    "W": {
        "历史": 40,
        "物理": 70,
        "化学": 90,
    }, "赫德雷": {
        "历史": 90,
        "物理": 40,
        "化学": 40,
    }, "伊内斯": {
        "历史": 60,
        "物理": 60,
        "化学": 70
    }
}
print(f"学生的考试信息是：{stu_score_dict}")

# 从嵌套字典中获取数据
score = stu_score_dict["W"]["历史"]
print(f"W的历史分数是：{score}")

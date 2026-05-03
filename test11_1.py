# 设计一个类（类比生活中：设计一张登记表）
class Student:
    name = None         # 记录学生姓名
    gender = None       # 记录学生性别
    nationality = None  # 记录学生国籍
    native_place = None # 记录学生籍贯
    age = None          # 记录学生年龄

# 创建一个对象（类比生活中：打印一张登记表）
stu_1 = Student()

# 对象属性赋值（类比生活中：填写表单）
stu_1.name = "特蕾西娅"
stu_1.gender = "女"
stu_1.nationality = "卡兹戴尔"
stu_1.native_place = "未知"
stu_1.age = 105

# 获取对象中的记录信息
print(stu_1.name)
print(stu_1.gender)
print(stu_1.nationality)
print(stu_1.native_place)
print(stu_1.age)
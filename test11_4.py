# 构造方法的名称：__init__

class Student:
    name = None
    age = None
    tel = None

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创造了一个类对象")

stu = Student("特蕾西娅", 105, "000000001")
print(stu.name)
print(stu.age)
print(stu.tel)


class Student1:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

for i in range(10):

    print(f"当前录入第{i+1}位学生的信息，总共需录入10位学生信息")
    stu1 = str(input("请输入学生姓名："))
    stu2 = int(input("请输入学生年龄："))
    stu3 = str(input("请输入学生地址"))
    stu = Student1(stu1, stu2, stu3)
    print(f"学生{i+1}信息录入完成，信息为：【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.address}")

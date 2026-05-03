# 定义一个带有成员方法的类
class Student:
    name = None     # 学生姓名

    def say_hi(self):
        print(f"大家好呀，我是{self.name}，欢迎大家多多关照")

    def say_hi2(self, msg):
        print(f"大家好，我是{self.name}, {msg}")


stu = Student()
stu.name = "特蕾西娅"
stu.say_hi2("1")

stu = Student()
stu.name = "伊内斯"
stu.say_hi2("2")


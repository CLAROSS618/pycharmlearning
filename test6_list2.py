student_age = [21,25,21,23,22,20]

student_age.append(31)
print(f"追加一个数字31后，列表的内容是：{student_age}")

student_age2 = [29,33,30]
student_age.extend(student_age2)
print(f"追加一个新列表后，列表的内容是：{student_age}")

del student_age[0]
print(f"用del方法删除=第一个元素后，列表的内容是：{student_age}")

element = student_age.pop(-1)
print(f"用pop方法删除最后一个元素后，列表的内容是：{student_age}。删除的元素是：{element}")

index = student_age.index(31)
print(f"元素31在列表中的下标是：{index}")

# 使用while循环遍历列表
def list_while_func():
    my_list = [1,2,3]
    index = 0  # 初始下标为0
    while index < len(my_list):
        element = my_list[index]
        print(f"列表的元素：{element}")
        index += 1


# 使用for循环遍历列表
def list_for_func():
    my_list = [1,2,3,4,5,6,7]
    for element in my_list:
        print(f"列表的元素有：{element}")


def list_while_func1():
    my_list = [1,2,3,4,5,6,7,8,9,10]
    my_list2 = []
    index = 0
    while index < len(my_list):
        element = my_list[index]
        if element % 2 == 0:
           my_list2.append(element)
        index += 1
    print(f"列表中的偶数组成的新列表是：{my_list2}")

list_while_func1()

def list_for_func1():
    my_list = [1,2,3,4,5,6,7,8,9,10]
    my_list2 = []
    for element in my_list:
        if element % 2 == 0:
            my_list2.append(element)
    print(f"列表中的偶数组成新的列表是：{my_list2}")

list_for_func1()

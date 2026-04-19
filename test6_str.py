# 字符串的下标索引
my_str = "itheima and itcast"
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素的值是：{value},取下标为-16的值是：{value2}")

# index方法
value = my_str.index("and")
print(f"从字符串中查找and，其起始下标是：{value}")

# replace方法（字符串的替换）
new_my_str = my_str.replace("it","程序")
print(f"将字符串{my_str}进行替换后得到：{new_my_str}")

# split方法（分割字符串）
my_str = "hello python inheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到：{my_str_list},类型是：{type(my_str_list)}")

# strip方法（规整字符串）
my_str = "  itheima  and  itcast   "
new_my_str = my_str.strip() # 不传入参数，去除首尾空格
print(f"字符串{my_str}被strip后的结果是：{new_my_str}")

my_str = "12itheima  and  itcast21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip（'12'）后的结果是：{new_my_str}")

# 统计字符串中某字符串的出现次数（count方法）
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it的出现次数是：{count}")

# 统计字符串的长度（len函数）
num = len(my_str)
print(f"字符串{my_str}的长度是：{num}")

my_str3 = "itheima itcast boxuegu"
count = my_str3.count("it")
my_str4 = my_str3.replace(" ","|")
my_str_list2 = my_str4.split("|")
print(f"字符串{my_str3}中有：{count}个it字符")
print(f"字符串{my_str3}，被替换空格后，结果：{my_str4}")
print(f"字符串{my_str3},按照|分隔后，得到：{my_str_list2}")

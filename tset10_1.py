import json

from my_utils import file_util

# 准备列表，列表内每一个元素都是字典，将其转化为json
data = [{"name": "伊内斯", "age": 40}, {"name": "赫德雷", "age": 42}, {"name": "W", "age": 33}]
json_str = json.dumps(data, ensure_ascii=False) # 包含中文后使用
print(type(json_str))
print(json_str)

# 准备字典，将字典转换为json
d = {"name": "特蕾西娅", "addr": "卡兹戴尔"}
json_str = json.dumps(d, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将json字符串转换为python数据类型[{k: v, k: v}, {k: v, k: v}
s = '[{"name": "伊内斯", "age": 40}, {"name": "赫德雷", "age": 42}, {"name": "W", "age": 33}]'
l = json.loads(s)
print(type(l))
print(l)

# 将json字符串转换为python数据类型{k: v, k: v}
s = '{"name": "特蕾西娅", "addr": "卡兹戴尔"}'
d = json.loads(s)
print(type(d))
print(d)

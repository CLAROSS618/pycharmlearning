# 导入自定义模块使用
# import my_model1
# my_model1.test(1, 2)

# from my_model1 import test
# test(1, 2)

# 导入不同模块的同名功能
# from my_model1 import test
# from my_model2 import test
# test(1, 2)

# __main__ 变量
from my_model1 import test

# _all_ 变量
from my_model1 import *
test_a(1, 2)
test_b(1, 2)
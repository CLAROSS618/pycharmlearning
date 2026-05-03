# 导入time模块
import time

# 打开文件，不存在的文件，r，w，a（w模式会自动创建）
f = open("D:/text.txt", "w", encoding="UTF-8")

# write写入
f.write("Hello World")    # 内容导入到内存中

# flush刷新
f.flush()                 # 将内存中的内容写入硬盘文件中

# close关闭
f.close()                 # close方法，内置了flush的功能的

# 打开一个存在的文件（文件存在则会清空内容并将新内容写入硬盘）

# write写入，flush刷新

# close关闭
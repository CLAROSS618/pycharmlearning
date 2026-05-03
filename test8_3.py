# 打开文件，不存在的文件
f = open("D:/test2.txt", "a", encoding="UTF-8")

# write写入
f.write("特蕾西娅")

# flush刷新
f.flush()

# close关闭
f.close()

# 调用已存在的文件，a模式会在后面追加写入的内容，不会删除原来的内容
# 换行写入使用\n

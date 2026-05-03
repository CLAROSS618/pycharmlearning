r = open("D:/bill.txt", "r", encoding="UTF-8")
w = open("D:/bill.txt.bak", "w", encoding="UTF-8")

for line in r:
    line.strip()
    if "测试" in line:
        continue
    w.write(line + "\n")

r.close()
w.close()

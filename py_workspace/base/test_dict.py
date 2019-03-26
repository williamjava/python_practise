d = {"Zhangsan":100,"Lisi":99,"Wangwu":88}
print(d["Zhangsan"])

d["Zhaoliu"]=66
print(d)

print(d.get("Lisi"))
d.pop('Zhaoliu')
print(d)
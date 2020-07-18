import json

diction = {
    "name": "aa",
    "phonenumber": 13305958697865,
    "grade": "3class"}

print(diction)  # 原文件格式为字典
d1 = json.dumps(diction)  # 将字典转换为字符串
print(d1)
d2 = json.loads(d1)  # 将字符串转换为字典
print(d2)
print('d', type(diction))
print('d1', type(d1))
print('d2', type(d2))
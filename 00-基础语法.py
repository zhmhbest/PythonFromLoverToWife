# 注释1

print(end='')

'''
注释2
'''

print(end='')

"""
注释3
"""
# ------------------------------


print("【变量定义与删除】")
var1 = 'variable'
del var1
try:
    print(var1)
except NameError:
    print('Undefined Variable!')
# end try
print('-'*30)
# ------------------------------

print("【交换变量的值】")
var1 = 1
var2 = 2
var1, var2 = var2, var1
print('var1 =', var1)
print('var2 =', var2)
print('-'*30)
# ------------------------------


print("【基础数据类型】")
number1 = 666           # 整型
number2 = 3.1415926     # 浮点型
# 字符串
string1 = "String"
string2 = 'string'
string3 = """STT
ing"""
string4 = '''str
ING'''
string5 = r"C:\Windows"
string6 = r'C:\C:\Program Files'
# Bytes
string7 = b'ABC'
string8 = b"ABC"
print(type(number1), number1)
print(type(number2), number2)
print(type(string1), string1)
print(type(string2), string2)
print(type(string3), string3)
print(type(string4), string4)
print(type(string5), string5)
print(type(string6), string6)
print(type(string7), string7)
print(type(string8), string8)
print('-'*30)
# ------------------------------


print("【同物判断、等值判断】")
obj1 = {}
obj2 = {}
obj3 = obj2
if obj1 is obj2:
    print('obj1和obj2是一个东西')
else:
    print('obj1和obj2不是一个东西')
# end if
if obj1 == obj2:
    print('obj1和obj2的值相同')
else:
    print('obj1和obj2的值不同')
# end if
if obj2 is obj3:
    print('obj2和obj3是一个东西')
else:
    print('obj2和obj3不是一个东西')
# end if
print('-'*30)
# ------------------------------


print("【基础运算】")
# + - * /
print('整除: 10 // 3 =', 10 // 3)
print('取余: 10 % 3 =', 10 % 3)
print('乘方: 2 ** 8 =', 2 ** 8)
print('等于:', 1 == 2)
print('不等:', 1 != 2)
index = 0  # 赋值
index += 1
index *= 2
print('自运算:', index)
print('and:', True and True)
print('or:', True or False)
print('not:', not False)
print('-'*30)
# ------------------------------


print("【字符串切片】")
string_test = "0123456789"
print('删头:', string_test[2:])
print('删尾:', string_test[:-2])
print('Left:\t', string_test[:3])
print('Right:\t', string_test[-3:])
print('Mid:\t', string_test[1:3])
print('Mid:\t', string_test[3:7])
print('-'*30)
# ------------------------------


print("【数据结构-元组】")
# 元组是只读的列表
tuple1 = (1, 2, 3)
tuple2 = tuple()  # 定义空元组
tuple3 = ()  # 定义空元组
print(type(tuple1), tuple1)
print(type(tuple2), tuple2)
print(type(tuple3), tuple3)
print('-'*30)
# ------------------------------


print("【数据结构-集合】")
set0 = set()  # 定义空set
print(type(set0), set0)
#
set1 = {1, 2, 3}
set1.add(3)  # set内容不能重复，此行将不产生任何影响
set1.add(4)
set1.add(5)
print(type(set1), set1)
set1.remove(5)  # 从中删除指定的元素
ele = set1.pop()  # 弹出最左边的元素
print("pop:", ele)
set2 = {3, 4, 5}
#
print(type(set1), set1)
print(type(set2), set2)
print('并集:\t', set1 | set2)
print('交集:\t', set1 & set2)
print('差集1:\t', set1 - set2)
print('差集2:\t', set2 - set1)
print('并差集:\t', set1 ^ set2)
print('-'*30)
# ------------------------------


print("【数据结构-列表】")
list1 = [4, 5, 6]
list2 = list()  # 定义空列表
list3 = []  # 定义空列表
list1.append(7)  # 向列表追加元素
list1.append(8)  # 向列表追加元素
ele = list1.pop()  # 弹出最右边的元素
print("pop:", ele)
print(type(list1), list1)
print(type(list2), list2)
print(type(list3), list3)
# 从元组创建列表
list_from_tuple = list(tuple1)
print(list_from_tuple)
print('-'*30)
# ------------------------------


print("【数据结构-字典】")
dict1 = {'key': 'value'}
dict2 = dict()  # 定义空字典
dict3 = {}  # 定义空字典
dict1['key2'] = 'add2'  # 向字典追加内容
dict1['key3'] = 'add3'  # 向字典追加内容
del dict1['key2']  # 删除字典的一条内容
print(type(dict1), dict1)
print("所有key", dict1.keys())
print("所有value", dict1.values())
print(type(dict2), dict2)
print(type(dict3), dict3)
# 两个列表创建字典 方法1
l_key = ['a', 'b']
l_val = [96, 54]
dict4 = dict(zip(l_key, l_val))
print(dict4)
# 两个元组创建字典
t_1 = ('a', 96)
t_2 = ('b', 54)
dict5 = dict((t_1, t_2))
print(dict5)
print('-'*30)
# ------------------------------


print("【条件语句】")
b = True
ret = 123 if b else 456
# ret = b ? 123 : 456
print(ret)

if b:
    pass
elif b:
    pass
else:
    pass

print('-'*30)
# ------------------------------


print("【循环语句】")
arr = [i*2 for i in range(3)]
for i in arr:
    print(i)
# end for
for i in range(0, 10, 2):
    print(i)
print('-'*30)
# ------------------------------

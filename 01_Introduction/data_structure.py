print("【元组】")
# 元组是只读的列表
tuple1 = (1, 2, 3)
tuple2 = tuple()  # 定义空元组
tuple3 = ()  # 定义空元组
print(type(tuple1), tuple1)
print(type(tuple2), tuple2)
print(type(tuple3), tuple3)
print('-' * 30)
# ------------------------------


print("【集合】")
set0 = set()  # 定义空set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(type(set0), set0)
print(type(set1), set1)
print(type(set2), set2)
# 添加元素
set1.add(3)  # set内容不能重复，此行将不产生任何影响
set1.add(4)
set1.add(5)
print(type(set1), set1)
# 移除元素
set1.remove(5)  # 从中删除指定的元素
ele = set1.pop()  # 弹出最左边的元素
print("pop:", ele)
# 集合运算
print("set1", type(set1), set1)
print("set2", type(set2), set2)
print('并集:\t', set1 | set2)
print('交集:\t', set1 & set2)
print('差集1:\t', set1 - set2)
print('差集2:\t', set2 - set1)
print('并差集:\t', set1 ^ set2)
print('-' * 30)
# ------------------------------


print("【列表】")
list1 = [4, 5, 6]
list2 = list()  # 定义空列表
list3 = []  # 定义空列表
print(type(list1), list1)
print(type(list2), list2)
print(type(list3), list3)
# 追加
list1.append(7)  # 向列表追加元素
list1.append(8)  # 向列表追加元素
# 删除
print("Before", list1)
del list1[0]  # 删除最左边的元素
ele = list1.pop()  # 弹出最右边的元素
print("pop:", ele)
print("After", list1)
# 从元组创建列表
list_from_tuple = list(tuple1)
print("From Tuple", type(list_from_tuple), list_from_tuple)
print('-' * 30)
# ------------------------------


print("【字典】")
dict1 = {'key': 'value'}
dict2 = dict()  # 定义空字典
dict3 = {}  # 定义空字典
print(type(dict1), dict1)
print(type(dict2), dict2)
print(type(dict3), dict3)
#
dict1['key2'] = 'add2'  # 向字典追加内容
dict1['key3'] = 'add3'  # 向字典追加内容
del dict1['key2']  # 删除字典的一条内容
print("所有key", dict1.keys())
print("所有value", dict1.values())
# 从两个列表创建字典
l_key = ['a', 'b']
l_val = [96, 54]
dict4 = dict(zip(l_key, l_val))
print(dict4)
# 两个元组创建字典
t_1 = ('a', 96)
t_2 = ('b', 54)
dict5 = dict((t_1, t_2))
print(dict5)
print('-' * 30)

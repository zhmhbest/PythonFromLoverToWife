# 注释1

"""
注释2
"""

'''
注释3
'''

print("■■■■■■■■■■■■■■■■【删除变量】■■■■■■■■■■■■■■■■")
# 定义变量
var1 = 996
print('var1 =', var1)
# ------------------------------
# 删除变量
del var1
try:
    print(var1)
except NameError:
    print('var1 : 未定义!')
# end try

print("■■■■■■■■■■■■■■■■【交换变量】■■■■■■■■■■■■■■■■")
var1 = 1
var2 = 2
var1, var2 = var2, var1
print('var1 =', var1)
print('var2 =', var2)

print("■■■■■■■■■■■■■■■■【变量类型】■■■■■■■■■■■■■■■■")
# Boolean
var_bool1 = True
var_bool2 = False
print(type(var_bool1), var_bool1)
print(type(var_bool2), var_bool2)
# ------------------------------
# 数字
var_integer1 = 666      # 整型
var_float1 = 3.1415926  # 浮点型
print(type(var_integer1), var_integer1)
print(type(var_float1), var_float1)
# ------------------------------
# 单行字符串
var_string1 = "string1"
var_string2 = 'string2'
print(type(var_string1), var_string1)
print(type(var_string2), var_string2)
# ------------------------------
# 可换行字符串
var_string3 = """str
|ing3"""
var_string4 = '''str
|ing4'''
print(type(var_string3), var_string3)
print(type(var_string4), var_string4)
# ------------------------------
# 不转义字符串
var_string5 = r"C:\Program Files"
var_string6 = r'C:\Program Files'
print(type(var_string5), var_string5)
print(type(var_string6), var_string6)
# ------------------------------
# Bytes
var_bytes1 = b'ABC'
var_bytes2 = b"ABC"
print(type(var_bytes1), var_bytes1)
print(type(var_bytes2), var_bytes2)
# ------------------------------
# 判断变量类型
print("bool ?", isinstance(var_bool1, bool))
print("int  ?", isinstance(var_integer1, int))
print("float?", isinstance(var_float1, float))
print("str  ?", isinstance(var_string1, str))
print("bytes?", isinstance(var_bytes1, bytes))

print("■■■■■■■■■■■■■■■■【格式化输出】■■■■■■■■■■■■■■■■")
var_format1='abc'
var_format2=123
print("str=%s, num=%d" % (var_format1, var_format2))
print(f"str={var_format1}, num={var_format2}")

print("■■■■■■■■■■■■■■■■【条件语句】■■■■■■■■■■■■■■■■")
button = True
if button:
    pass
elif button:
    pass
else:
    pass
# end if
# ------------------------------
# 三目表达式
# ret = button ? 'A' : 'B'
ret = 'T' if button else 'F'
print(ret)

print("■■■■■■■■■■■■■■■■【基础运算】■■■■■■■■■■■■■■■■")
# 四则运算：+ - * /
print('整除: 10 // 3 =', 10 // 3)
print('取余: 10 % 3  =', 10 % 3)
print('乘方: 2 ** 8  =', 2 ** 8)
# ------------------------------
# 自运算
index = 0  # 赋值
index += 1
index *= 2
print('自运算:', index)
# ------------------------------
# 逻辑运算
print('等于:', 1 == 2)
print('不等:', 1 != 2)
print('and:', True and True)
print('or:', True or False)
print('not:', not False)

print("■■■■■■■■■■■■■■■■【循环语句】■■■■■■■■■■■■■■■■")
# 数字区间
for i in range(0, 10, 2):
    print(i, end=',')
# end for
print()
# ------------------------------
# 迭代列表
for item in ['Q', 'W', 'E', 'R']:
    print(item, end=',')
# end for
print()
# ------------------------------
# 迭代字典
var_dict1 = {'a': 11, 'b': 22}
for item in var_dict1:
    print(item, end=',')
# end for
print()
for item, val in var_dict1.items():
    print(item, '=', val, end=',')
# end for
print()
# ------------------------------
# while循环
condition = False
while condition:
    # do-something(break, continue)
    pass
# end while
# ------------------------------
# do-while循环
while True:
    # do-something(break, continue)
    if not condition:
        break
# end while

print("■■■■■■■■■■■■■■■■【字符切片】■■■■■■■■■■■■■■■■")
test_string = "0123456789"
print('DelHead:', test_string[2:])
print('DelTail:', test_string[:-2])
print('Left:\t', test_string[:3])
print('Right:\t', test_string[-3:])
print('Mid:\t', test_string[1:3])
print('Mid:\t', test_string[3:7])

print("■■■■■■■■■■■■■■■■【数据结构】■■■■■■■■■■■■■■■■")
print("【元组】：只读的列表")
tuple1 = (1, 2, 3)
tuple2 = tuple()    # 定义空元组
tuple3 = ()         # 定义空元组
print(type(tuple1), tuple1)
print(type(tuple2), tuple2)
print(type(tuple3), tuple3)
# ------------------------------
print("【集合】")
set0 = set()        # 定义空set
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(type(set0), set0)
print(type(set1), set1)
print(type(set2), set2)
# 添加元素
set1.add(3)         # set内容不能重复，此行将不产生任何影响
set1.add(4)
set1.add(5)
print(type(set1), set1)
# 移除元素
set1.remove(5)      # 从中删除指定的元素
ele = set1.pop()    # 弹出最左边的元素
print("pop:", ele)
# 集合运算
print("set1", type(set1), set1)
print("set2", type(set2), set2)
print('并集:\t', set1 | set2)
print('交集:\t', set1 & set2)
print('差集1:\t', set1 - set2)
print('差集2:\t', set2 - set1)
print('并差集:\t', set1 ^ set2)
# ------------------------------
print("【列表】")
list1 = [4, 5, 6]
list2 = list()      # 定义空列表
list3 = []          # 定义空列表
print(type(list1), list1)
print(type(list2), list2)
print(type(list3), list3)
# 追加
list1.append(7)     # 向列表追加元素
list1.append(8)     # 向列表追加元素
# 删除
print("Before", list1)
del list1[0]        # 删除最左边的元素
ele = list1.pop()   # 弹出最右边的元素
print("pop:", ele)
print("After", list1)
# 从元组创建列表
list_from_tuple = list(tuple1)
print("From Tuple", type(list_from_tuple), list_from_tuple)
# ------------------------------
print("【字典】")
dict1 = {'key': 'value'}
dict2 = dict()          # 定义空字典
dict3 = {}              # 定义空字典
print(type(dict1), dict1)
print(type(dict2), dict2)
print(type(dict3), dict3)
#
dict1['key2'] = 'add2'  # 向字典追加内容
dict1['key3'] = 'add3'  # 向字典追加内容
del dict1['key2']       # 删除字典的一条内容
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

print("■■■■■■■■■■■■■■■■【等同判断】■■■■■■■■■■■■■■■■")
obj1 = {}
obj2 = {}
obj3 = obj2

# 同物判断
if obj1 is obj2:
    print('obj1和obj2是一个东西')
else:
    print('obj1和obj2不是一个东西')
# end if

# 等值判断
if obj1 == obj2:
    print('obj1和obj2的值相同')
else:
    print('obj1和obj2的值不同')
# end if

# 同物判断
if obj2 is obj3:
    print('obj2和obj3是一个东西')
else:
    print('obj2和obj3不是一个东西')
# end if

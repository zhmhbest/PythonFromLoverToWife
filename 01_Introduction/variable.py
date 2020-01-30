
print("【变量定义】")
var1 = "这是变量var1的值"
print(var1)


print("【删除变量】")
del var1
try:
    print(var1)
except NameError:
    print('错误：未定义的变量!')
# end try


print("【交换变量的值】")
var1 = 1
var2 = 2
var1, var2 = var2, var1
print('var1 =', var1)
print('var2 =', var2)


print("【基础变量类型】")
# 数字
number1 = 666           # 整型
number2 = 3.1415926     # 浮点型
print(type(number1), number1)
print(type(number2), number2)

# 单行字符串
string1 = "String"
string2 = 'string'
print(type(string1), string1)
print(type(string2), string2)

# 可换行字符串
string3 = """STT
ing"""
string4 = '''str
ING'''
print(type(string3), string3)
print(type(string4), string4)

# 不转义字符串
string5 = r"C:\Windows"
string6 = r'C:\C:\Program Files'
print(type(string5), string5)
print(type(string6), string6)

# Bytes
string7 = b'ABC'
string8 = b"ABC"
print(type(string7), string7)
print(type(string8), string8)


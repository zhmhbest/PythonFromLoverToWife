
print("【数字区间】")
for i in range(0, 10, 2):
    print(i)
# end for
print('-' * 30)
# ------------------------------


print("【迭代列表】")
list1 = ['Q', 'W', 'E', 'R']
for item in list1:
    print(item)
# end for
print('-' * 30)
# ------------------------------


print("【迭代字典】")
dict1 = {'a': 11, 'b': 22}
for item in dict1:
    print(item)
# end for

for item, val in dict1.items():
    print(item, val)
# end for
print('-' * 30)
# ------------------------------


print("【while循环】")
while True:
    break
    # continue
# end while


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

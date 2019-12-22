"""
    运算符重载
"""


class OperatorOverloading:
    _dict1 = dict()
    _dict2 = dict()
    _size = 999
    _string = "使用str方法返回的字符串"

    def __len__(self):
        """
        len()
        :return:
        """
        return self._size

    def __str__(self):
        """
        str()
        :return:
        """
        return self._string

    def __setitem__(self, key, value):
        """
        []
        :return:
        """
        self._dict2[key] = value

    def __getitem__(self, item):
        """
        []
        :return:
        """
        return self._dict2[item]

    def __getattr__(self, item):
        """
        .
        :return:
        """
        return self._dict1[item]

    def __setattr__(self, key, value):
        """
        .
        :return:
        """
        self._dict1[key] = value

    def __add__(self, other):
        """
        +
        :return:
        """
        return self._size + other

    def __sub__(self, other):
        """
        -
        :return:
        """
        return self._size - other

    def __iter__(self):
        """
        iter()
        :return:
        """
        return iter(self._dict2)


if __name__ == '__main__':
    obj = OperatorOverloading()
    print(len(obj), obj.__len__())
    print(str(obj), obj.__str__())

    print(obj + 1, obj.__add__(1))
    print(obj - 9, obj.__sub__(9))

    obj.A = 'QWE'
    obj.__setattr__('B', 'ASD')
    print(obj.A)
    print(obj.__getattr__('B'))

    obj['x'] = 'Apple'
    obj.__setitem__('y', 'Bubble')

    print(obj['x'])
    print(obj.__getitem__('y'))

    print(iter(obj))
    print(obj.__iter__())
    for i in obj:
        print(i)
    for i in obj.__iter__():
        print(i)

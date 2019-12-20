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
    print(len(obj))      # __len__(self)方法
    print(str(obj))      # __str__(self)方法
    #
    print(obj + 1)
    print(obj - 99)
    #
    obj.A = 'QWE'        # __setattr__(self, key, value)
    # print(obj._dict1)
    print(obj.A)         # __getattr__(self, item)
    #
    obj['x'] = 'Apple'   # __setitem__(self, key, value)
    obj['y'] = 'Bubble'  # __setitem__(self, key, value)
    obj['z'] = 'Candy'   # __setitem__(self, key, value)
    # print(obj._dict2)
    print(obj['y'])      # __getitem__(self, item):
    #
    print(iter(obj))
    for i in obj:
        print(i)

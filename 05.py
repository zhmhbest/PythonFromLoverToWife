"""
    列表拷贝
    请说明以下三个arr：arr1，arr2，arr3的区别
"""

if __name__ == '__main__':
    src_arr = [1, 2, 3]

    arr1 = src_arr
    arr2 = src_arr[:]
    arr3 = src_arr.copy()

    print(arr1)
    print(arr2)
    print(arr3)

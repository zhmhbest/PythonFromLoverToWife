"""
    列表拷贝
    请说明以下三个arr：arr1，arr2，arr3的区别
"""

if __name__ == '__main__':
    src_arr = [[11, 12], 2, 3]
    print(src_arr)

    arr1 = src_arr
    arr2 = src_arr[:]
    arr3 = src_arr.copy()

    src_arr[1] = 'changed'
    src_arr[0][1] = 'changed'

    print(arr1)
    print(arr2)
    print(arr3)

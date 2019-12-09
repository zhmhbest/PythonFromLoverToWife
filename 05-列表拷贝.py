"""
    列表拷贝
"""
import copy


if __name__ == '__main__':
    src_arr = [[11, 12], 2, 3]
    print(src_arr)

    """
    【引用拷贝】
        直接赋值仅传递对象的引用
        原始列表改变，被赋值对象也会做相同的改变。
    """
    arr1 = src_arr

    """
    【浅拷贝】
        只拷贝了对象的第一层，没有拷贝子对象
        原始列表的子对象改变，被赋值对象也会做相同的改变。
        原始列表第一层改变，被赋值对象不会发生改变
    """
    arr2_1 = src_arr[:]
    arr2_2 = src_arr.copy()
    arr2_3 = copy.copy(src_arr)

    """
    【深拷贝】
        完全拷贝所有内容，与原始数据彻底解耦。
    """
    arr3 = copy.deepcopy(src_arr)

    src_arr[1] = 'changed'
    src_arr[0][1] = 'sub_changed'
    print(arr1)
    print(arr2_1)
    print(arr2_2)
    print(arr2_3)
    print(arr3)

"""
    排序算法
    https://www.runoob.com/w3cnote/ten-sorting-algorithm.html
"""
import random


def get_random_list(size):
    result = []
    for i in range(size):
        result.append(random.randint(0, 100))
    # end for
    return result


def sort_select_directly(arr):
    """
    【择排序之直接选择排序】
    核心思想：
        >每次选择一个最小值，将其移动到无序序列的最左端
    缺点: 是时间复杂度最高的排序算法之一。
    """
    for i in range(len(arr)):

        index = i  # 先假设当前值是最小值

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[index]:  # 向后依次比较
                index = j
            # end if
        # end for(j)
        # j循环结束后index所在位置即为还没有排序的序列当中的最小值

        arr[i], arr[index] = arr[index], arr[i]
        # 每次i循环结束，都将一个最小值移动到i所在的位置

    # end for(i)
    return arr


def sort_swap_bubble(arr):
    """
    【交换排序之冒泡排序】
    核心思想：
        >从前向后依次两两比较，如果(左>右)就交换位置。
        >每次大环都有一个最大值被移动到无序序列的最右端
    缺点: 是时间复杂度最高的排序算法之一。
    """
    # 原数据重新定义为列表
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # end if
            # 如果(左>右)就交换位置
        # end for(j)
    # end for(i)
    return arr


def sort_insert_directly(arr):
    """
    【直接插入排序】
    核心思想：每次从无序序列中选择一个元素插入到有序序列中
    """
    # 原数据重新定义为列表
    for i in range(1, len(arr)):
        key = arr[i]

        # key 将列表分割成
        # 左边: 已经有序的部分
        # 右边: 待排序的部分

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # 将元素往右移动，给插入key留出空间。
            j -= 1
        # end while
        arr[j + 1] = key  # 在留出空间的地方插入key
    # end for
    return arr


def sort_quick(arr):
    """
    快速排序
    :param arr:
    :return:
    """

    def partition(arr, low, hig):
        pivot = arr[hig]
        i = (low - 1)
        for j in range(low, hig):
            # 当前元素小于或等于 pivot
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
            # end if
        # end for
        arr[i + 1], arr[hig] = arr[hig], arr[i + 1]
        return i + 1
    # end def

    def recursion(a, l, h):
        """
        递归修正
        :param a: 待排序序列
        :param l: 可达起始索引
        :param h: 可达结束索引
        """
        if l < h:
            # m: 本次partition确定的数据的位置
            m = partition(a, l, h)
            recursion(a, l, m - 1)
            recursion(a, m + 1, h)
        # end if
    # end def
    recursion(arr, 0, len(arr) - 1)
    return arr


def sort_auto(arr):
    # 原数据重新定义为列表
    # 利用Python自带的方法排序
    arr.sort()
    return arr


if __name__ == '__main__':
    l1 = get_random_list(20)
    print(l1)
    # ↓↓↓↓↓↓↓↓ 在此处编写自己的代码 ↓↓↓↓↓↓↓↓
    print("select: ", sort_select_directly(l1.copy()))
    print("bubble: ", sort_swap_bubble(l1.copy()))
    print("insert: ", sort_insert_directly(l1.copy()))
    print("quick : ", sort_quick(l1.copy()))
    print("auto  : ", sort_auto(l1.copy()))
    # ↑↑↑↑↑↑↑↑ 在此处编写自己的代码 ↑↑↑↑↑↑↑↑

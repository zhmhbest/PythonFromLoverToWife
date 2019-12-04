"""
    x, y, z为随机生成的三个正整数
    请由小到大依次输出。
"""
import random


def way1(x, y, z):
    """
    【逻辑套嵌】
    核心思想：
        >分情况判断
    缺点: 数据量大时无法使用！
    """
    result = []
    if x < y and x < z:
        result.append(x)  # x是最小值
        if y < z:
            result.append(y)
            result.append(z)
        else:
            result.append(z)
            result.append(y)
    elif y < x and y < z:
        result.append(y)  # y是最小值
        if x < z:
            result.append(x)
            result.append(z)
        else:
            result.append(z)
            result.append(x)
    else:
        result.append(z)  # z一定是最小值
        if x < y:
            result.append(x)
            result.append(y)
        else:
            result.append(y)
            result.append(x)
    # end if
    print("way1: ", result)


def way2(x, y, z):
    """
    【择排序之直接选择排序】
    核心思想：
        >每次选择一个最小值，将其移动到无序序列的最左端
    缺点: 是时间复杂度最高的排序算法之一。
    """
    # 原数据重新定义为列表
    arr = [x, y, z]
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
    print("way2: ", arr)


def way3(x, y, z):
    """
    【交换排序之冒泡排序】
    核心思想：
        >从前向后依次两两比较，如果(左>右)就交换位置。
        >每次大环都有一个最大值被移动到无序序列的最右端
    缺点: 是时间复杂度最高的排序算法之一。
    """
    # 原数据重新定义为列表
    arr = [x, y, z]
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            # end if
            # 如果(左>右)就交换位置
        # end for(j)
    # end for(i)
    print("way3: ", arr)


def way4(x, y, z):
    """
    【直接插入排序】
    核心思想：每次从无序序列中选择一个元素插入到有序序列中
    """
    # 原数据重新定义为列表
    arr = [x, y, z]
    for i in range(1, len(arr)):
        key = arr[i]

        # key 将列表分割成
        # 左边: 已经有序的部分
        # 有病: 待排序的部分

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]  # 将元素往由移动，已给插入key留出空间。
            j -= 1
        arr[j + 1] = key  # 在留出空间的地方插入key
    print("way4: ", arr)


def way5(x, y, z):
    # 原数据重新定义为列表
    arr = [x, y, z]
    # 利用Python自带的方法排序
    arr.sort()
    print("way4: ", arr)


if __name__ == '__main__':
    x_val = random.randint(0, 9)
    y_val = random.randint(0, 9)
    z_val = random.randint(0, 9)
    print(x_val, y_val, z_val)
    # ↓↓↓↓↓↓↓↓ 在此处编写自己的代码 ↓↓↓↓↓↓↓↓
    way1(x_val, y_val, z_val)
    way2(x_val, y_val, z_val)
    way3(x_val, y_val, z_val)
    way4(x_val, y_val, z_val)
    way5(x_val, y_val, z_val)
    # 算法2~4仅需了解
    # 需要熟练掌握算法1和算法5
    # ↑↑↑↑↑↑↑↑ 在此处编写自己的代码 ↑↑↑↑↑↑↑↑

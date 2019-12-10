"""
    数据分析
"""
import pandas as pd
import math


def write_to_csv(data):
    try:
        data.to_csv("test.csv", encoding='gbk', index=False, index_label=False)
        print("使用Excel打开“test.csv”查看内容。")
    except PermissionError:
        print("请先关闭Excel再执行本程序！")
    # end try


def get_distance(lat_a, lon_a, lat_b, lon_b):
    rad = 3.1415926 / 180
    lat1 = lat_a * rad
    lat2 = lat_b * rad
    tmp = math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos((lon_b - lon_a) * rad)
    distance = 6371000 * math.acos((min(tmp, 1)))
    return distance


def get_distance_from_row(row1, row2):
    return get_distance(row1['lat'], row1['lon'], row2['lat'], row2['lon'])


if __name__ == '__main__':
    # print(wait_analyse_data)
    data = pd.read_csv("21-数据分析.csv")
    # 按t排序
    data.sort_values('t', inplace=True)
    data = data.reset_index(drop=True)  # 重新生成索引

    # 计算dt并修改列名
    zero = data['t'][0]
    data.loc[:, 't'] -= zero
    data.rename(columns={'t': 'dt'}, inplace=True)

    # 获得列数
    # row_size = data.shape[0]

    # 计算ds
    dump = []
    pre_row = data.loc[0]
    # r = get_distance_from_row(data.loc[0], data.loc[2])
    for index, row in data.iterrows():
        cur_row = row
        dump.append(get_distance_from_row(pre_row, cur_row))
        pre_row = cur_row
    # end for

    # 追加一列
    data['ds'] = dump

    # 展示文件
    write_to_csv(data)
    print(data)

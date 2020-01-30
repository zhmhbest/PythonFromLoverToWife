"""
    位运算
    可能需要的辅助工具：https://tool.lu/hexconvert/
"""

print(end='')

"""
    按位与运算
        1 & 1 = 1
        1 & 0 = 0
        0 & 1 = 0
        0 & 0 = 0
    ################
    51: 110011
     &
    28: 011100
    ————————————
    16: 010000
"""
print("&", 28 & 51)

"""
    按位或运算
        1 | 1 = 1
        1 | 0 = 1
        0 | 1 = 1
        0 | 0 = 0
    ################
    51: 110011
     |
    28: 011100
    ————————————
    63: 111111
"""
print("|", 28 | 51)

"""
    按位取反运算
        ~1 = 0
        ~0 = 1
    ################
    51: 110011
     ~
    ————————————
    12: 001100
"""
print("~", ~51 & 0b111111)
# & 0b111111 是因为51前面实际还有0会影响结果，这步忽略掉前面的0

"""
    按位异或运算（相同为0不同为1）
        1 ^ 1 = 0
        1 ^ 0 = 1
        0 ^ 1 = 1
        0 ^ 0 = 0
    ################
    51: 110011
     ^
    28: 011100
    ————————————
    47: 101111
"""
print("^", 28 ^ 51)

"""
    右位移运算，右移动，空出的位置补0
    11111111>>1 & 0b11111111
    ————————————
    01111111 = 127

    11111111>>2 & 0b11111111
    ————————————
    00111111 = 63
    
"""
print(">>", 0b11111111 >> 1 & 0b11111111)
print(">>", 0b11111111 >> 2 & 0b11111111)

"""
    左位移运算，左移动，空出的位置补0
    11111111<<1 & 0b11111111
    ————————————
    11111110 = 254

    11111111<<2 & 0b11111111
    ————————————
    11111100 = 252
    
"""
print("<<", 0b11111111 << 1 & 0b11111111)
print("<<", 0b11111111 << 2 & 0b11111111)

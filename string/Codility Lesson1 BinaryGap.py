"""
找出2位元中1與1之間最大的差距

9 > 1001 > 2
32 > 100000 > 0
1041 > 10000010001 > 5

算出2位元最後需反轉
N = 9
9 % 2 = 1
9 / 2 > 4 % 2 = 0
4 / 2 > 2 % 2 = 0
2 / 2 > 1 % 2 = 1
1 / 2 > 0

先算出2位元 > binary
one_index = 0  2位元中1出現的位置, 會一直往右推進
max_gap = -1
for i in data:
	如果one_index不為初始值且又遇到'1'
		算出gap並更新max_gap
		設one_index = i
	如果是第一次遇到'1':
		設one_index = i
回傳max_gap
"""

def solve(N):
    binary = get_binary(N)
    one_index = -1
    max_gap = 0
    for i in range(len(binary)):
        if one_index != -1 and binary[i] == '1':
            gap = i - one_index - 1
            max_gap = max(gap, max_gap)
            one_index = i
        elif binary[i] == '1':
            one_index = i
    return max_gap

def get_binary(N):
    if N <=0:
        return '0'
    ret = []
    while N != 0:
        ret.append(str(N % 2))
        N = int(N / 2)
    ret.reverse()
    return ''.join(ret)

if __name__ == "__main__":
    print(solve(9))  # 1001 > 2
    print(solve(32))  # 100000 > 0
    print(solve(1041))  # 10000010001 > 5
     
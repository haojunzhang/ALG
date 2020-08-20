"""
找出沒有出現在此陣列中, 最小整數
A = [1, 2, 3, 4, 5]
return = 6
m = 創一個set或dict存出現過的整數

迴圈A:
    塞進set
迴圈1~999:
    如此值不存在於m則回傳
"""
def solve(A):
    m = set()
    for i in A:
        m.add(i)
    
    for i in range(1, 999):
        if i not in m:
            return i
    return 1

if __name__ == "__main__":
    print(solve([1, 3, 4, 5, 6]))  # 2
    print(solve([1, 3, 2, 4, 5]))  # 6
    print(solve([-1, -2]))  # 1
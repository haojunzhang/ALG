"""
找出可以當作起點且可以繞完一圈的加油站位置
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

條件
總gas - 總cost 需>=0 不然, 任一點皆無法完成
total = 0 計算總油量
tmp_total = 0 作為一次測試的油量 
start = 0 起點

每圈加總total, tmp_total
假設從0開始到了2, tmp_total才不夠, 那0,1,2都不能作為起點, 設起點為start = i + 1, 並且重設tmp_total
"""


def solve(gas, cost):
    total = 0
    tmp_total = 0
    start = 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        tmp_total += gas[i] - cost[i]
        if tmp_total < 0:
            start = i + 1
            tmp_total = 0
    return start if total >= 0 else -1


if __name__ == "__main__":
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(solve(gas, cost))  # 3

    gas = [2, 3, 4]
    cost = [3, 4, 3]
    print(solve(gas, cost))  # -1

    gas = [3, 4, 5, 6, 7]
    cost = [4, 5, 6, 7, 3]
    print(solve(gas, cost))  # 4

    gas = [3, 4, 5, 6, 7]
    cost = [3, 4, 5, 6, 7]
    print(solve(gas, cost))  # 0

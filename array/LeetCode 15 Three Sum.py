"""
3Sum
找出總和為0的三個數, 結果不可重複

思路
先排序
3個變數i, lo, hi
i跑回圈0~len-2(不含)
    如 i 與 i-1 一樣則需跳過此圈(避免A[i] A[i-1]重複)
    lo , hi則是雙指針, lo從左, hi從右
    i  lo                hi
    [-4, -1 , -1 , 0 , 1 , 2]
    找出 lo + hi 為 i 的相反數
    如比相反數小 lo++(如lo++和lo相同就回圈到不同為止避免重複)
    反之比相反數大 hi--(同上避免重複)

變化
  i  lo        ~       hi
[-4, -1 , -1 , 0 , 1 , 2]
      i   lo     ~     hi
[-4, -1 , -1 , 0 , 1 , 2]
           i  lo   ~   hi
[-4, -1 , -1 , 0 , 1 , 2]
               i  lo   hi
[-4, -1 , -1 , 0 , 1 , 2]
"""


def solve(A):
    ret = []
    # 排序
    A.sort()
    for i in range(len(A) - 2):
        # 第一圈ok, 與前一個值不同ok(避免重複)
        if i == 0 or A[i] != A[i - 1]:
            lo, hi, target = i + 1, len(A) - 1, 0 - A[i]
            while lo < hi:
                if A[lo] + A[hi] == target:
                    ret.append([A[i], A[lo], A[hi]])

                    # 如下一個重複再跳過(會跳到重複的最後一個位置)
                    while lo < hi and A[lo] == A[lo + 1]:
                        lo += 1

                    # 如上一個重複再跳過(會跳到重複的最後一個位置)
                    while lo < hi and A[hi] == A[hi - 1]:
                        hi -= 1

                    # 再推一格
                    lo += 1
                    hi -= 1
                elif A[lo] + A[hi] > target:  # 比目標大 > 減少hi
                    hi -= 1
                elif A[lo] + A[hi] < target:  # 比目標小 > 增加lo
                    lo += 1

    return ret


if __name__ == "__main__":
    print(solve([-1, 0, 1, 2, -1, -4]))

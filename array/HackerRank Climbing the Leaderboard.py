"""
排行榜
rank = [100, 90, 90, 80]
player = [70, 80, 105]
output = [4, 3, 1]
rank為遞減數列
player為遞增數列
70分排第4
80分排第3
105分排第1

回圈player
    cur_rank這一round的排名
    回圈
        去比rank直到有適合的位置
        append進rank
        ret.append(cur_rank)
"""


def solve(rank, player):
    ret = []
    for p in player:
        cur_rank = 1
        is_end = True
        j = 0
        while j < len(rank):
            if p >= rank[j]:
                rank.insert(j, p)
                ret.append(cur_rank)
                is_end = False  # 跑到底了
                break
            else:
                # 跳過重複
                while j < len(rank) - 1 and rank[j] == rank[j+1]:
                    j += 1
                cur_rank += 1
            j += 1  # 每圈+1
        # 如跑到底, 代表最小
        if is_end is True:
            rank.append(p)
            ret.append(cur_rank)
    return ret


if __name__ == "__main__":
    print(solve(
        [100, 90, 90, 80],
        [70, 80, 105]
    ))  # [4, 3, 1]

    print(solve(
        [100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]
    ))  # [6,4,2,1]

    print(solve(
        [100, 90, 90, 80, 75, 60],
        [50, 65, 77, 90, 102]
    ))  # [6,5,4,2,1]

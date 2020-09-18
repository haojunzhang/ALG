"""
找出最長的前綴

Input: ['flower','flow','flight']
Output: 'fl'

Input: ['dog','racecar','car']
Output: ''

思路
A=Input
先找出長度最小字串, shortest_str
回圈shortest_str:
    回圈A:
        如A[i]==shortest_str[i]下一圈(不寫)
        A[i]!=shortest_str[i]回傳shortest_str[0:i](不含i)
"""


def solve(A):
    if len(A) == 0:
        return ''

    # 先找出最短的字串
    shortest_str = A[0]
    for it in A:
        if len(it) < len(shortest_str):
            shortest_str = it

    for i in range(len(shortest_str)):
        ch = shortest_str[i]

        for other in A:
            if other[i] != ch:
                return shortest_str[0:i]

    return ''


if __name__ == '__main__':
    print(solve(['flower', 'flow', 'flight']))  # 'fl'
    print(solve(['dog', 'racecar', 'car']))  # ''
    print(solve(['abcd', 'abc123', 'ab987654321']))  # 'ab'

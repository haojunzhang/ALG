"""
求出子字串中不重複最長的長度, 想像成一個移動框, left為左index, i則是右邊
m為則是記錄讀過的字串最後的位置, ex: a:0
res存結果
for i in range(text):
    s = text[i]
    if 如果s出現過則更新left到目前位置, ex: lee, 
        設left為2, le=2的結果已存所以不用擔心
        清空m, 重新計算
    存s出現的位置
    res = max(res, i - left), 找最大

過程:
    hellow'orld' : 4
    'h'elloworld
    'he'lloworld
    'hel'loworld : 3
    hel'l'oworld
    hel'lo'world
    hel'low'orld : 3
    hellow'o'rld
    hellow'or'ld
    hellow'orl'd
    hellow'orld' : *4*

Time complexity : O(N)
Space complexity : O(N)
"""


def longest_substring_without_repeating_characters(text):
    m = {}
    left = 0
    ret = 0
    for i in range(len(text)):
        s = text[i]
        if s in m:
            m.clear()
            left = i
        m[s] = i
        ret = max(ret, i - left + 1)
    return ret


if __name__ == '__main__':
    print(longest_substring_without_repeating_characters('facebook'))  # 6
    print(longest_substring_without_repeating_characters('leetcode'))  # 5
    print(longest_substring_without_repeating_characters('google'))  # 4
    print(longest_substring_without_repeating_characters('tomorrow'))  # 3
    print(longest_substring_without_repeating_characters('helloworld'))  # 4

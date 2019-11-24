# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\C\C_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
A, B, X = [int(item) for item in input().split()]
res_list = []
left = 1 -1
right = 10 ** 9 + 1

is_search = True

while is_search:
    N = (left + right)//2
    res = A * N + B * len(str(N))

    if res > X:
        right = N
    elif res <= X:
        res_list.append(N)
        left = N

    if right - left <= 1:
        is_search = False

if res_list == []:
    print(0)
else:
    print(max(res_list))


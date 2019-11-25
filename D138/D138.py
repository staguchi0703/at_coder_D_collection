# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D138\D138.txt', 'r', encoding="utf-8")
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
N, Q = [int(item) for item in input().split()]

tree_list = [input() for _ in range(1,N)]
tree_list_int = [[int(k) for k in i.split()] for i in tree_list]
query_list = [input() for _ in range(Q)]
query_list_int = [[int(k) for k in i.split()]  for i in query_list]

val_list = [0 for _ in range(N)]
node_index = [[] for _ in range(N)]
cumulated_sum_list = [0] * N


for a, b in tree_list_int:
    node_index[a -1].append(b - 1)
    node_index[b -1].append(a - 1)

for index, val in query_list_int:
    val_list[index-1] += val

def dfs(child_index, pairent_index):
    for child in node_index[child_index]:

        if child == pairent_index:
            continue

        val_list[child] += val_list[child_index]
        dfs(child, child_index)

    return val_list

res = dfs(0, -1) #0はルート、-1は親を持っていない事

for i in res:
    print(i)
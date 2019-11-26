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

tree_list = [input().split() for _ in range(1,N)]

query_list = [input().split() for _ in range(Q)]
query_list_int = [[int(k) for k in i]  for i in query_list]

val_list = [0 for _ in range(N)]
linkde_node_list = [[] for _ in range(N)]

for a, b in tree_list:
    linkde_node_list[int(a) -1].append(int(b) - 1)
    linkde_node_list[int(b) -1].append(int(a) - 1)


for index, val in query_list_int:
    val_list[index-1] += val

def dfs(node_index, pairent_index):
    print('node_index',node_index+1)
    for child in linkde_node_list[node_index]:
        print('A',child)
        if child == pairent_index:
            continue
        print('B', child)
        val_list[child] += val_list[node_index]
        dfs(child, node_index)

    return val_list

res = dfs(0, -1) 

print(*res)
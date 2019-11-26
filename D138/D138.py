# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f = open(r'.\D138\D138.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin = f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可
N, Q = [int(item) for item in input().split()]

tree_list = [input().split() for j in range(1, N)]

query_list = [input().split() for k in range(Q)]
query_list_int = [[int(k) for k in i] for i in query_list]

val_list = [0 for _ in range(N)]

linked_node_list = [[] for _ in range(N)]

for a, b in tree_list:
    a, b = int(a)-1, int(b) -1
    linked_node_list[a].append(b)
    linked_node_list[b].append(a)


for index, val in query_list_int:
    val_list[index-1] += val

stack = [0]
parent = [0] * (N+1)

#再帰関数を使うとメモリ制限に引っかかるので、whileで順次実行する
# スタックでLIFOを使う
# 訪問済みノードを確認し、除外する　=>あるノードの親ノードはXをリストで持っておく
# この辺データ構造でもてればすっきりしそう

while True:
    v=stack.pop()
    for child in linked_node_list[v]:
        if child != parent[v]:
            parent[child] = v
            stack.append(child)
            val_list[child] += val_list[v]
    if not stack:
        break

print(*val_list)


# %%

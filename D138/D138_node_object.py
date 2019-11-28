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


class Node:
    def __init__(self, val):
        self.val = val
        self.child_list = []
        self.cnt = 0

class my_tree:
    def __init__(self, tree_list):
        self.node_list = []

        for i in range(N):
            self.node_list.append(Node(i+1))

        for a, b in tree_list:
            a, b = int(a), int(b)

            child_node = self.node_list[b-1]
            self.node_list[a-1].child_list.append(child_node)








ins = my_tree(tree_list)
print(ins.node_list)

            
        
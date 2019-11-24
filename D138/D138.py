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
tree = [[int(item) for item in input().split()] for _ in range(1, N)]
act_list = [[int(item) for item in input().split()] for _ in range(Q)]

print(tree)
print(act_list)

class Node:
    def __init__(self, data):
        self.data = data
        self.cnt = 0
        self.child_list = []

class my_tree:
    def __init__(self, N, tree):
        generated_node_list = []

        for i in range(1, N+1):
            generated_node_list.append(Node(i))

        for i, j in tree:
            generated_node_list[i-1].child_list.append(generated_node_list[j-1])

            
ins = my_tree(N, tree)
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
tree_list_int = [list(map(int,i.split())) for i in tree_list]
action_list = [input() for _ in range(Q)]
action_list_int = [list(map(int, i.split())) for i in action_list]

print('tree', tree_list_int)
print('act', action_list_int)

class Node:
    def __init__(self, data):
        self.data = data
        self.cnt = 0
        self.child = None


class tree:
    def __init__(self, tree_list_int):
        self.node_list = [Node(i) for i in range(1,N+1)]

        for i, j in tree_list_int:
            node = self.node_list[i-1]
            node.child = []
            node.child.append(Node(j))


    def adder(self, node, val):
        node.cnt += val

        if not node.child:
            return node.cnt

        for next_child in node.child:
            self.adder(next_child, val)

                

        
ins=tree(tree_list_int)

for pos, val in action_list_int:
    for node in ins.node_list:
        if node.data == pos:
            ins.adder(node, val)


for i in range(0, N):
    print(i+1, ins.node_list[i].cnt)



# %%

# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D142\D142.txt', 'r', encoding="utf-8")
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
import math 

A, B = sorted([int(item) for item in input().split()])

def gdc(A, B):

    while A > 0:
        A, B = B % A, A
    return B

def chk_pn(num):

    if num is 1:
        return True
    
    for i in range(int(math.sqrt(num)) + 1):

print(gdc(A, B))


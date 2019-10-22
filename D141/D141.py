# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D141\D141.txt', 'r', encoding="utf-8")
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
import heapq as hp
N, M = [int(item) for item in input().split()]
price_list = sorted([-1 * int(item) for item in input().split()])

total_m = 0

def discount(price_list, ticket_num):
    total_ticket =0
    hp.heapify(price_list)

    while total_ticket < ticket_num:
        temp = hp.heappop(price_list)
        hp.heappush(price_list, -1* (-1*temp//2))
        total_ticket += 1

    return price_list

res = discount(price_list, M)
print(res)
print(-1 * sum(res))
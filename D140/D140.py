# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\D140\D140.txt', 'r', encoding="utf-8")
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

N, K = [int(item) for item in input().split()]
S = [item for item in input()]

def compress(arr):
    """圧縮して消えた人はhappy"""
    cnt_h = 0
    new_arr = []
    comp_arr = ['L']

    #最初は先頭をLにする　この回転はノーカン
    if arr[0] == 'R':
        for item in arr:
            if item == 'L':
                new_arr.append('R')
            else:
                new_arr.append('L')

            prev_item = item
    else:
        new_arr = arr
    # 圧縮操作と圧縮されたかずを数える

    for i in range(1, N):
        if new_arr[i - 1] == new_arr[i]:
            cnt_h += 1
        else:
            comp_arr.append(new_arr[i])

    return [comp_arr, cnt_h] 


def execute(arr, cnt_h, K):
    # 境界を全て反転するために必要な操作回数
    max_rotation = len(arr)//2
    # 全てLになるか反転回数がKに到達するかで終了
    if max_rotation <= K:
        if arr[-1] == 'R':
            cnt_h += max_rotation*2 -1
        elif arr[-1] == 'L':
            cnt_h += max_rotation*2
    else:
        if arr[2*K] == 'R':
            cnt_h += 2*K - 1
        elif arr[2*K] == 'L':
            cnt_h += 2*K

    return cnt_h

arr, cnt_h = compress(S)
print(execute(arr, cnt_h, K))


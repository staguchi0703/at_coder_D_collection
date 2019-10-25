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

A, B = [int(item) for item in input().split()]

def gdc(A, B):
    """最大公約数を求める
    再帰関数にするよりWhileでしたほうが前回の値を覚えているので早いらしい
    TODO whileで書き直す
    """
    if B == 0:
        return A
    else:
        return gdc(B, A % B)

def chk_pn(num):

    flag = True
    if num  <= 3:
        pass

    else:    
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                flag = False
                break
    return flag


def mk_factor(num):

    max_divisor = int(math.sqrt(num))+1
    divisor = 2
    factor_list = [1]

    while divisor <= max_divisor:
        if num % divisor == 0:
            factor_list.append(divisor)
            num /= divisor
        else:
            divisor += 1
    
    factor_list.append(num) #割り残った数を約数に含める事を忘れない
    return factor_list

GDC = gdc(A, B)
pn_factor = [i for i in mk_factor(GDC) if chk_pn(i) is True]
# print(pn_factor)
print(len(set(pn_factor)))

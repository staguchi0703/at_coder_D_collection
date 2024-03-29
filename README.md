# at_coder_template

## はじめに

* ド素人の筆者が[AtCoder](https://atcoder.jp/contests/) Beginner Contestに数回挑んでみた。
* しかしながらD問題以降まったく歯が立たない。
* これらの問題は、計算量の見積もり＋処理速度向上のためのアルゴリズムorライブラリの使いこなし方or数学知識が問われている。
* 難しくて吐きそうだけど、面白い。解けないとついついムキになってしまう！


## 目的

* AtCoderのDランク問題（400点）の解き方を習得する。
* D問題のための計算量の見積もりと、計算量を削減するアルゴリズムについて習得する。

## 今後

* 本番で解けるイメージが沸かない....。
* 今後も勉強した結果が溜まったた記事を追加する予定。

## 問題へのリンク

* ABC D問題
  * [ABC 142 D](https://atcoder.jp/contests/abc142/tasks/abc142_d)
  * [ABC 141 D](https://atcoder.jp/contests/abc141/tasks/abc141_d)
  * [ABC 140 D](https://atcoder.jp/contests/abc140/tasks/abc140_d)
  * [ABC 139 D](https://atcoder.jp/contests/abc139/tasks/abc139_d)
  * [ABC 138 D](https://atcoder.jp/contests/abc138/tasks/abc138_d)

* D問題の練習になる問題
  * [Disco2020 B](https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_b)
  * [ABC 146 C](https://atcoder.jp/contests/abc146/tasks/abc146_c)

## 回答

### [ABC 142 D](https://atcoder.jp/contests/abc142/tasks/abc142_d)

* 方針
  * 素数の探索は $O{(\sqrt{N})}$
  * 約数を求めるとき(因数分解)も $O{(\sqrt{N})}$

* 実装
  * 素数探索`for i in range(int(math.sqrt(N))+1)`
  * 最大公約数はユークリッドの互除法` A, B = B, A % B `
  * 因数分解はの時に割り残った値を約数に加えることを忘れない
* おまけ
  * 最小公倍数は ${A  B / gdc}$

### [ABC 141 D](https://atcoder.jp/contests/abc141/tasks/abc141_d)

*  方針
   *  N個の商品に対してM個の商品券を使う際、一枚づつ常に最大値の商品に使用する。
   *  価格が変更された際の並び替えのために、優先度キューアルゴリズム（ヒープソート）を使用する
*  実装
   *  ヒープの作成`heapq.heapify(list)`
   *  最大値の抽出は要素を負にしておいて最小値を抽出する`heapq.heappop(heap)`を使用する
   *  割引後の価格は`heapq.heappush(heap, item)`で追加する

* おまけ
  * [ソートのアルゴリズム](http://sevendays-study.com/algorithm/day3.html)
  * [python標準ライブラリでのヒープキューの使用例](https://docs.python.org/ja/3/library/heapq.html)

### [ABC 140 D](https://atcoder.jp/contests/abc140/tasks/abc140_d)

  * 方針
    * 同じ方向を向いているグループをひとまとめにする
    * 同じグループにまとめられた人は幸せ
    * 一番左の人を左向にする。（右を向いてたら全反転する）
    * 一番左端のひとはどうやっても不幸
    * 圧縮するとLRLR・・・・・交互のリストになっているから、Rを反転できる回数＊2が幸せ増加数となる
      * ただし、右端がLの時とRの時ですべてのRを反転させてLにした際の連続数が1ズレてくるので注意

  * 実装
    * リストを圧縮したあとに幸せ数を数え上げるのは、わざわざ反転したリストをつくらなくても要素数の偶数奇数と操作できる回数で場合分けして数字計算でもとめられる。リストの反転操作を行わなくていいのでそのほうが早い。

``` python
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
        cnt_h += len(arr) - 1
    else:
        cnt_h += 2*K

    return cnt_h
```

### [ABC 139 D](https://atcoder.jp/contests/abc139/tasks/abc139_d)

  * 方針 
    * 余りが最大になるにはある数をある数+1で割ればいい
    * じゃあ数列を数列+1の数で割るようなのがいい。最大値をわる値はつくれないから１当てとけ。。。
    * for文で足していくとTLEするので・・・・等差数列の和の公式　
  * 実装
    * 2行・・・・
  * 気づき
    * N=10^10でfor回しちゃダメってことか
  
### [ABC 138 D](https://atcoder.jp/contests/abc138/tasks/abc138_d)

  * 方針 
    * 木データ構造を作成する
    * 値の追加のたび下流に加算していくと`O(NQ)`となってしまう。加算した場所へ値をおいて、あとから累積和をとることで、加算操作を一回で済ませてしまう。`O(N + Q)`
  * 実装
    * グラフをリストで表現する場合
      * 子と親へのリンクをリストでもつ。
      * 訪問済みノードのリストをもつ
      * 深さ優先探索はLIFOで行うので、探索用stackを有し、`.pop()` と `.append()`　を行う。
    * 木データ構造作成する場合
      * Nodeはノード番号、本問題の加算値、リンク先ノードリストを持つ。訪問済みノードリストもノードの属性として持っていても良かった（今回は訪問済みノードリストを別途保持した）。
      * グラフをリストで表現した場合と同じことを木データ構造で実現する。
      * python3だと計算間に合わないないのでpypy3で提出する。

  * 気づき
    *再帰関数を使うとメモリ制限に引っかかるので、whileで順次実行する
    * スタックでLIFOを使う。LIFOになるので、一番若い者をみながら深さ優先探索にできる。
    * スタックの処理速度向上のために `form collections import deque`を使う。先端後端の出し入れはこのほうが速くなる。
    * 親ノードに遡ると想定している巡回にならないから、親ノードを覚えておいて弾くようにする
    * 有向グラフで定義すれば親を弾く処理はいらないと思ったが、コンテスト後に追加された条件があると無効グラフの親弾き処理をいれないとACできない。
    * 再帰関数をつかうとメモリを大幅に食うため、メモリ制限でREとなる。
    * データ構造をインスタンスオブジェクトで表現すると速度が遅くなり間に合わない。
    * あとちょっと間に合わないときは、pypy3で押し通せる事が分かった。

#### python リスト版

```python
N, Q = [int(item) for item in input().split()]

tree_list = [input().split() for j in range(1, N)]

query_list = [input().split() for k in range(Q)]
query_list_int = [[int(k) for k in i] for i in query_list]

val_list = [0 for _ in range(N)]

linked_node_list = [[] for _ in range(N)]

# 無向グラフのリンク関係を作成（上流への接続も含んでいる）
for a, b in tree_list:
    a, b = int(a)-1, int(b) -1
    linked_node_list[a].append(b) #子の追加
    linked_node_list[b].append(a) #親の追加


for index, val in query_list_int:
    val_list[index-1] += val

stack = [0] #ルートノードの値を入れたスタックを生成、巡回するターゲットを格納する
parent = [0] * (N+1) #訪問済みノードを記憶するスタックを格納する

#再帰関数を使うとメモリ制限に引っかかるので、whileで順次実行する
# スタックでLIFOを使う。LIFOになるので、一番若い者をみながら深さ優先探索にできる。
# 親ノードを覚えておいて弾くようにする
# 有向グラフで定義すれば親を弾く処理はいらない

while True:
    #ルートから順に巡回
    v=stack.pop()
    for child in linked_node_list[v]:
        if child != parent[v]:
            parent[child] = v # 訪問済みノードを格納
            stack.append(child) #このノードvの接続先ノードをスタックに格納
            val_list[child] += val_list[v] #累積和
    if not stack:
        #スタックがなくなれば巡回終了
        break

print(*val_list)
```


#### pypy3 ノードオブジェクト版

``` python

from collections import deque
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
            parent_node = self.node_list[a-1]
            self.node_list[a-1].child_list.append(child_node)
            self.node_list[b-1].child_list.append(parent_node)

    def adding(self, query_list):
        for a, data in query_list:
            a, data = int(a), int(data)
            self.node_list[a-1].cnt += data

        stack = deque([self.node_list[0]])
        parent_node_list = [self.node_list[0]]*(N + 1)

        while True:
            v = stack.pop()
            for child in v.child_list:
                if child != parent_node_list[v.val -1]:
                    child.cnt += v.cnt
                    parent_node_list[child.val -1] = v
                    stack.append(child)

            if not stack:
                break


ins = my_tree(tree_list)
ins.adding(query_list)
print(*[node.cnt for node in ins.node_list])

```

## D問題の練習になる問題

### [Disco2020 B](https://atcoder.jp/contests/ddcc2020-qual/tasks/ddcc2020_qual_b)

* N回合計を計算する問題は、毎回素直に計算すると計算量が膨大になってしまう。
* for文 の中で`sum`を計算させてしまうと、実は知らず知らずの内に二重ループを回していたでござる。ポルナレフ。
* というわけで累積和を上手に使いましょう問題。

```
N = int(input())
A_list = [int(item) for item in input().split()]

all_sum = sum(A_list)

F_sum_list = [A_list[0]]

for j in range(1,N):
    F_sum_list.append(F_sum_list[-1] + A_list[j])

delta_list = [abs(all_sum - 2* i) for i in F_sum_list]

print(min(delta_list))
```

### [ABC 146 C](https://atcoder.jp/contests/abc146/tasks/abc146_c)
* the 二分探索！！

```
A, B, X = [int(item) for item in input().split()]
res_list = []
left = 1 -1
right = 10 ** 9 + 1

is_search = True

while is_search:
    N = (left + right)//2
    res = A * N + B * len(str(N))

    if res > X:
        right = N
    elif res <= X:
        res_list.append(N)
        left = N

    if right - left <= 1:
        is_search = False

if res_list == []:
    print(0)
else:
    print(max(res_list))
```


* 下のコードは最初に思い付きで書いた二分探索。
* このコードだと、絞り方がまずくて解に収束しない場合があったので二分探索の後に、解近傍で検索範囲を絞った線形探索をぶっこむというアホなこ事をやってしまった。
* めちゃくちゃ恥ずかしい。
* こんなこと二度としないよう戒めの為に公開する。

```
import math
 
A, B, X = [int(item) for item in input().split()]
 
res = 0
res_list = []
delta = 10**9 // 4
N= 10**9 // 2
 
 
is_search = True
 
while is_search:
    res = A * N + B * len(str(N))
    if res > X:
        N = N -delta
    elif res <= X:
        res_list.append(N)
        N = N + delta
 
    if delta <= 0:
        break
 
    delta = delta // 2 
 
new_res_list = []
for i in range(N - 1000, N + 1000):
    res = A * i + B * len(str(i))
    if res <= X:
        new_res_list.append(i)
 
 
if new_res_list == [] or max(new_res_list) <1:
    print(0)
else:
    if 1<= max(new_res_list) < 10**9:
        print(max(new_res_list))
    else:
        print(10**9)
```

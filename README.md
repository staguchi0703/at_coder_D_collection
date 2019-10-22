# at_coder_template
## 目的
* VScodeでabcのDランク問題（400点）が取れるように練習するために問題を収集した
* D問題は計算量の見積もりと、計算量を削減するアルゴリズムを知っていることがポイント

## 問題へのリンク
* [ABC 142 D](https://atcoder.jp/contests/abc142/tasks/abc142_d)
* [ABC 141 D](https://atcoder.jp/contests/abc141/tasks/abc141_d)
* [ABC 140 D](https://atcoder.jp/contests/abc140/tasks/abc140_d)
* [ABC 139 D](https://atcoder.jp/contests/abc139/tasks/abc139_d)
* [ABC 138 D](https://atcoder.jp/contests/abc138/tasks/abc138_d)
* [ABC 137 D](https://atcoder.jp/contests/abc137/tasks/abc137_d)

## 回答

* ABC 142 D 
  * 方針
    * 素数の探索は $O{(\sqrt{N})}$
    * 約数を求めるとき(因数分解)も $O{(\sqrt{N})}$

  * 実装
    * 素数探索`for i in range(int(math.sqrt(N))+1)`
    * 最大公約数はユークリッドの互除法` A, B = B, A % B `
    * 因数分解はの時に割り残った値を約数に加えることを忘れない
  * おまけ
    * 最小公倍数は ${A  B / gdc}$

* ABC 141 D 
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
  
* ABC 140 D 
  * 方針
  * 実装
* ABC 139 D 
  * 方針 
  * 実装
* ABC 138 D 
  * 方針 
  * 実装
* ABC 137 D 
  * 方針　
  * 実装


## 使い方

1. ローカルに複製する。　`git clone {repo}`
   * 複製するとローカルリポジトリのディレクトリに自動で飛ぶ。
   * そこで`code .`すれば、そのまま今回のコンテストに必要なディレクトリだけを持ったworkingspaceが立ち上がる。
2. テストケースの値を各問題フォルダの`X_input.txt`にペースト
3. 回答をX.pyに記入
4. 実行して動作確認する。terminalからのpython実行をキーバインドするのが〇
5. cwdは、クローンしてきたリポジトリの先頭にいること（フォルダA~Fが見えているところ）。
6. 19行目からを回答へ投げる
7. 終わったらpushして公開する
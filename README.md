# NaiveBayes_Clastering

<br>1.Wiki用の素性リストの作成
-プログラム名：mk_feature.py

-参照：Wikiのtrain用のテキストデータ

-実行コマンド<br>
python3 mk_feature.py > feature.list

<br>2.train用テキストデータによるナイーブベイズ手法の確率モデルを構築
-プログラム名：bays_learn.py

-参照：train用テキストデータ ＆ feature.list

-実行コマンド<br>
python3 bays_learn.py > model

<br>3.学習済み確率モデルから新規ページ(テストページ)がどのカテゴリかを識別
-プログラム名：bays_classify.py

-参照：model & testページ & feature.list

-実行コマンド<br>
python3 bays_classify.py

-出力：各ページ毎に、識別したカテゴリと確率のlog(尤度)の表示

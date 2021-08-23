<!Doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8">
  </head>
  
  <body>
      <h1>NaiveBayes_Clastering:<br>Wikiをtrainデータとtestデータにわけ、trainデータからtestデータのカテゴリを推定する試み</h1>
      <h3>1.Wiki用の素性リストの作成</h3>
        <ul>
          <li>プログラム名：mk_feature.py</li>
          <li>参照：Wikiのtrain用のテキストデータ</li>
          <li>実行コマンド</li>
            <ul>
              <li>python3 mk_feature.py > feature.list</li>
            </ul>
        </ul>
      <h3>2.train用テキストデータによるナイーブベイズ手法の確率モデルを構築</h3>
        <ul>
          <li>プログラム名：bays_learn.py</li>
          <li>参照：train用テキストデータ ＆ feature.list</li>
          <li>実行コマンド</li>
            <ul>
              python3 bays_learn.py > model
            </ul>
        </ul>
      <h3>3.学習済み確率モデルから新規ページ(テストページ)がどのカテゴリかを識別</h3>
      <ul>
        <li>プログラム名：bays_classify.py</li>
        <li>参照：model & testページ & feature.list</li>
        <li>実行コマンド</li>
          <ul>
            python3 bays_classify.py
          </ul>
        <li>出力：各ページ毎に、識別したカテゴリと確率のlog(尤度)の表示</li>  
       </ul>
   </ol>
   <h3>extra1.環境構築編　Ubuntu(Linux)対応></h3>
     <ol>
      <li>sudo apt update</li> 
       <li>sudo apt upgrade</li>
       <li>sudo apt install vim lv dbus-x11 gconf2 p7zip-full fonts-ipafont gcc g++ make emacs emacs-mozc mecab mecab-ipadic-utf8 swig</li>
     </ol>
   <h3>extra2.Pythonの設定編</h3>
   <ol>
     <li>sudo apt install python3-pip python3-dev</li>
     <li>sudo pip3 install --upgrade pip numpy scikit-learn gensim h5py joblib paramiko mecab-python3 tensorflow keras</li>
     <li>cd /usr/local/etc/　　</li>
     <li>sudo ln -s /etc/mecabrc</li>
   </ol>
 
  </body>
 </html>

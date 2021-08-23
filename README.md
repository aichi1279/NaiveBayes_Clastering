<!Doctype html>
<html lang="ja">
  <head>
    <meta charset="UTF-8">
    <title>NaiveBayes_Clastering:Wikiをtrainデータとtestデータにわけ、trainデータからtestデータのカテゴリを推定する試み</title>
  </head>
  
  <body>
    <ol>
      <li>Wiki用の素性リストの作成</li>
        <ul>
          <li>プログラム名：mk_feature.py</li>

          <li>参照：Wikiのtrain用のテキストデータ</li>

          <li>実行コマンド</li>
            <ul>
              <li>python3 mk_feature.py > feature.list</li>
            </ul>
        </ul>
    <li>train用テキストデータによるナイーブベイズ手法の確率モデルを構築</li>
      <ul>
        <li>プログラム名：bays_learn.py</li>

        <li>参照：train用テキストデータ ＆ feature.list</li>

        <li>実行コマンド</li>
          <ul>
            python3 bays_learn.py > model
          </ul>
      </ul>
    <li>学習済み確率モデルから新規ページ(テストページ)がどのカテゴリかを識別</li>
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
    
    
    
    <環境構築編　Ubuntu(Linux)対応><br>
      sudo apt update <br>
      sudo apt upgrade<br>
      sudo apt install vim lv dbus-x11 gconf2 p7zip-full fonts-ipafont gcc g++ make emacs emacs-mozc mecab mecab-ipadic-utf8 swig
    <br>

    <Pythonの設定編><br>
    sudo apt install python3-pip python3-dev<br>
    sudo pip3 install --upgrade pip numpy scikit-learn gensim h5py joblib paramiko mecab-python3 tensorflow keras<br>
    cd /usr/local/etc/　　<br>
    sudo ln -s /etc/mecabrc<br>
    <br>
      
  </body>
 </html>

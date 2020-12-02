# NaiveBayes_Clastering

<br>#1.Wiki用の素性リストの作成<br>
-プログラム名：mk_feature.py

-参照：Wikiのtrain用のテキストデータ

-実行コマンド<br>
python3 mk_feature.py > feature.list

<br>#2.train用テキストデータによるナイーブベイズ手法の確率モデルを構築<br>
-プログラム名：bays_learn.py

-参照：train用テキストデータ ＆ feature.list

-実行コマンド<br>
python3 bays_learn.py > model

<br>#3.学習済み確率モデルから新規ページ(テストページ)がどのカテゴリかを識別<br>
-プログラム名：bays_classify.py

-参照：model & testページ & feature.list

-実行コマンド<br>
python3 bays_classify.py

-出力：各ページ毎に、識別したカテゴリと確率のlog(尤度)の表示

<br><br>
<環境構築編　Ubuntu(Linux)対応><br>
sudo apt update <br>
sudo apt upgrade<br>
sudo apt install vim<br>
sudo apt install lv<br>
sudo apt install dbus-x11<br>
sudo apt install gconf2<br>
sudo apt install p7zip-full<br>
sudo apt install fonts-ipafont<br>
sudo apt install gcc<br>
sudo apt install g++<br>
sudo apt install make<br>
sudo apt install emacs<br>
sudo apt install emacs-mozc<br>
sudo apt install mecab<br>
sudo apt install mecab-ipadic-utf8<br>
sudo apt install swig<br>

<Pythonの設定編><br>
sudo apt install python3-pip<br>
sudo apt install python3-dev<br>
sudo pip3 install --upgrade pip<br>
sudo pip3 install --upgrade numpy<br>
sudo pip3 install --upgrade scikit-learn<br>
sudo pip3 install --upgrade gensim<br>
sudo pip3 install --upgrade h5py<br>
sudo pip3 install --upgrade joblib<br>
sudo pip3 install --upgrade paramiko<br>
sudo pip3 install --upgrade mecab-python3<br>
sudo pip3 install --upgrade tensorflow<br>
sudo pip3 install --upgrade keras<br>
cd /usr/local/etc/　　<br>
sudo ln -s /etc/mecabrc<br>
<br>

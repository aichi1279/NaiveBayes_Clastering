#!/usr/bin/python3
import sys
import glob
import os
import math
import MeCab

mecab = MeCab.Tagger('')

def main():
    # 学習データの場所
    TrainList = glob.glob("./train/*.txt")
    
    # 学習用データの文書数
    N = len(TrainList)
    
    DF ={}
    for file in TrainList:
        # fileの形態素解析を行い、名詞を取り出す
        TermHash = get_POS_data(file)
	
        # クラスごとの文書頻度を格納
        for noun in TermHash.keys():
            if noun in DF:
                DF[noun] += 1
            else:
                DF[noun] = 1

    # 素性選択（IDFが2以上）
    for noun in DF.keys():
        df = DF[noun]
        idf = math.log2(N/df)
        
        # DFが2以下の名詞は除去
        # IDFが２以下の名詞は除去
        if idf > 2 and df > 2:
            if len(noun) > 1:
                print(noun)


# fileの形態素解析を行う
def get_POS_data(file):
    sentences = getSentence(file)
    
    hash = {}
    for sent in sentences:
        mecab_results = mecab.parse(sent)
        results = mecab_results.split('\n')
        
        for line in results:
            if line == "EOS":
                break
            
            word = line.split('\t')[0]
            pos_info = line.split('\t')[1]
            
            if pos_info.split(',')[0] == "名詞":

                if len(word) > 1:
                    if word in hash:
                        hash[word] += 1
                    else:
                        hash[word] = 1
    return hash

# 本文を取り出す
def getSentence(file):
    sgml = open(file)
    lines = sgml.readlines()

    sentences = []
    for line in lines:
        line = line.rstrip()
        e = line.split(" ")
        tag = e[0];

        # 先頭にタグがある行を除去
        if tag == "<id>" or tag == "<date>" or tag == "<title>":
            continue
        
        if tag == "<company>" or tag == "<class>":
            continue
        
        line = line.lstrip("　")  # 先頭の全角スペースを除去
        line = line.lstrip(" ")   # 先頭の半角スペースを除去

        # 何もない行を除去
        if line == "":
            continue

        if "。" in line:
            sentences.append(line)
        
    return sentences

    
if __name__ == "__main__":
    main()

#!/usr/bin/python3
import glob
import MeCab
from decimal import Decimal

mecab = MeCab.Tagger('')

def main():
    Corpus_name = "./train/*.txt"
    feature_name= "feature.list"
    files = glob.glob(Corpus_name)

    feature_list=[]
    lines = open(feature_name)
    lines = lines.readlines()
    for line in lines:
        line = line.strip('\n')
        feature_list.append(line)


    files.sort()
    class_feature = {}

    for file in files:
        #print(file)
        lines = open(file)
        lines = lines.readlines()
        classname=""
        for line in lines:
            if "<title>" in line or "<id>" in line or "<date>" in line or "<company>" in line:
                continue
            elif "<class>" in line:
                sep = line.split(' ')
                classname = sep[2]
                continue

            mecab_results = mecab.parse(line)
            results = mecab_results.split('\n')
            for res in results:
                if res == "EOS" or "名詞" not in res:
                    continue
                res = res.split('\t')
                key = res[0]

                set_name = classname+':'+key
                if set_name in class_feature and key in feature_list:
                    class_feature[set_name] += 1
                elif set_name not in class_feature and key in feature_list:
                    class_feature[set_name] = 1



    hash = {}
    sum =0
    for key in class_feature.keys():
        sum += class_feature[key]
        key2 = key.split(':')
        if key2[0] in hash:
            hash[key2[0]] += class_feature[key]
        else:
            hash[key2[0]] = class_feature[key]


    print("<feature> "+str(sum) )
    for class_name in hash.keys():
        print("<prior> "+class_name+" "+ str( hash[class_name]/sum ))



    for C_F in class_feature.keys():
        cs_ft = C_F.split(":")
        cs = cs_ft[0]
        num = Decimal(class_feature[C_F]/hash[cs])
        num = round(num, 18)
        print("<conditional> "+C_F+"\t"+ str(num))




if __name__ == "__main__":
        main()

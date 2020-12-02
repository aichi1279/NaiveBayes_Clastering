#!/usr/bin/python3
import MeCab
from decimal import Decimal
import glob
import math

mecab = MeCab.Tagger('')

def main():

    model_name = "./model"
    feature_name= "./feature.list"
    test_name = "./test/*.txt"
    file_ls = glob.glob(test_name)
    file_ls.sort()

    feature_list=[]
    lines = open(feature_name)
    lines = lines.readlines()
    for line in lines:
        line = line.strip('\n')
        feature_list.append(line)


    model_hash = {}
    sum_F = 0
    kind_class=[]
    model_info = open(model_name)
    lines = model_info.readlines()
    for line in lines:
        line = line.strip('\n')
        #print(line)
        if "<feature>" in line:
            line = line.split(' ')
            sum_F = float(line[1])
        elif "<prior>" in line:
            line = line.split(' ')
            model_hash[line[1]] = float(line[2])
        elif "<conditional>" in line:
            line = line.split(' ')
            line = line[1]
            line = line.split('\t')
            model_hash[line[0]] = float(line[1])
            line = line[0].split(":")
            kind_class.append(line[0])

    kind_class = set(kind_class)
    #print(kind_class)
    #for key in model_hash.keys():
    #    print(key+"   "+str(model_hash[key]))

    #-------------------------------------------------------------------------

    list=[]
    for file in file_ls:
        #print(file)
        lines = open(file)
        lines = lines.readlines()
        index_hash = {}
        for line in lines:
            if "<id>" in line or "<date>" in line or "<company>" in line or "<title>" in line or "<class>" in line or "。" not in line:
                continue

            mecab_results = mecab.parse(line)
            results = mecab_results.split('\n')
            for mec in results:
                if mec=="EOF" or "名詞" not in mec:
                    continue

                mec = mec.split('\t')
                noun = mec[0]
                for key in kind_class:
                    set_name = key+':'+noun
                    if noun in feature_list and set_name in model_hash:
                        if key in index_hash:
                            index_hash[key] += math.log2(model_hash[set_name])
                        else:
                            index_hash[key] = math.log2(model_hash[key]) + math.log2(model_hash[set_name])


                    elif  noun in feature_list and set_name not in model_hash:
                        if  key in index_hash:
                            index_hash[key] += math.log2(1/sum_F)
                        else:
                            index_hash[key] = math.log2(model_hash[key]) + math.log2(1/sum_F)


        file = file.split('/')
        mini = 100000
        for CL in index_hash.keys():
            index_hash[CL]= -1 * index_hash[CL]
            if mini > index_hash[CL]:
                mini = index_hash[CL]
                name = CL

        list.append(file[-1]+": "+name+" "+str(mini*(-1)))


    for one in list:
        print(one)

if __name__ == "__main__":
        main()

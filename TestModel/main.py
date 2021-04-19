import os ,sys
from functools import reduce
from TestModel.models import *

import jieba ,codecs,math
import jieba.posseg as pseg
import jieba
from django.utils.module_loading import module_dir

names={}
relationships={}
linesnames=[]
all_name=[]
my_nodes=[]
with open('../ handle/jinyong_all_person0.txt' ,'r+',encoding='utf-8') as f:
    for line in f.readlines():
        line=line.strip()
        all_name.append(line)
        my_nodes.append({"name":line})
print(all_name)

excludes = {'左骑军'}

fei_nodes=[]
fei_name_nodes=[]
with codecs.open("../ handle/金庸05射雕英雄传.txt",'r',encoding='utf-8')as f:
    for line in f.readlines():
        poss=pseg.cut(line)
        linesnames.append([])
        for w in poss:
            if w.word not in all_name:
                continue
            real_word = w.word
            print("==="*30)
            print(real_word)
            print("==="*30)
            fei_nodes.append({"name":real_word})
            fei_name_nodes.append(real_word)
            linesnames[-1].append(real_word)
            if names.get(real_word) is None:
                names[real_word]=0
                relationships[real_word]={}
            names[real_word]+=1
fei_nodes = reduce(lambda x, y: x if y in x else x + [y], [[], ] + fei_nodes)
fei_name_node=set(fei_name_nodes)





for line in linesnames:
    print(line)
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                print(name1,name2)
                relationships[name1][name2]=1
            else:
                relationships[name1][name2]=relationships[name1][name2]+1
links=[]
fei_nodes=[]
fei_name_nodes=[]
for name,id in zip(fei_name_node,range(1000)):
    person=Persons(id=id,name=name,book="she")
    person.save()
    fei_name_nodes.append(name)
for node in fei_name_node:
    fei_nodes.append({"id":node,"text":node})
print("**"*30)
print(len(fei_nodes))
print("**"*30)
print(len(fei_name_nodes))
print("**"*30)
print(len)
with codecs.open("fei.txt","w","gbk")as f:
    f.write("Source Target Weight\r\n")
    for name,edges in relationships.items():
        for v,w in edges.items():
            if w>50:
                f.write(name+" "+v+" "+str(w)+"\r\n")
                links.append({"from":name,"to":v})
                Link=Links(book="she",person_a=name,person_b=v,a_id=fei_name_nodes.index(name),b_id=fei_name_nodes.index(v))
                Link.save()

    print("=="*30)
    print(links)
import json
jsondata={'nodes': fei_nodes,"links":links}
f = open('she.json', 'w')
jsondata =json.dumps(jsondata)
f.write(jsondata)
f.close()
# file_path = os.path.join(module_dir, 'the_actions.txt')
# with open(file_path, "r+", encoding="utf-8")as f:
#   for line in f.readlines():
#     line = line.strip()
#     if line != '':
#       dict = line.split("，", 1)
#       print(dict)
#       the_action=Actions(date=dict[0],description=dict[1])
#       the_action.save()
#       lists.append(dict)


import os ,sys
from functools import reduce

import jieba ,codecs,math
import jieba.posseg as pseg
import jieba
import pymysql


# 使用execute()方法执行SQL查询
names = {}
relationships = {}
linesnames = []
all_name = []
my_nodes = []
with open("jinyong_all_person0.txt", 'r+', encoding='utf-8') as f:
    for line in f.readlines():
      line = line.strip()
      all_name.append(line)
      my_nodes.append({"name": line})
print(all_name)

excludes = {'左骑军'}

fei_nodes = []
fei_name_nodes = []

with codecs.open("金庸07鹿鼎记.txt", 'r', encoding='utf-8')as f:
    for line in f.readlines():
      poss = pseg.cut(line)
      linesnames.append([])
      for w in poss:
        if w.word not in all_name:
          continue
        real_word = w.word
        print("===" * 30)
        print(real_word)
        print("===" * 30)
        fei_nodes.append({"name": real_word})
        fei_name_nodes.append(real_word)
        linesnames[-1].append(real_word)
        if names.get(real_word) is None:
          names[real_word] = 0
          relationships[real_word] = {}
        names[real_word] += 1
fei_nodes = reduce(lambda x, y: x if y in x else x + [y], [[], ] + fei_nodes)
fei_name_node = set(fei_name_nodes)

for line in linesnames:
    print(line)
    for name1 in line:
      for name2 in line:
        if name1 == name2:
          continue
        if relationships[name1].get(name2) is None:
          print(name1, name2)
          relationships[name1][name2] = 1
        else:
          relationships[name1][name2] = relationships[name1][name2] + 1
links = []
fei_nodes = []
db=pymysql.connect(host="39.108.139.175",user="lannister",port=3306,passwd="lannister",db="web_jy",charset='utf8')
cursor = db.cursor()
for name, id in zip(fei_name_node, range(1200,1400,1)):
    print(id,name,"fei")
    sql = "INSERT INTO TestModel_persons(id, \
           name,book,img) \
           VALUES (%s,'%s','%s','%s')" % \
          (id, name, "lu","null")

        # 执行sql语句
    cursor.execute(sql)
        # 提交到数据库执行
    db.commit()
    print("person提交")

fei_name_nodes=[]
for node in fei_name_node:
    fei_name_nodes.append(node)
    fei_nodes.append({"id": node, "text": node})
print("**" * 30)
print(len(fei_nodes))
print("**" * 30)
print(len(fei_name_nodes))
print("**" * 30)
print(len)
with codecs.open("fei.txt", "w", "gbk")as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
      for v, w in edges.items():
        if w > 30:
          f.write(name + " " + v + " " + str(w) + "\r\n")
          links.append({"from": name, "to": v})
          # Link = Links(book="shen", person_a=name, person_b=v, a_id=fei_name_nodes.index(name),
          #              b_id=fei_name_nodes.index(v))
          sql = "INSERT INTO TestModel_links(book, \
                     person_a, person_b,a_id,b_id,relation) \
                     VALUES ('%s','%s','%s',%s,%s,'%s')" % \
                ("lu", name, v,fei_name_nodes.index(name)+1200,fei_name_nodes.index(v)+1200,"待定")

          try:
              # 执行sql语句
              cursor.execute(sql)
              # 提交到数据库执行
              db.commit()
              print("relation 成功")
          except:
              # 如果发生错误则回滚
              db.rollback()

    print("==" * 30)
    print(links)
import json
jsondata = {'nodes': fei_nodes, "links": links}
f = open('shen.json', 'w')
jsondata = json.dumps(jsondata)
f.write(jsondata)
f.close()


print("gggggggggggggggggggg")


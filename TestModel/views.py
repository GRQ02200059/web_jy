import os

from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.http import require_http_methods

from TestModel.models import Actions
import os, sys
# from functools import reduce
from TestModel.models import *
#
# import jieba, codecs, math
# import jieba.posseg as pseg
# import jieba
# from django.utils.module_loading import module_dir
def select(request):
  if request.method=='POST':
    name = request.POST.get("text")
    book=request.POST.get("book")

    print("==="*30)
    print(name,book)
    print("===" * 30)
    if (book == "fei"):
      # node_lists = Links.objects.filter(book=book)
      #
      # the_nodes = []
      # for node in node_lists:
      #   print("jinlllll")
      #   the_nodes.append({"source": int(node.a_id) - 200, "target": int(node.b_id) - 200, "relation": node.relation})
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id)-200, "target": int(node.b_id)-200, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id)-200, "target": int(node.b_id)-200, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "xue"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id) - 400, "target": int(node.b_id) - 400, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id) - 400, "target": int(node.b_id) - 400, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "lian"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id) - 600, "target": int(node.b_id) - 600, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id) - 600, "target": int(node.b_id) - 600, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "tian"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id) - 800, "target": int(node.b_id) - 800, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id) - 800, "target": int(node.b_id) - 800, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "she"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id), "target": int(node.b_id), "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id), "target": int(node.b_id), "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "bai"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id) - 1000, "target": int(node.b_id) - 1000, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id) - 1000, "target": int(node.b_id) - 1000, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "lu"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id) - 1200, "target": int(node.b_id) - 1200, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id) - 1200, "target": int(node.b_id) - 1200, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "shu"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id) - 1400, "target": int(node.b_id) - 1400, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id) - 1400, "target": int(node.b_id) - 1400, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "xiao"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id) - 1600, "target": int(node.b_id) - 1600, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id) - 1600, "target": int(node.b_id) - 1600, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "shen"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id) - 1800, "target": int(node.b_id) - 1800, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id) - 1800, "target": int(node.b_id) - 1800, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "jian"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id) - 2000, "target": int(node.b_id) - 2000, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id) - 2000, "target": int(node.b_id) - 2000, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "yi"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id) - 2200, "target": int(node.b_id) - 2200, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id) - 2200, "target": int(node.b_id) - 2200, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "bi"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id) - 2400, "target": int(node.b_id) - 2400, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id) - 2400, "target": int(node.b_id) - 2400, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))
    elif (book == "yuan"):
      list1 = Links.objects.filter(person_a=name, book=book)
      print(len(list1))
      list2 = Links.objects.filter(person_b=name, book=book)
      print(len(list2))

      the_nodes = []
      for node in list1:
        the_nodes.append({"source": int(node.a_id) - 2600, "target": int(node.b_id) - 2600, "relation": node.relation})
      for node in list2:
        the_nodes.append({"source": int(node.a_id) - 2600, "target": int(node.b_id) - 2600, "relation": node.relation})
      lists = Persons.objects.filter(book=book)
      the_lists = []
      for list in lists:
        the_lists.append({"name": list.name, "role_id": list.id, "avatar": list.img})

      data = {"nodes": the_lists, "links": the_nodes}
      print(len(the_lists), len(the_nodes))





    return render(request, "relationship.html", {"data": data, "book": book})



def index(request):
  # module_dir = os.path.dirname(__file__)
  # file_path = os.path.join(module_dir, 'jinyong_all_person0.txt')
  # with open(file_path, "r+", encoding="utf-8")as f:
  #   for line in f.readlines():
  #     line = line.strip()
  #     if line != '':
  #       dict = line.split("，", 1)
  #       print(dict)
  #       the_action=Actions(date=dict[0],description=dict[1])
  #       the_action.save()
  #       lists.append(dict)


  # names = {}
  # relationships = {}
  # linesnames = []
  # all_name = []
  # my_nodes = []
  # with open(file_path, 'r+', encoding='utf-8') as f:
  #   for line in f.readlines():
  #     line = line.strip()
  #     all_name.append(line)
  #     my_nodes.append({"name": line})
  # print(all_name)
  #
  # excludes = {'左骑军'}
  #
  # fei_nodes = []
  # fei_name_nodes = []
  # file_path = os.path.join(module_dir, '金庸10神雕侠侣.txt')
  #
  # with codecs.open(file_path, 'r', encoding='utf-8')as f:
  #   for line in f.readlines():
  #     poss = pseg.cut(line)
  #     linesnames.append([])
  #     for w in poss:
  #       if w.word not in all_name:
  #         continue
  #       real_word = w.word
  #       print("===" * 30)
  #       print(real_word)
  #       print("===" * 30)
  #       fei_nodes.append({"name": real_word})
  #       fei_name_nodes.append(real_word)
  #       linesnames[-1].append(real_word)
  #       if names.get(real_word) is None:
  #         names[real_word] = 0
  #         relationships[real_word] = {}
  #       names[real_word] += 1
  # fei_nodes = reduce(lambda x, y: x if y in x else x + [y], [[], ] + fei_nodes)
  # fei_name_node = set(fei_name_nodes)
  #
  # for line in linesnames:
  #   print(line)
  #   for name1 in line:
  #     for name2 in line:
  #       if name1 == name2:
  #         continue
  #       if relationships[name1].get(name2) is None:
  #         print(name1, name2)
  #         relationships[name1][name2] = 1
  #       else:
  #         relationships[name1][name2] = relationships[name1][name2] + 1
  # links = []
  # fei_nodes = []
  # fei_name_nodes = []
  # for name, id in zip(fei_name_node, range(1000)):
  #   person = Persons(id=id, name=name, book="shen")
  #   person.save()
  #   fei_name_nodes.append(name)
  # for node in fei_name_node:
  #   fei_nodes.append({"id": node, "text": node})
  # print("**" * 30)
  # print(len(fei_nodes))
  # print("**" * 30)
  # print(len(fei_name_nodes))
  # print("**" * 30)
  # print(len)
  # with codecs.open("fei.txt", "w", "gbk")as f:
  #   f.write("Source Target Weight\r\n")
  #   for name, edges in relationships.items():
  #     for v, w in edges.items():
  #       if w > 50:
  #         f.write(name + " " + v + " " + str(w) + "\r\n")
  #         links.append({"from": name, "to": v})
  #         Link = Links(book="shen", person_a=name, person_b=v, a_id=fei_name_nodes.index(name),
  #                      b_id=fei_name_nodes.index(v))
  #         Link.save()
  #
  #   print("==" * 30)
  #   print(links)
  # import json
  # jsondata = {'nodes': fei_nodes, "links": links}
  # f = open('shen.json', 'w')
  # jsondata = json.dumps(jsondata)
  # f.write(jsondata)
  # f.close()
  #

  print("gggggggggggggggggggg")
  return   render(request, "index.html")
def timeline(request):

  lists = []
  module_dir = os.path.dirname(__file__)
  file_path = os.path.join(module_dir, 'the_actions.txt')
  # with open(file_path, "r+", encoding="utf-8")as f:
  #   for line in f.readlines():
  #     line = line.strip()
  #     if line != '':
  #       dict = line.split("，", 1)
  #       print(dict)
  #       the_action=Actions(date=dict[0],description=dict[1])
  #       the_action.save()
  #       lists.append(dict)

  all_actions=Actions.objects.all()




  return  render(request, "timeline.html",{"actions":all_actions})
def detail(request,book):


  if(book=="飞"):
    pass
    # book="fei"
    # node_lists = Links.objects.filter(book=book)
    #
    # the_nodes = []
    # for node in node_lists:
    #   print("jinlllll")
    #   the_nodes.append({"source": int(node.a_id)-200, "target": int(node.b_id)-200, "relation": node.relation})
  elif(book=="雪"):
    pass
    # book="xue"
    # node_lists = Links.objects.filter(book=book)
    # the_nodes = []
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id)-400, "target": int(node.b_id)-400, "relation": node.relation})
  elif (book == "连"):
    pass
    # book = "lian"
    #
    # the_nodes = []
    # node_lists = Links.objects.filter(book=book)
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id)-600, "target": int(node.b_id)-600, "relation": node.relation})
  elif (book == "天"):
    pass
    # book = "tian"
    #
    # the_nodes = []
    # node_lists = Links.objects.filter(book=book)
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id)-800, "target": int(node.b_id)-800, "relation": node.relation})
  elif (book == "射"):
    pass
    # book = "she"
    #
    # node_lists = Links.objects.filter(book=book)
    # the_nodes = []
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id), "target": int(node.b_id), "relation": node.relation})
  elif (book == "白"):
    # book = "bai"
    #
    # node_lists = Links.objects.filter(book=book)
    # the_nodes = []
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id)-1000, "target": int(node.b_id)-1000, "relation": node.relation})
    pass
  elif (book == "鹿"):
    # book = "lu"
    #
    # node_lists = Links.objects.filter(book=book)
    # the_nodes = []
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id)-1200, "target": int(node.b_id)-1200, "relation": node.relation})
    pass
  elif (book == "书"):
    # book = "shu"
    #
    # node_lists = Links.objects.filter(book=book)
    # the_nodes = []
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id)-1400, "target": int(node.b_id)-1400, "relation": node.relation})
    pass
  elif (book == "笑"):
    # book = "xiao"
    #
    # node_lists = Links.objects.filter(book=book)
    # the_nodes = []
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id)-1600, "target": int(node.b_id)-1600, "relation": node.relation})
    pass
  elif (book == "神"):
    # book = "shen"
    #
    # node_lists = Links.objects.filter(book=book)
    # the_nodes = []
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id)-1800, "target": int(node.b_id)-1800, "relation": node.relation})
    pass
  elif (book == "剑"):
    # book = "jian"
    #
    # node_lists = Links.objects.filter(book=book)
    # the_nodes = []
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id)-2000, "target": int(node.b_id)-2000, "relation": node.relation})
    pass
  elif (book == "倚"):
    # book = "yi"
    #
    # node_lists = Links.objects.filter(book=book)
    # the_nodes = []
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id)-2200, "target": int(node.b_id)-2200, "relation": node.relation})
    pass
  elif (book == "碧"):
    # book = "bi"
    #
    # node_lists = Links.objects.filter(book=book)
    # the_nodes = []
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id)-2400, "target": int(node.b_id)-2400, "relation": node.relation})
    pass
  elif (book == "鸳"):
    # book = "yuan"
    # node_lists = Links.objects.filter(book=book)
    # the_nodes = []
    # for node in node_lists:
    #   the_nodes.append({"source": int(node.a_id)-2600, "target": int(node.b_id)-2600, "relation": node.relation})
    pass



  # lists=Persons.objects.filter(book=book)
  # the_lists=[]
  # for list in lists:
  #   the_lists.append({"name":list.name,"role_id":list.id})
  #
  # data={"nodes":the_lists,"links":the_nodes}




  return render(request, "detail.html")
import json
def relationship(request,book):
  if (book == "飞"):
    book = "fei"
    node_lists = Links.objects.filter(book=book)

    the_nodes = []
    for node in node_lists:
      print("jinlllll")
      the_nodes.append({"source": int(node.a_id) - 200, "target": int(node.b_id) - 200, "relation": node.relation})
  elif (book == "雪"):
    book = "xue"
    node_lists = Links.objects.filter(book=book)
    the_nodes = []
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id) - 400, "target": int(node.b_id) - 400, "relation": node.relation})
  elif (book == "连"):
    book = "lian"

    the_nodes = []
    node_lists = Links.objects.filter(book=book)
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id) - 600, "target": int(node.b_id) - 600, "relation": node.relation})
  elif (book == "天"):
    book = "tian"

    the_nodes = []
    node_lists = Links.objects.filter(book=book)
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id) - 800, "target": int(node.b_id) - 800, "relation": node.relation})
  elif (book == "射"):
    book = "she"

    node_lists = Links.objects.filter(book=book)
    the_nodes = []
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id), "target": int(node.b_id), "relation": node.relation})
  elif (book == "白"):
    book = "bai"

    node_lists = Links.objects.filter(book=book)
    the_nodes = []
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id) - 1000, "target": int(node.b_id) - 1000, "relation": node.relation})
  elif (book == "鹿"):
    book = "lu"

    node_lists = Links.objects.filter(book=book)
    the_nodes = []
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id) - 1200, "target": int(node.b_id) - 1200, "relation": node.relation})
  elif (book == "书"):
    book = "shu"

    node_lists = Links.objects.filter(book=book)
    the_nodes = []
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id) - 1400, "target": int(node.b_id) - 1400, "relation": node.relation})
  elif (book == "笑"):
    book = "xiao"

    node_lists = Links.objects.filter(book=book)
    the_nodes = []
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id) - 1600, "target": int(node.b_id) - 1600, "relation": node.relation})
  elif (book == "神"):
    book = "shen"

    node_lists = Links.objects.filter(book=book)
    the_nodes = []
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id) - 1800, "target": int(node.b_id) - 1800, "relation": node.relation})
  elif (book == "剑"):
    book = "jian"

    node_lists = Links.objects.filter(book=book)
    the_nodes = []
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id) - 2000, "target": int(node.b_id) - 2000, "relation": node.relation})
  elif (book == "倚"):
    book = "yi"

    node_lists = Links.objects.filter(book=book)
    the_nodes = []
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id) - 2200, "target": int(node.b_id) - 2200, "relation": node.relation})
  elif (book == "碧"):
    book = "bi"

    node_lists = Links.objects.filter(book=book)
    the_nodes = []
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id) - 2400, "target": int(node.b_id) - 2400, "relation": node.relation})
  elif (book == "鸳"):
    book = "yuan"
    node_lists = Links.objects.filter(book=book)
    the_nodes = []
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id) - 2600, "target": int(node.b_id) - 2600, "relation": node.relation})
  else:
    book = "she"

    node_lists = Links.objects.filter(book=book)
    the_nodes = []
    for node in node_lists:
      the_nodes.append({"source": int(node.a_id), "target": int(node.b_id), "relation": node.relation})

  lists = Persons.objects.filter(book=book)
  the_lists = []
  for list in lists:
    the_lists.append({"name": list.name, "role_id": list.id,"avatar":list.img})

  data = {"nodes": the_lists, "links": the_nodes}

  return render(request, "relationship.html", {"data": data,"book":book})
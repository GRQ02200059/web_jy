string=' '+'10'+' '+'nr'+'\n'
text=''
with open('jinyong_all_person.txt' ,'r+',encoding='utf-8') as f:
    for line in f.readlines():

        text+=line.strip()+string

f.close()
with open('jinyong_all_person.txt','w+',encoding='utf-8')as f:
    f.write(text)
f.close()
import pymysql
db=pymysql.connect(host="39.108.139.175",user="lannister",port=3306,passwd="lannister",db="web_jy",charset='utf8')
cursor = db.cursor()
m="sadfasfasdfffff"
sql = "INSERT INTO TestModel_links(book, \
                     person_a, person_b,a_id,b_id,relation) \
                     VALUES ('%s','%s','%s',%s,%s,'%s')" % \
                ("fei", 'name','name2', 100000,100000,"待定")
cursor.execute(sql)
db.commit()
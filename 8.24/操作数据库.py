import pymysql
db=pymysql.connect('localhost','root','123456','text')
cussro=db.cursor()
sql="select * from people"
cussro.execute(sql)
db.commit()
db.close()

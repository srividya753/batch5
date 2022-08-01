import mysql.connector as mysql




mydb=mysql.connect(host="localhost",user="root",password="root",database="company")



mycus=mydb.cursor()


e=input("ename")
j=input("job ")
s=int(input("salary "))

query="insert into software(ename,job,salary)values('{}','{}',{})".format(e,j,s)

mycus.execute(query)
mydb.commit()

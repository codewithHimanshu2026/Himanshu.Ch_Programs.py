'''import sqlite3
conn=sqlite3.connect("sqlite.db")

conn.execute('''
'''Create table student1
(
student1_id  int primary key,
student1_name  varchar(50),
student1_class  char(50),
student1_email  varchar(50)
)'''
''')

conn.close()'''

import sqlite3
conn=sqlite3.connect("sqlite.db")

ins='''insert into student1(student1_id,student1_name,student1_class,student1_email)
values(16,"Himanshu Jaat","Btech","xyz@gmail.com")'''
conn.execute(ins)
conn.commit()
conn.close()






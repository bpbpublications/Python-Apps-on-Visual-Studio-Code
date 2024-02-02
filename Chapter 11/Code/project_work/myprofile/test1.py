import sqlite3

con =sqlite3.connect("data.sqlite")
q1  ="Select * from details"
q2 = "Update Users set acc_type=0 where ID=2"
q3  ="Delete from Testimonials"
q4 = "PRAGMA table_info(details)"
q5 = "Select * from users"

q6="Drop table Details"
q7='''Create table Details(ID Integer primary key,
org text,
startdate date,
enddate date,
title Text,
description Text,
info_type Text)'''

#q8 = '''Delete from Details'''
#con.execute(q8)
#q8='''Insert into Details values(6,'ABC Company','01-01-2019','01-01-2020','Design Specialist','Design the software code','Project')'''
#con.execute(q8)
#q8='''Insert into Details values(2,'ABC Company','01-01-2019','01-01-2020','Work Ex Specialist','Design the software code','Work Experience')'''
#con.execute(q8)
#q8='''Insert into Details values(7,'ABC Company','01-01-2019','01-01-2020','Expertise Specialist','Design the software code','Expertise')'''
con.execute(q3)
##q8='''Insert into Details values(8,'ABC Company','01-01-2019','01-01-2020','Education Specialist','Design the software code','Education')'''
#con.execute(q8)
con.commit()
rset = con.execute(q1)
#print("RSET = ",list(rset))
for r in rset:
    print(r)
con.close()
import sqlite3
data = sqlite3.connect("hospital.db")
result = data.execute("select * from patient")
for i in result:
    print("patient id",i[0])
    print("patient name",i[1])
    print("patient address",i[2])
    print("patient phone number",i[3])
    print("patient email-id",i[4])
    print("patient pincode",i[5])
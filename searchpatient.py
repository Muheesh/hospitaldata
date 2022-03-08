import sqlite3
data = sqlite3.connect("hospital.db")
getPid = input("Enter the patient id to be searched:")
result = data.execute("select * from patient where id="+getPid)
for i in result:
    print("ID", i[0])
    print("Patient name", i[1])
    print("Patient address", i[2])
    print("Patient phone number", i[3])
    print("Patient email-id", i[4])
    print("Patient pincode", i[5])
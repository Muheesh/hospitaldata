import sqlite3
data = sqlite3.connect("hospital.db")
getPid = input("Enter the patient Id to be updated:")
getPname = input("Enter the new patient name:")
getPadrreess = input("Enter the new patient address:")
getPphno = input("Enter the new patient phone number:")
getPemail = input("Enter the new patient email-id:")
getPpincode = input("Enter the new patient pincode")
data.execute("update patient set pname = '"+getPname+"',paddress='"+getPadrreess+"',pphno="+getPphno+",\
pemail='"+getPemail+"',ppincode="+getPpincode+" where id="+getPid)
data.commit()
print("updated successfully")
result = data.execute("select * from patient")
for i in result:
    print("ID",i[0])
    print("Patient name", i[1])
    print("Patient address", i[2])
    print("Patient phone number", i[3])
    print("Patient email-id", i[4])
    print("Patient pincode", i[5])
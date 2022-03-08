import sqlite3
patientdata = sqlite3.connect("hospital.db")
patientdata.execute('''create table patient(
                        Id integer,
                        pname text,
                        paddress text,
                        pphno integer,
                        pemail text,
                        ppincode integer
);''')
getId = input("Enter patient ID: ")
getPname = input("Enter patient name: ")
getPaddress = input("Enter patient address: ")
getPphno = input("Enter patient phone number:")
getPemail = input("Enter patient email id:")
getPpincode = input("Enter patient pincode:")
patientdata.execute("insert into patient(Id,pname,paddress,pphno,pemail,ppincode)\
values("+getId+",'"+getPname+"','"+getPaddress+"',"+getPphno+",'"+getPemail+"',"+getPpincode+")")
patientdata.commit()
patientdata.close()
doctor = sqlite3.connect("hospital.db")
doctor.execute('''create table doctordata(
                        drname text,
                        qualification text,
                        draddress text,
                        drphno integer,
                        dremail text
);''')
getDrname = input("Enter doctor name:")
getDrquali = input("Enter doctor qualification:")
getDraddress = input("Enter doctor address:")
getDrphno = input("Enter doctor Phone number:")
getDremail = input("Enter doctor email id:")
doctor.execute("insert into doctordata(drname,qualification,draddress,drphno,dremail)\
values('"+getDrname+"','"+getDrquali+"','"+getDraddress+"',"+getDrphno+",'"+getDremail+"')")
doctor.commit()
doctor.close()
print("Table created and inserted for patient and doctor")

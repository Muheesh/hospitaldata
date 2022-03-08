import sqlite3
data = sqlite3.connect("hospital.db")
getDrphno = input("Enter the doctor phone number to be searched:")
result = data.execute("select * from doctordata where drphno="+getDrphno)
for i in result:
    print("Doctor name", i[0])
    print("qualification", i[1])
    print("Doctor address", i[2])
    print("Doctor phone number", i[3])
    print("Doctor email-id", i[4])
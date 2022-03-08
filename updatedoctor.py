import sqlite3
data = sqlite3.connect("hospital.db")
getDrphno = input("Enter the doctor phone number to be updated:")
getDrname = input("Enter the new doctor name:")
getDrquali = input("Enter the new doctor qualification:")
getDraddress = input("Enter the new doctor address:")
getDremail = input("Enter the new doctor email-id:")
data.execute("update doctordata set drname = '"+getDrname+"',qualification='"+getDrquali+"',\
draddress='"+getDraddress+"',dremail='"+getDremail+"' where drphno="+getDrphno)
data.commit()
print("updated successfully")
result = data.execute("select * from doctordata")
for i in result:
    print("Doctor name",i[0])
    print("qualification", i[1])
    print("Doctor address", i[2])
    print("Doctor phone number", i[3])
    print("Doctor email-id", i[4])

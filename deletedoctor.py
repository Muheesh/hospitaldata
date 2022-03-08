import sqlite3
data = sqlite3.connect("hospital.db")
getDrphno = input("Enter doctor phone number to be deleted")
data.execute("delete from doctordata where drphno="+getDrphno)
data.commit()
print("Deleted successfully")
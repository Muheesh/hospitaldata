import sqlite3
data = sqlite3.connect("hospital.db")
getPid = input("Enter patient id to be deleted")
data.execute("delete from patient where Id="+getPid)
data.commit()
print("Deleted successfully")
import sqlite3

f = open("periodic.txt", "r", encoding = "UTF-8")
data = []
for sor in f:
    data.append(sor.strip().split(","))
data.remove(data[0])
f.close()



con = sqlite3.connect("periodictable.db")

cur = con.cursor()

cur.execute("CREATE TABLE periodic(atomicnumber, element, symbol, atomicmass)")

cur.executemany("INSERT INTO periodic VALUES(?, ?, ?, ?)", data)


res = cur.execute("SELECT element FROM periodic WHERE atomicmass > 1")
print(res.fetchall())
con.commit()

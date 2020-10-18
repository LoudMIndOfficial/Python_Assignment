import sqlite3

conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_data1( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileType TEXT \
        )")

col_fileType = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

for x in col_fileType:
    x.endswith(".txt")
    
conn = sqlite3.connect('assignment.db')


with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_data1(col_fileType) VALUES(?),[x]")


    conn.commit()
conn.close()


print(cur.rowcount, "record inserted.")













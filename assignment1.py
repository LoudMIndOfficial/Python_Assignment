import sqlite3

conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_data2( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileType TEXT \
        )")

col_fileType = ('information.docx','Hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

with conn:
    cur = conn.cursor()
    for x in col_fileType:
        if x.endswith(".txt"):
            cur.execute("INSERT INTO tbl_data2(col_fileType) VALUES(?)",(x,))
    conn.commit()
conn.close()

conn = sqlite3.connect('assignment.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_data2")
    results = cur.fetchall()
    print(results)
conn.close()














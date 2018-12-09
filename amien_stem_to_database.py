import sqlite3
from amien_stemmer import encode
from nltk.tokenize import word_tokenize

sql_update_text_id = '''update id_zhcn set tok_id = ? where id= ?  '''
filepath = 'gabungan.db'

db_connection = sqlite3.connect(filepath)
db_cur = db_connection.cursor()  # type: Cursor
db_cur.execute(
    "select id, text_id from id_zhcn ")
textnya = db_cur.fetchall()
count =  len(textnya)
posisi = count//10000
hitung = 0
print(posisi)
token = []
for text in textnya:
    for kata in word_tokenize(text[1]):
        token.append(encode(kata) if len(kata)!=1 else kata)
    hasil = ' '.join(token)
    token =[]
    db_cur.execute(sql_update_text_id,[hasil,text[0]])
    hitung+=1
    if hitung%posisi==0:
        print((hitung/count)*100)


db_connection.commit()
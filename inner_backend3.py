import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta


def connect():
    conn=sqlite3.connect("inner.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, imie text, model text, adres text, data text, historia text)")
    conn.commit()
    conn.close()

def dodaj(imie,model,adres,data,historia):
    conn=sqlite3.connect("inner.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?)",(imie,model,adres,data,historia))
    conn.commit()
    conn.close()

def wyswietl():
    conn=sqlite3.connect("inner.db")
    cur=conn.cursor()
    cur.execute("SELECT id, imie, model, adres, data FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def history(id):
    conn=sqlite3.connect("inner.db")
    cur=conn.cursor()
    cur.execute("SELECT historia FROM book WHERE id=?",(id,))
    rows=cur.fetchall()
    conn.close()
    return rows


def usun(id):
    conn=sqlite3.connect("inner.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def szukaj(imie="",model="",adres="",data=""):
    conn=sqlite3.connect("inner.db")
    cur=conn.cursor()
    cur.execute("SELECT id,imie,model,adres,data FROM book WHERE imie=? OR model=? OR adres=? OR data=?", (imie,model,adres,data))
    rows=cur.fetchall()
    conn.close()
    return rows

def zmien(id,imie,model,adres,data,historia):
    conn=sqlite3.connect("inner.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET imie=?, model=?, adres=?, data=?, historia=? WHERE id=?",(imie,model,adres,data,historia,id))
    conn.commit()
    conn.close()

"""
funkcja sql ktora wyswietla wszystkie wizyty starsze i rowne 6 miesiecy temu
"""
def test():
    #now = datetime.now().date()
    six_months = datetime.now().date() + relativedelta(months=-12)
    conn=sqlite3.connect("inner.db")
    cur=conn.cursor()
    cur.execute("SELECT id, imie, model, adres, data FROM book WHERE data <=?",(six_months,))
    rows=cur.fetchall()
    conn.close()
    return rows

connect()
#usun(2)
#dodaj("Tomasz", "Bond", "wzgorze ber 162 Gdynia", 111)
#zmien("1","maja","mama","erl","2018-12-12","kebabos")
#print(szukaj('maja'))
#print(wyswietl())
#print(test())

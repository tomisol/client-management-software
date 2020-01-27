from tkinter import *
import inner_backend3
from datetime import datetime
from tkinter import messagebox

"""
Tuple
"""
def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
        e5.delete(0.0, END)
        # e5.insert(END, selected_tuple[5])
        for row in inner_backend3.history(selected_tuple[0]):
            e5.insert(END, str(row[0]) + ' ')
    except IndexError:
        pass

"""
Double Left Click function
"""
def click(event):
    try:
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        list1.delete(0, END)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
        e5.delete(0.0, END)
        list1.insert(END, selected_tuple)
        for row in inner_backend3.history(selected_tuple[0]):
            e5.insert(END, str(row[0]) + ' ')
            """above statement gets rid of curly brackets in tuple output"""
    except IndexError:
        pass


    # mytuple=e5.get("1.0",END)
    # for row in mytuple:
    #     e5.insert(END, str(row[0]) + ',')
"""
Commands
"""
def wyswietl_command():
    list1.delete(0,END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0.0, END)
    for row in inner_backend3.wyswietl():
        list1.insert(END,row)


def test_command():
    list1.delete(0, END)
    for row in inner_backend3.test():
        list1.insert(END,row)

def szukaj_command():
    list1.delete(0,END)
    for row in inner_backend3.szukaj(e1.get(),e2.get(),e3.get(),e4.get()):
        list1.insert(END,row)


def dodaj_command():
    try:
        inner_backend3.dodaj(e1.get(),e2.get(),e3.get(),datetime.strptime(e4.get(), "%Y-%m-%d").date(),e5.get("1.0",END))
        list1.delete(0, END)
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0.0, END)
        for row in inner_backend3.wyswietl():
            list1.insert(END,row)
    except ValueError:
        messagebox.showerror("Błąd", "Sprawdz czy informacje sa podane w poprawnym formacie (szczegolnie Data Wizyty)")



def usun_command():
    inner_backend3.usun(selected_tuple[0])
    list1.delete(0, END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0.0,END)
    for row in inner_backend3.wyswietl():
        list1.insert(END,row)


def zmien_command():
    try:
        inner_backend3.zmien(selected_tuple[0],e1.get(),e2.get(),e3.get(),datetime.strptime(e4.get(), "%Y-%m-%d").date(),e5.get("1.0",END))
        # list1.delete(0, END)
        # for row in inner_backend3.wyswietl():
        #     list1.insert(END,row)
        messagebox.showinfo("Zmiana Danych", "Zmiany zostaly zapisane")

    except ValueError:
        messagebox.showerror("Błąd", "Sprawdz czy informacje sa podane w poprawnym formacie (szczegolnie Data Wizyty)")
        
def clear_command():
    list1.delete(0,END)
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0.0, END)

window=Tk()
window.title("Baza Danych Inner")
window.geometry("1140x490")



"""
Labels
"""
l1=Label(window,text=" Imie i Nazwisko:",font="arial 11")
l1.grid(row=0,column=0)
l2=Label(window,text=" Model Kotla:",font="arial 11")
l2.grid(row=0,column=3)
l3=Label(window,text=" Adres:",font="arial 11")
l3.grid(row=0,column=4)
l4=Label(window,text=" Data Wizyty(rrrr-mm-dd):",font="arial 11")
l4.grid(row=0,column=5)
l5=Label(window,text=" Historia:",font="arial 11")
l5.grid(row=2,column=7,columnspan=1)

"""
Entry Input
"""

e1=Entry(window,width=20,font="arial 11")
e1.grid(row=1,column=0,columnspan=3,padx=5, pady=5)
e2=Entry(window,width=20,font="arial 11")
e2.grid(row=1,column=3,padx=5, pady=5)
e3=Entry(window,width=40,font="arial 11")
e3.grid(row=1,column=4,padx=5, pady=5)
e4=Entry(window,width=15,font="arial 11")
e4.grid(row=1,column=5,padx=5, pady=5)
e5=Text(window,height=18,width=30,font="arial 11", pady=20)
e5.grid(row=2,column=7,rowspan=20,columnspan=8)



"""
Buttons
"""
b1=Button(window,text="Wyswietl Wszystkie", width=15,font="arial 12",command=wyswietl_command)
b1.grid(row=2,column=0, pady=10)
b2=Button(window,text="Szukaj", width=15,font="arial 12",command=szukaj_command)
b2.grid(row=3,column=0, pady=10)
b3=Button(window,text="Dodaj", width=15,font="arial 12",command=dodaj_command)
b3.grid(row=4,column=0, pady=10)
b4=Button(window,text="Usun", width=15,font="arial 12",command=usun_command)
b4.grid(row=5,column=0, pady=10)
b5=Button(window,text="Zmien", width=15,font="arial 12",command=zmien_command)
b5.grid(row=6,column=0, pady=10)
b6=Button(window,text="Wyczysc Liste", width=15,font="arial 12",command=clear_command)
b6.grid(row=7,column=0, pady=10)
b8=Button(window,text="Wyswietl Starsze", width=15,font="arial 12",command=test_command)
b8.grid(row=8,column=0, pady=10)
b7=Button(window,text="Zamknij", width=15,font="arial 12",command=window.destroy)
b7.grid(row=9,column=0, pady=10)

"""
List Box
"""
list1=Listbox(window, height=22,width=75,font="arial 12")
list1.grid(row=2,column=0,rowspan=15,columnspan=12,padx=5)

"""
Scrollbar
"""
sb1=Scrollbar(window)
sb1.grid(row=2,column=6,rowspan=10,sticky=N+S)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


sb2=Scrollbar(window)
sb2.grid(row=3,column=30,rowspan=6,sticky=N+S)
e5.configure(yscrollcommand=sb2.set)
sb2.configure(command=e5.yview)
"""
Bind Methods
"""
list1.bind('<<ListboxSelect>>', get_selected_row)
list1.bind('<Double-1>',click)




window.mainloop()



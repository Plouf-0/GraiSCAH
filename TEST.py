"""
from tkinter import *
from tkinter import ttk


def selectmode_none():
    tv['selectmode']="none"

def selectmode_browse():
    tv['selectmode']="browse"

def selectmode_extended():
    tv['selectmode']="extended"

ws = Tk()

tv = ttk.Treeview(
    ws, 
    columns=(1, 2, 3), 
    show='headings', 
    height=8
    )
tv.pack()

tv.heading(1, text='roll number')
tv.heading(2, text='name')
tv.heading(3, text='class')

tv.insert(parent='', index=0, iid=0, values=(21, "Krishna", 5))
tv.insert(parent='', index=1, iid=1, values=(18, "Bhem", 3))
tv.insert(parent='', index=2, iid=2, values=(12, "Golu", 6))
tv.insert(parent='', index=3, iid=3, values=(6, "Priya", 3))


b1 = Button(
    ws, 
    text="Browse",
    pady=20,
    command=selectmode_browse
    )
b1.pack(side=LEFT, fill=X, expand=True)


b2 = Button(
    ws, 
    text="None",
    pady=20,
    command=selectmode_none
    )
b2.pack(side=LEFT, fill=X, expand=True)


b3 = Button(
    ws, 
    text="Extended",
    pady=20,
    command=selectmode_extended
    )
b3.pack(side=LEFT, fill=X, expand=True)

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

ws.mainloop()
"""
"""
from tkinter import *
from tkinter import ttk

ws = Tk()
ws.title("PythonGuides")


frame = Frame(ws)
frame.pack(pady=20)

tv = ttk.Treeview(frame, columns=(1, 2, 3), show='headings', height=8)
tv.pack(side=LEFT)

tv.heading(1, text="name")
tv.heading(2, text="eid")
tv.heading(3, text="Salary")

sb = Scrollbar(frame, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)

tv.config(yscrollcommand=sb.set)
sb.config(command=tv.yview)


def update_item():
    selected = tv.focus()
    temp = tv.item(selected, 'values')
    sal_up = float(temp[2]) + float(temp[2]) * 0.05
    tv.item(selected, values=(temp[0], temp[1], sal_up))
    print(temp)

tv.insert(parent='', index=0, iid=0, values=("vineet", "e11", 1000000.00))
tv.insert(parent='', index=1, iid=1, values=("anil", "e12", 120000.00))
tv.insert(parent='', index=2, iid=2, values=("ankit", "e13", 41000.00))
tv.insert(parent='', index=3, iid=3, values=("Shanti", "e14", 22000.00))
tv.insert(parent='', index=4, iid=4, values=("vineet", "e11", 1000000.00))
tv.insert(parent='', index=5, iid=5, values=("anil", "e12", 120000.00))
tv.insert(parent='', index=6, iid=6, values=("ankit", "e13", 41000.00))
tv.insert(parent='', index=7, iid=7, values=("Shanti", "e14", 22000.00))
tv.insert(parent='', index=8, iid=8, values=("vineet", "e11", 1000000.00))
tv.insert(parent='', index=9, iid=9, values=("anil", "e12", 120000.00))
tv.insert(parent='', index=10, iid=10, values=("ankit", "e13", 41000.00))
tv.insert(parent='', index=11, iid=11, values=("Shanti", "e14", 22000.00))

Button(
    ws, 
    text='Increment Salary', 
    command=update_item, 
    padx=20, 
    pady=10, 
    bg='#081947', 
    foreground='#fff', 
    font=('Times BOLD', 12)
    ).pack(pady=10)

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

ws.mainloop()
"""









'''

import tkinter as tk
 
# fenêtre principale
w = tk.Tk()
 
# le tableau à afficher : [0, 0, 0, 0, 0]
tableau = [0 for i in range(5)]
 
# les 2 couleurs à utiliser
couleurs = {0: "white", 1: "blue"}
 
# dimensions du canevas
can_width = 250
can_height = 50
 
# taille d'une "case"
size = 50
 
# création canevas
can = tk.Canvas(w, width=can_width, height=can_height)
can.grid()
 
def afficher(t):
    """
    Fonction d'affichage du tableau ; 1 élément = 1 case
    La couleur de la "case" dépend de l'état de l'élement correspondant, 0 ou 1
    """
    for i in range(len(t)):
        can.create_rectangle(i * size,
                             0,
                             i * size + size,
                             size,
                             fill = couleurs[tableau[i]])
 
def modifierTableau(evt):
    """
    Fonction appelée lors d'un clic gauche sur le canevas
    Déterminer la correspondance entre la position horizontale
    de la souris et l'élément correspondant du tableau :
    evt.x est la position en x de la souris
    Pour simplifier j'ai pris un tableau à une dimension ;
    si on utilise un tableau 2d (échecs, dames, tic tac toe, etc)
    il faudra s'occuper aussi de evt.y ... """
    pos_x = int(evt.x / size)
 
    # inverser la valeur de l'élément cliqué
    if tableau[pos_x] == 0:
        tableau[pos_x] = 1
    else:
        tableau[pos_x] = 0
 
    # ré-afficher le tableau
    afficher(tableau)
 
#-----------------------------------------------------
# programme
afficher(tableau)
# binding de la fonction modifierTableau sur le canevas
can.bind("<Button-1>", modifierTableau)
# boucle principale
w.mainloop()
'''


"""
import tkinter as tk
 
 
class Master(tk.Frame):
    
 
    def __init__(self, master):
 
        tk.Frame.__init__(self, master)
 
        self.text_entry = tk.Entry(master, width=30)
         
         
        #packages here
        self.text_entry.pack()
 
        self.master.bind("<Return>", self.get_entry)
 
    def get_entry(self, event):
        v = self.text_entry.get()
        print(v)
 
#sortie de la classe
 
 
def test():
    root= tk.Tk()
    master=Master(root)
    root.mainloop()
 
 
 
if __name__ == '__main__':
    test()
"""
"""import time



for i in range(10):
    print(i)
    time.sleep(3)"""
"""
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')


def month_changed(event):
    msg = f'You selected {month_cb.get()}!'
    showinfo(title='Result', message=msg)


# month of year
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

label = ttk.Label(text="Please select a month:")
label.pack(fill='x', padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()

month_cb = ttk.Combobox(root, textvariable=selected_month)
month_cb['values'] = months
month_cb['state'] = 'readonly'  # normal
month_cb.pack(fill='x', padx=5, pady=5)

month_cb.bind('<<ComboboxSelected>>', month_changed)

root.mainloop()"""
"""
s = ('24', 'popoticarré', 'vert foncé', '32', 'Carottes', '7', '2021', 'en juin', 'pas mal en soupe')
#tomates
v = [(0, 'tomates'), (1, 'Carottes')]

#print(s[4])
#print(v.get("Carottes"))
def findi(l, a):
    for i in range(len(l)):
        if l[i][1] == a:
            return i
print(findi(v, 'tomates'))
"""
"""
import tkinter as tk
from tkinter import ttk
 
app = tk.Tk() 
app.geometry('200x100')

labelTop = tk.Label(app,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(app, 
                            values=[
                                    "January", 
                                    "February",
                                    "March",
                                    "April"])
#print(dict(comboExample)) 
comboExample.grid(column=0, row=1)
comboExample.current(2)

#print(comboExample.current(), comboExample.get())

app.mainloop()
"""
"""import tkinter as tk
#from _cffi_backend import callback
 
def callBackFunc():
    print("Oh. I'm clicked")

    print(chkValue.get())
    
app = tk.Tk() 
app.geometry('150x100')

chkValue = tk.BooleanVar() 
chkValue.set(True)
 
chkExample = tk.Checkbutton(app, text='Check Box', command=callBackFunc, var = chkValue) 
chkExample.grid(column=0, row=0)

app.mainloop()"""

"""import tkinter as tk
 
app = tk.Tk() 
app.geometry('150x100')

chkValue = tk.BooleanVar() 
chkValue.set(True)
 
chkExample = tk.Checkbutton(app, text='Check Box', var=chkValue) 
chkExample.grid(column=0, row=0)


#print("The checkbutton original value is {}").format(chkValue.get())
#chkExample.toggle()
#print("The checkbutton value after toggled is {}").format(chkValue.get())
#chkExample.toggle()
#print("The checkbutton value after toggled twice is {}").format(chkValue.get())

app.mainloop()"""


import tkinter as tk
from tkinter import ttk

#from tkcalendar import Calendar, DateEntry

"""def example1():
    def print_sel():
        print(cal.selection_get())

    top = tk.Toplevel(root)

    cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                   cursor="hand1", year=2018, month=2, day=5)

    cal.pack(fill="both", expand=True)
    ttk.Button(top, text="ok", command=print_sel).pack()


def example2():

    top = tk.Toplevel(root)

    cal = Calendar(top, selectmode='none')
    date = cal.datetime.today() + cal.timedelta(days=2)
    cal.calevent_create(date, 'Hello World', 'message')
    cal.calevent_create(date, 'Reminder 2', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=-2), 'Reminder 1', 'reminder')
    cal.calevent_create(date + cal.timedelta(days=3), 'Message', 'message')

    cal.tag_config('reminder', background='red', foreground='yellow')

    cal.pack(fill="both", expand=True)
    ttk.Label(top, text="Hover over the events.").pack()


def example3():
    top = tk.Toplevel(root)

    ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2, year=2010)
    cal.pack(padx=10, pady=10)


root = tk.Tk()
ttk.Button(root, text='Calendar', command=example1).pack(padx=10, pady=10)
ttk.Button(root, text='Calendar with events', command=example2).pack(padx=10, pady=10)
ttk.Button(root, text='DateEntry', command=example3).pack(padx=10, pady=10)

root.mainloop()"""

"""try:
    from tkinter import *
    from tkinter import ttk
except ImportError:
    from Tkinter import *
    import ttk

def treeview_sort_column(tv, col, reverse):
    print(col)
    l = [(tv.set(k, col), k) for k in tv.get_children('')]
    print(l)
    l.sort(key=lambda t: int(t[0]), reverse=reverse)

    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)

    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))
               

root = Tk()
columns = ('number', 'bleu')
treeview = ttk.Treeview(root, columns=columns, show='headings')
for t in ('1', '10', '11', '2', '3'):
    treeview.insert('', END, values=(t,))
treeview.pack()
for col in columns:
    print(col)
    treeview.heading(col, text=col, command=lambda c=col: treeview_sort_column(treeview, c, False))

mainloop()"""

a = ['poti', 'popotirond', 'popoticarré', 'popoticarré', 'popoticarré', 'la courgette de teste', 'fghj', 'Name', '', '']

b = sorted(a , key= lambda word: word.lower(),reverse = False)
#print(b)

normal = ['', '', 'fghj', 'la courgette de teste', 'Name', 'popoticarré', 'popoticarré', 'popoticarré', 'popotirond', 'poti']
inverse = ['poti', 'popotirond', 'popoticarré', 'popoticarré', 'popoticarré', 'Name', 'la courgette de teste', 'fghj', '', '']

def upperf(w):       
    return w.replace(w[0], w[0].upper())

print(upperf(("bleu")))

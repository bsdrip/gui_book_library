from tkinter import *

from backend import Database

be = Database("books.db")


def get_selected_row(event):
  try:
    global selected_tuple
    index = l_box.curselection()[0]
    selected_tuple = l_box.get(index)
    title_e.delete(0,END)
    title_e.insert(END,selected_tuple[1])
    author_e.delete(0,END)
    author_e.insert(END,selected_tuple[2])
    year_e.delete(0,END)
    year_e.insert(END,selected_tuple[3])
    isbn_e.delete(0,END)
    isbn_e.insert(END,selected_tuple[4])
  except IndexError:
    pass

def view_command():
  l_box.delete(0,END)
  for row in be.db_view():
    l_box.insert(END,row)

def search_command():
  l_box.delete(0,END)
  for row in be.book_search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
    l_box.insert(END,row)

def add_command():
  be.book_insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
  l_box.delete(0,END)
  l_box.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
  index = selected_tuple[0]
  be.book_delete(index)

def update_command():
  row = selected_tuple
  be.db_update(row[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


#----------------------------------------------------------------------


window = Tk()
window.resizable(False, False)
window.title("Library")

title_l = Label(window,text="Title")
title_l.grid(row=0,column=0)

author_l = Label(window,text="Author")
author_l.grid(row=0,column=2)

year_l = Label(window,text="Year")
year_l.grid(row=1,column=0)

isbn_l = Label(window,text="ISBN")
isbn_l.grid(row=1,column=2)


#----------------------------------------------------------------------


title_text = StringVar()
title_e = Entry(window, textvariable=title_text)
title_e.grid(row=0,column=1)

author_text = StringVar()
author_e = Entry(window, textvariable=author_text)
author_e.grid(row=0,column=3)

year_text = StringVar()
year_e = Entry(window, textvariable=year_text)
year_e.grid(row=1,column=1)

isbn_text = StringVar()
isbn_e = Entry(window, textvariable=isbn_text)
isbn_e.grid(row=1,column=3)


#----------------------------------------------------------------------


l_box = Listbox(window,height=6,width=35)
l_box.grid(row=2,column=0,rowspan=6,columnspan=2)

s_bar = Scrollbar(window)
s_bar.grid(row=2,column=2,rowspan=6)

l_box.configure(yscrollcommand=s_bar.set)
s_bar.configure(command=l_box.yview)

l_box.bind("<<ListboxSelect>>",get_selected_row)


#----------------------------------------------------------------------


view_all_b = Button(window,text="VIEW ALL",width=12,command=view_command)
view_all_b.grid(row=2,column=3)

search_entry_b = Button(window,text="SEARCH ENTRY",width=12,command=search_command)
search_entry_b.grid(row=3,column=3)

add_entry_b = Button(window,text="ADD ENTRY",width=12,command=add_command)
add_entry_b.grid(row=4,column=3)

update_b = Button(window,text="UPDATE",width=12,command=update_command)
update_b.grid(row=5,column=3)

delete_b = Button(window,text="DELETE",width=12,command=delete_command)
delete_b.grid(row=6,column=3)

close_b = Button(window,text="CLOSE",width=12,command=window.destroy)
close_b.grid(row=7,column=3)



window.mainloop()

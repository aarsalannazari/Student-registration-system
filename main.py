from tkinter import *
from Data_Base_function import *

window=Tk() # Create instance

# Labels 
name_label=Label(window,text='name:')
name_label.grid(row=0,column=0,padx=5,pady=5)

familly_label=Label(window,text='familly name:')
familly_label.grid(row=0,column=2,padx=5,pady=5)

student_id_label=Label(window,text='student id:')
student_id_label.grid(row=1,column=0,padx=5,pady=5)

age_label=Label(window,text='age:')
age_label.grid(row=1,column=2,padx=5,pady=5)

# Entries

name_entry=Entry(window)
name_entry.grid(row=0,column=1)

familly_entry=Entry(window)
familly_entry.grid(row=0,column=3)

id_entry=Entry(window)
id_entry.grid(row=1,column=1)

age_entry=Entry(window)
age_entry.grid(row=1,column=3)

search_entry=Entry(window)
search_entry.grid(row=4,column=3)

# Buttons

add_button=Button(window,text='add',font=('arial',12,'bold'),bd=2,activeforeground='white',activebackground='black',bg='white',fg='black')
add_button.grid(row=3,column=0,padx=5,pady=5)

edit_button=Button(window,text='edit',font=('arial',12,'bold'),bd=2,activeforeground='white',activebackground='black',bg='white',fg='black')
edit_button.grid(row=3,column=1,padx=5,pady=5)

delete_button=Button(window,text='delete',font=('arial',12,'bold'),bd=2,activeforeground='white',activebackground='black',bg='white',fg='black')
delete_button.grid(row=3,column=2,padx=5,pady=5)

show_button=Button(window,text='show all',font=('arial',12,'bold'),bd=2,activeforeground='white',activebackground='black',bg='white',fg='black')
show_button.grid(row=3,column=3,padx=5,pady=5)

search_button=Button(window,text='search',bd=2,font=('arial',14,'bold'),bg='powder blue',activebackground='powder blue')
search_button.grid(row=4,column=2,padx=5,pady=5)


# Listbox

listbox=Listbox(window,width=35,height=30)
listbox.grid(row=4,column=1,rowspan=1,columnspan=1)

# Scrollbar

scrollbar=Scrollbar(window)
scrollbar.grid(row=4,column=0)

# Settings
window.title('Student Registration System')
window.geometry('700x700')
window.resizable(width=False,height=False)
listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

# Run

window.mainloop()

# I Continue this program for tomorrow

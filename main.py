from tkinter import *
from tkinter import messagebox
from Data_Base_function import *

# Create instance

window=Tk()

#Functions

def get_sellected(self):
    global select
    try:i=listbox.curselection()[0]
    except IndexError:pass
    select=listbox.get(i)
    name_entry.delete(0,END)
    name_entry.insert(0,select[1])

    familly_entry.delete(0,END)
    familly_entry.insert(0,select[2])

    student_id_entry.delete(0,END)
    student_id_entry.insert(0,select[3])

    age_entry.delete(0,END)
    age_entry.insert(0,select[4])

    return select


def Insert_student(name,familly,st_id,age):
    res=Insert(name,familly,st_id,age)
    if res != False:
        name_entry.delete(0,END)
        familly_entry.delete(0,END)
        student_id_entry.delete(0,END)
        age_entry.delete(0,END)
        messagebox.showinfo('Registration confirmation','The new student was successfully registered')
        Show_students()
    else:
        messagebox.showerror('Error','This student number has already been registered!')

def Show_students():
    res=Show()
    if res != False:
        listbox.delete(0,END)
        for i in res:
            listbox.insert(0,i)
    else:
        messagebox.showerror('Error','An error occurred while retrieving data!')

def Delete_student():
    id=select[3]
    res=Delete(id)
    if res != False:
        name_entry.delete(0,END)
        familly_entry.delete(0,END)
        student_id_entry.delete(0,END)
        age_entry.delete(0,END)
        messagebox.showinfo('Confirm deletion','Student information has been successfully deleted')
        Show_students()
    else:
        messagebox.showerror('Error','An error occurred while deleting information!')

def Search_student(id,name,familly,age):
    res=Search(id,name,familly,age)
    if res != False:
        listbox.delete(0,END)
        for i in res:
            listbox.insert(0,i)
    else:
        messagebox.showerror('Error','An error occurred while retrieving data!')

def Update_student(name,familly,student_id,age):
    id=select[0]
    res=Update(name,familly,student_id,age,id)
    if res != False:
        messagebox.showinfo('Update confirmation','The update was completed successfully')
        name_entry.delete(0,END)
        familly_entry.delete(0,END)
        student_id_entry.delete(0,END)
        age_entry.delete(0,END)
        Show_students()
    else:
        messagebox.showerror('Error','An error occurred in the update!')


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

student_id_entry=Entry(window)
student_id_entry.grid(row=1,column=1)

age_entry=Entry(window)
age_entry.grid(row=1,column=3)

search_entry=Entry(window)
search_entry.grid(row=4,column=3)

# Buttons

add_button=Button(window,text='add',command=lambda:Insert_student(name_entry.get(),familly_entry.get(), student_id_entry.get(),age_entry.get()),font=('arial',12,'bold'),bd=2,activeforeground='white',activebackground='black',bg='white',fg='black')
add_button.grid(row=3,column=0,padx=5,pady=5)

edit_button=Button(window,text='edit',command=lambda:Update_student(name_entry.get(),familly_entry.get(),student_id_entry.get(),age_entry.get()),font=('arial',12,'bold'),bd=2,activeforeground='white',activebackground='black',bg='white',fg='black')
edit_button.grid(row=3,column=1,padx=5,pady=5)

delete_button=Button(window,text='delete',command=lambda:Delete_student(),font=('arial',12,'bold'),bd=2,activeforeground='white',activebackground='black',bg='white',fg='black')
delete_button.grid(row=3,column=2,padx=5,pady=5)

show_button=Button(window,text='show all',command=lambda:Show_students(),font=('arial',12,'bold'),bd=2,activeforeground='white',activebackground='black',bg='white',fg='black')
show_button.grid(row=3,column=3,padx=5,pady=5)

search_button=Button(window,text='search',bd=2,command=lambda:Search_student(id=search_entry.get(),name=search_entry.get(),familly=search_entry.get(),age=search_entry.get()),font=('arial',14,'bold'),bg='powder blue',activebackground='powder blue')
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
listbox.bind('<<ListboxSelect>>',get_sellected)

# Run

window.mainloop()

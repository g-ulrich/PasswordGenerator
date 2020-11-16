from tkinter import *
import datetime as dt
import random
import os
import json

def insert_substr(string,insert, index):
    return string[:index] + insert + string[index:]

def read_from_history():
    f = open("password_history.txt", "r")
    return f.readlines()

def write_to_history(stamp):
    f = open("password_history.txt", "a")
    f.write(str(stamp) + "\n")
    f.close()

def str_list_to_list(string):
    return string.strip('][').split(', ')




def password():
    lower = ["a", "b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upper = [i.upper() for i in lower]
    num = [str(i) for i in range(10)]
    char = ["!" "?", ".", "%", "$", "#", "&", "*", "^"]
    all = lower + upper + num
    try:
        x = int(length.get())
    except:
        x = 10
    password = ""
    for i in range(int((x - (len(append.get())+ len(insert.get())) if append.get() != "" or insert.get() != "" else x)//2)):
        password += random.choice(all)
        password += random.choice(char)
        
    if insert.get() != "":
        password += insert_substr(password, insert.get(), random.choice([i for i in range(len(password))]))
    if append.get() != "":
        password += append.get()
    
    if len(password) != x:
        if len(password) > x:
            keep = len(password) - (len(password) - x)
            password = password[-keep:]
        else:
            add = x - len(password)
            password = password
            for z in range(add):
                password += random.choice(all + char)
                
    
    stamp = {"generated": str(dt.datetime.now())[:19],
             "title": title.get(), "append":append.get(),
             "insert":insert.get(),
             "initial_length": length.get(),
             "total_length":len(password),
             "password": password}
    write_to_history(stamp)
    view_window(stamp['generated'], stamp['title'], stamp['append'], stamp['insert'], stamp['password'])

def quit_all():
    quit()

def history_window(message=""):
    
    history = Tk()
    history.title("Secure Password History")
    v = Scrollbar(history) 
    v.pack(side = RIGHT, fill = Y) 
    t = Text(history, width = 80, height = 20, wrap = NONE, yscrollcommand = v.set) 
    li = [json.loads(i.replace("'", '"')) for i in read_from_history()]
    li.reverse()
    
    
            

    if message == "" or len(li) > 0:
        for i, v in enumerate(li, 0):
            t.insert(END, "[Generated: " + v['generated'] + "] [Title: " + v['title'] + "] [Password: " + v['password'] + "]\n")
    else:
        # Label(history, text=message, font="none 15").grid(row=2, column=1)
        t.insert(END, message)

        
    t.pack(side=TOP, fill=X)
    v.config(command=t.yview) 
   
    
def copy_password_to_clipboard(password):
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(password)
    r.update()
    r.destroy()

def view_window(generated, reason, append, insert, password):
    
    Label(root, text="___________", font="none 15").grid(row=6, column=0)
    Label(root, text="__________________", font="none 15").grid(row=6, column=1)
    Label(root, text="_____", font="none 15").grid(row=6, column=2)
    
    
    Label(root, text="Generated  ", font="none 15").grid(row=7, column=0)
    Label(root, text="Title            ", font="none 15").grid(row=8, column=0)
    Label(root, text="Appended   ", font="none 15").grid(row=9, column=0)
    Label(root, text="Inserted      ", font="none 15").grid(row=10, column=0)
    Label(root, text="Length        ", font="none 15").grid(row=11, column=0)
    Label(root, text="Password   ", font="none 15").grid(row=12, column=0)
    
    Label(root, text=generated, font="none 15").grid(row=7, column=1)
    Label(root, text=reason, font="none 15").grid(row=8, column=1)
    Label(root, text=append, font="none 15").grid(row=9, column=1)
    Label(root, text=insert, font="none 15").grid(row=10, column=1)
    Label(root, text=len(password), font="none 15").grid(row=11, column=1)
    pw = Entry(root, font="none 15")
    pw.insert(0,password)
    pw.grid(row=12, column=1)
    def destroy_app():
        root.destroy()
        
    Button(root, text='Quit', 
            command=destroy_app, font="none 15").grid(row=13, 
                                            column=0, 
                                            sticky=W, 
                                            padx=5)
    Button(root, text='View Password History', 
            command=history_window, font="none 15").grid(row=13, 
                                            column=1, 
                                            sticky=W, 
                                            pady=6)
    Button(root, text='Copy', 
            command=lambda: copy_password_to_clipboard(password), font="none 15").grid(row=12, 
                                            column=2, 
                                            sticky=W, 
                                            padx=5)
    # Label(root, text="With Love by Gabe :)", font="none 6").grid(row=13, column=2)
    
    # def destroy_app():
    #     history.destroy()
    # Button(history, text='Quit', 
    #         command=destroy_app, font="none 15").grid(row=1, 
    #                                         column=1, 
    #                                         sticky=W, 
    #                                         padx=5,
    #                                         pady=5)
    def clear_history():
        f = open("password_history.txt", "w")
        f.write("")
        f.close()
        history_window("History Erased! :)")
        
    
    Button(root, text='Erase History', 
            command=clear_history, font="none 7").grid(row=13, 
                                            column=2, 
                                            sticky=W, 
                                            padx=2,
                                            pady=5)
    mainloop()
    
    
if __name__ == "__main__": 
    
    root = Tk()
    root.title("Secure Password Generator")
    Label(root, text="With Love by Gabe :)", font="none 7 bold").grid(row=1, column=0)
    Label(root, text=str(dt.datetime.now())[:19], font="none 12 bold").grid(row=1, column=1)
    Label(root, text="Title            ", font="none 15").grid(row=2)
    Label(root, text="Append       ", font="none 15").grid(row=3)
    Label(root, text="Insert          ", font="none 15").grid(row=4)
    Label(root, text=" Length ", font="none 8").grid(row=1, column=2)
    
    length = Entry(root, width=3, font="none 15")
    length.insert(0,"15")
    length.grid(row=2, column=2)
    
    title = Entry(root, font="none 15")
    title.grid(row=2, column=1)
    
    append = Entry(root, font="none 15")
    append.grid(row=3, column=1)
    
    insert = Entry(root, font="none 15")
    insert.grid(row=4, column=1)
    
    # photo = PhotoImage(file = r"package/lock.png") 
    # photoimage = photo.subsample(10, 10)
    Button(root, text='Generate Password', 
            command=password, font="none 15").grid(row=5, 
                                            column=1, 
                                            sticky=W, 
                                            pady=6) 
    mainloop()
from funcs import Database
from tkinter import *
from tkinter import messagebox

if __name__ == "__main__":
    root = Tk()
    root.title("ZPassword Manager")
    root.iconbitmap('c:/Temp/pc.ico')
    root.geometry("700x360")

    db = Database('content.db')

    def clear_all():
        site_entry.delete(0,END)
        url_entry.delete(0,END)
        email_entry.delete(0,END)
        username_entry.delete(0,END)
        password_entry.delete(0,END)
        notes_entry.delete(0,END)
        global selected_site
        selected_site = None

    # Shows all records
    def show_all():
        site_list.delete(0, END)
        for r in  db.s_all():
            site_list.insert(END, r)

    # Add record to table - Button 1
    def add_site():
        if site_entry.get() == '' or url_entry.get() == '' or email_entry.get() == '' \
            or username_entry.get() == '' or password_entry.get() == '':
                messagebox.showerror("Required Fields", " Please include all fields")
                return
        db.a_site(site_entry.get(), url_entry.get(), email_entry.get(), username_entry.get(), password_entry.get(), notes_entry.get())
        site_list.delete(0, END)
        show_all()
        clear_all()

    # Delete record from table - Button 4
    def select_site(even):
        try:
            global selected_site
            index = site_list.curselection()[0]
            selected_site = site_list.get(index)
            site_entry.delete(0, END)
            site_entry.insert(END, selected_site[1])
            url_entry.delete(0, END)
            url_entry.insert(END, selected_site[2])
            email_entry.delete(0, END)
            email_entry.insert(END, selected_site[3])
            username_entry.delete(0, END)
            username_entry.insert(END, selected_site[4])
            password_entry.delete(0, END)
            password_entry.insert(END, selected_site[5])
            notes_entry.delete(0, END)
            notes_entry.insert(END, selected_site[6])
        except IndexError:
            pass

    def delete_rec():
        try:
            db.d_site(selected_site[0])
            show_all()
            clear_all()
        except:
            pass
    
    # Update Record -  Button 3
    def update_rec():
        db.u_site(selected_site[0], site_entry.get(), url_entry.get(), email_entry.get(), username_entry.get(), password_entry.get(), notes_entry.get())
        site_list.delete(0, END)
        show_all()

    # Create Labels, Textboxes and Scrollbar
    site_text = StringVar()
    site_label = Label(root, text="Site Name", font=('bold', 10), pady=10, padx=10)
    site_label.grid(row=0, column=0, sticky=W)
    site_entry = Entry(root, textvariable=site_text, width=35)
    site_entry.grid(row=0, column=1)

    url_text = StringVar()
    url_label = Label(root, text="Site URL", font=('bold', 10), padx=10)
    url_label.grid(row=0, column=2, sticky=W)
    url_entry = Entry(root, textvariable=url_text, width=45)
    url_entry.grid(row=0, column=3)
    
    email_text = StringVar()
    email_label = Label(root, text="Email", font=('bold', 10), padx=10)
    email_label.grid(row=1, column=0, sticky=W)
    email_entry = Entry(root, textvariable=email_text, width=35)
    email_entry.grid(row=1, column=1)

    username_text = StringVar()
    username_label = Label(root, text="Username", font=('bold', 10), padx=10)
    username_label.grid(row=1, column=2, sticky=W)
    username_entry = Entry(root, textvariable=username_text, width=45)
    username_entry.grid(row=1, column=3)

    password_text = StringVar()
    password_label = Label(root, text="Password", font=('bold', 10),pady=10, padx=10)
    password_label.grid(row=2, column=0, sticky=W)
    password_entry = Entry(root, textvariable=password_text, width=35)
    password_entry.grid(row=2, column=1)

    notes_text = StringVar()
    notes_label = Label(root, text="Notes", font=('bold', 10), padx=10)
    notes_label.grid(row=3, column=0, sticky=W)
    notes_entry = Entry(root, textvariable=notes_text, width=96)
    notes_entry.grid(row=3, column=1, pady=(0,10), columnspan=3)

    site_list = Listbox(root, height=10, width=90, border=1)
    site_list.grid(row=5, column=0, columnspan=4, rowspan=6, pady=10, padx=5, sticky="nesw")
    scrollbar = Scrollbar(root)
    scrollbar.grid(row=5, column=4,rowspan=6, sticky="ns")
    site_list.configure(yscrollcommand=scrollbar.set)
    scrollbar.configure(command=site_list.yview)
    site_list.bind('<<ListboxSelect>>', select_site)

    # Create Buttons
    center = Frame(root, bg='gray', width=700)
    center.grid(row=4, columnspan=5, sticky="nsew")

    add_btn = Button(root, text="Add Site", width=10, command=add_site)
    add_btn.grid(row=4, column=0, pady=10, padx=(10,10))
    #search_btn = Button(root, text="Show All", width=10, command=show_all)
    #search_btn.grid(row=4, column=1)
    show_btn = Button(root, text="Clear Text", width=10, command=clear_all)
    show_btn.grid(row=4, column=1,padx=5, sticky=W)
    update_btn = Button(root, text="Update Site", width=10, command=update_rec)
    update_btn.grid(row=4, column=3)
    delete_btn = Button(root, text="Delete Site", width=10, command=delete_rec)
    delete_btn.grid(row=4, column=3, sticky=E)


    show_all()
    root.mainloop()
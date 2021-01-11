# imports
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter import messagebox as ms

# Database for Account_Registers
with sqlite3.connect('accounts.db') as db:
    c = db.cursor()
c.execute('CREATE TABLE IF NOT EXISTS `admin_member` (admin_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'
          ', username TEXT NOT NULL, password TEXT NOT NULL, email TEXT NOT NULL, department TEXT NOT NULL, '
          'position TEXT NOT NULL);')
db.commit()
db.close()


# Main Class
class AdminMain:
    def __init__(self, master):
        self.master = master
        self.username = StringVar()
        self.password = StringVar()
        self.n_username = StringVar()
        self.n_password = StringVar()
        self.widgets()

    def contact_admin(self):
                    tkMessageBox.showinfo('Help', 'Contact to Head Admin: ssmosam22@gmail.com ', icon="info")

    # Login Function
    def login(self):
        # Establish Connection
        with sqlite3.connect('accounts.db') as db:
            c = db.cursor()
        find_user = 'SELECT * FROM admin_member WHERE username = ? and password = ?'
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchall()
        if result:
            # Opening Window (GitHub @RealMosam)
            root_cms = Tk()
            root_cms.title("Contacts Management System")
            p2 = PhotoImage(file="cms_icon.png", master=root_cms)
            root_cms.iconphoto(0,p2)
            width = 750
            height = 400
            screen_width = root_cms.winfo_screenwidth()
            screen_height = root_cms.winfo_screenheight()
            x = (screen_width / 2) - (width / 2)
            y = (screen_height / 2) - (height / 2)
            root_cms.geometry("%dx%d+%d+%d" % (width, height, x, y))
            root_cms.resizable(0, 0)
            root_cms.config(bg="#ffffff")

            # VARIABLES
            FIRSTNAME = StringVar()
            LASTNAME = StringVar()
            GENDER = StringVar()
            AGE = StringVar()
            ADDRESS = StringVar()
            CONTACT = StringVar()
            REMINDER = StringVar()

            # METHODS
            def Admin_Manager():

                root_cms_admin_manager = Tk()
                root_cms_admin_manager.title("Contacts Management System")
                p1 = PhotoImage(file="admin_icon.png", master=root_cms_admin_manager)
                root_cms_admin_manager.iconphoto(0, p1)
                width = 700
                height = 400
                screen_width = root_cms_admin_manager.winfo_screenwidth()
                screen_height = root_cms_admin_manager.winfo_screenheight()
                x = (screen_width / 2) - (width / 2)
                y = (screen_height / 2) - (height / 2)
                root_cms_admin_manager.geometry("%dx%d+%d+%d" % (width, height, x, y))
                root_cms_admin_manager.resizable(0, 0)
                root_cms_admin_manager.config(bg="#ffffff")

                ADMIN_USERNAME = StringVar()
                ADMIN_PASSWORD = StringVar()
                ADMIN_EMAIL = StringVar()
                ADMIN_DEPARTMENT = StringVar()
                ADMIN_POSITION = StringVar()

                def Admin_Database():
                    conn = sqlite3.connect("accounts.db")
                    cursor = conn.cursor()
                    cursor.execute(
                        "CREATE TABLE IF NOT EXISTS `admin_member` (admin_id INTEGER NOT NULL  PRIMARY KEY "
                        "AUTOINCREMENT, "
                        "username TEXT NOT NULL, "
                        "password TEXT NOT NULL, "
                        "email TEXT NOT NULL, "
                        "department TEXT NOT NULL, "
                        "position TEXT NOT NULL)")
                    cursor.execute("SELECT * FROM `admin_member` ORDER BY `username` ASC")
                    fetch = cursor.fetchall()
                    for data in fetch:
                        tree.insert('', 'end', values=(data))
                    cursor.close()
                    conn.close()

                def Admin_SubmitData():
                    if ADMIN_USERNAME.get() == "" or ADMIN_PASSWORD.get() == "" or ADMIN_EMAIL.get() == "" or \
                            ADMIN_DEPARTMENT.get() == "" or ADMIN_POSITION.get() == "":
                        result = tkMessageBox.showwarning('Oops!', 'Please Complete The Required Fields',
                                                          icon="warning")
                    else:
                        tree.delete(*tree.get_children())
                        conn = sqlite3.connect("accounts.db")
                        cursor = conn.cursor()
                        cursor.execute(
                            "INSERT INTO `admin_member` (username, password, email, department, position) VALUES(?, "
                            "?, ?, ?, ?)", (str(ADMIN_USERNAME.get()), str(ADMIN_PASSWORD.get()),
                                            str(ADMIN_EMAIL.get()),
                                            str(ADMIN_DEPARTMENT.get()), str(ADMIN_POSITION.get())))
                        conn.commit()
                        cursor.execute("SELECT * FROM `admin_member` ORDER BY `username` ASC")
                        fetch = cursor.fetchall()
                        for data in fetch:
                            tree.insert('', 'end', values=(data))
                        cursor.close()
                        conn.close()
                        ADMIN_USERNAME.set("")
                        ADMIN_PASSWORD.set("")
                        ADMIN_EMAIL.set("")
                        ADMIN_DEPARTMENT.set("")
                        ADMIN_POSITION.set("")
                        tkMessageBox.showwarning('Confirmation', 'Admin Added Successfully', icon="info")

                def Admin_UpdateData():
                    tree.delete(*tree.get_children())
                    conn = sqlite3.connect("accounts.db")
                    cursor = conn.cursor()
                    cursor.execute(
                        "UPDATE `admin_member` SET `username` = ?, `password` = ?, `email` = ?, `department` = ?, "
                        "`position` = ? WHERE `admin_id` = ?",
                        (str(ADMIN_USERNAME.get()), str(ADMIN_PASSWORD.get()), str(ADMIN_EMAIL.get()),
                         str(ADMIN_DEPARTMENT.get()), str(ADMIN_POSITION.get()), int(admin_id)))
                    conn.commit()
                    cursor.execute("SELECT * FROM `admin_member` ORDER BY `username` ASC")
                    fetch = cursor.fetchall()
                    for data in fetch:
                        tree.insert('', 'end', values=(data))
                    cursor.close()
                    conn.close()
                    ADMIN_USERNAME.set("")
                    ADMIN_PASSWORD.set("")
                    ADMIN_EMAIL.set("")
                    ADMIN_DEPARTMENT.set("")
                    ADMIN_POSITION.set("")
                    tkMessageBox.showwarning('Confirmation', 'Admin Information Updated Successfully', icon="info")

                def Admin_OnSelected(event):
                    global admin_id, Admin_UpdateWindow
                    curItem = tree.focus()
                    contents = (tree.item(curItem))
                    selecteditem = contents['values']
                    try:
                        admin_id = selecteditem[0]
                        ADMIN_USERNAME.set("")
                        ADMIN_PASSWORD.set("")
                        ADMIN_EMAIL.set("")
                        ADMIN_DEPARTMENT.set("")
                        ADMIN_POSITION.set("")
                        ADMIN_USERNAME.set(selecteditem[1])
                        ADMIN_PASSWORD.set(selecteditem[2])
                        ADMIN_EMAIL.set(selecteditem[3])
                        ADMIN_DEPARTMENT.set(selecteditem[4])
                        ADMIN_POSITION.set(selecteditem[5])
                        Admin_UpdateWindow = Toplevel()
                        try:
                            Admin_UpdateWindow.title("Contacts Management System")
                            p1 = PhotoImage(file="admin_icon.png", master=Admin_UpdateWindow)
                            Admin_UpdateWindow.iconphoto(0, p1)
                            width = 420
                            height = 260
                            screen_width = root.winfo_screenwidth()
                            screen_height = root.winfo_screenheight()
                            x = ((screen_width / 2) + 450) - (width / 2)
                            y = ((screen_height / 2) + 20) - (height / 2)
                            Admin_UpdateWindow.resizable(0, 0)
                            Admin_UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
                            if 'Admin_NewWindow' in globals():
                                Admin_NewWindow.destroy()

                            # FRAMES
                            FormTitle = Frame(Admin_UpdateWindow)
                            FormTitle.pack(side=TOP)
                            ContactForm = Frame(Admin_UpdateWindow)
                            ContactForm.pack(side=TOP, pady=10)

                            # LABELS
                            lbl_admin_title = Label(FormTitle, text="Updating Admins", font=('Times New Roman', 16),
                                                    bg="orange",
                                                    width=300)
                            lbl_admin_title.pack(fill=X)
                            lbl_username = Label(ContactForm, text="Username", font=('Times New Roman', 14), bd=5)
                            lbl_username.grid(row=0, sticky=W)
                            lbl_password = Label(ContactForm, text="Password", font=('Times New Roman', 14), bd=5)
                            lbl_password.grid(row=1, sticky=W)
                            lbl_email = Label(ContactForm, text="Email", font=('Times New Roman', 14), bd=5)
                            lbl_email.grid(row=2, sticky=W)
                            lbl_department = Label(ContactForm, text="Department", font=('Times New Roman', 14), bd=5)
                            lbl_department.grid(row=3, sticky=W)
                            lbl_position = Label(ContactForm, text="Position", font=('Times New Roman', 14), bd=5)
                            lbl_position.grid(row=4, sticky=W)

                            # ENTRY
                            username = Entry(ContactForm, textvariable=ADMIN_USERNAME, font=('Times New Roman', 14))
                            username.grid(row=0, column=1)
                            password = Entry(ContactForm, textvariable=ADMIN_PASSWORD, font=('Times New Roman', 14))
                            password.grid(row=1, column=1)
                            email = Entry(ContactForm, textvariable=ADMIN_EMAIL, font=('Times New Roman', 14))
                            email.grid(row=2, column=1)
                            department = Entry(ContactForm, textvariable=ADMIN_DEPARTMENT, font=('Times New Roman', 14))
                            department.grid(row=3, column=1)
                            position = Entry(ContactForm, textvariable=ADMIN_POSITION, font=('Times New Roman', 14))
                            position.grid(row=4, column=1)

                            # BUTTONS
                            btn_updatecon = Button(ContactForm, text="Update", width=50,
                                                   font=('Times New Roman', 10, 'bold'),
                                                   command=Admin_UpdateData)
                            btn_updatecon.grid(row=7, columnspan=2, pady=10)
                        except TclError:
                            tkMessageBox.showwarning('Oops!',
                                                     'Do not close the main Window!..Application will now Exit',
                                                     icon="warning")
                    except IndexError:
                        tkMessageBox.showwarning('Oops!', 'Please Select The Admin First!', icon="warning")

                def Admin_DeleteData():

                    if not tree.selection():
                        result = tkMessageBox.showwarning('Oops!', 'Please Select The Admin First!', icon="warning")
                    else:
                        result = tkMessageBox.askquestion('Confirm?',
                                                          'Are you sure you want to delete this record?',
                                                          icon="warning")
                        if result == 'yes':
                            curItem = tree.focus()
                            contents = (tree.item(curItem))
                            selecteditem = contents['values']
                            tree.delete(curItem)
                            conn = sqlite3.connect("accounts.db")
                            cursor = conn.cursor()
                            cursor.execute("DELETE FROM `admin_member` WHERE `admin_id` = %d" % selecteditem[0])
                            conn.commit()
                            cursor.close()
                            conn.close()
                            tkMessageBox.showwarning('Confirmation', 'Admin Deleted Successfully', icon="info")

                def Admin_AddNewWindow():
                    global Admin_NewWindow
                    ADMIN_USERNAME.set("")
                    ADMIN_PASSWORD.set("")
                    ADMIN_EMAIL.set("")
                    ADMIN_DEPARTMENT.set("")
                    ADMIN_POSITION.set("")
                    Admin_NewWindow = Toplevel()
                    p1 = PhotoImage(file="admin_icon.png", master=Admin_NewWindow)
                    Admin_NewWindow.iconphoto(0, p1)
                    Admin_NewWindow.title("Contacts Management System")
                    width = 420
                    height = 260
                    screen_width = root_cms_admin_manager.winfo_screenwidth()
                    screen_height = root_cms_admin_manager.winfo_screenheight()
                    x = ((screen_width / 2) - 455) - (width / 2)
                    y = ((screen_height / 2) + 20) - (height / 2)
                    Admin_NewWindow.resizable(0, 0)
                    Admin_NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
                    if 'Admin_UpdateWindow' in globals():
                        Admin_UpdateWindow.destroy()

                    # FRAMES
                    FormTitle = Frame(Admin_NewWindow)
                    FormTitle.pack(side=TOP)
                    ContactForm = Frame(Admin_NewWindow)
                    ContactForm.pack(side=TOP, pady=10)

                    # LABELS
                    lbl_admin_title = Label(FormTitle, text="Adding New Admin", font=('Times New Roman', 16),
                                            bg="#66ff66",
                                            width=300)
                    lbl_admin_title.pack(fill=X)
                    lbl_username = Label(ContactForm, text="Username", font=('Times New Roman', 14), bd=5)
                    lbl_username.grid(row=0, sticky=W)
                    lbl_password = Label(ContactForm, text="Password", font=('Times New Roman', 14), bd=5)
                    lbl_password.grid(row=1, sticky=W)
                    lbl_email = Label(ContactForm, text="Email", font=('Times New Roman', 14), bd=5)
                    lbl_email.grid(row=2, sticky=W)
                    lbl_department = Label(ContactForm, text="Department", font=('Times New Roman', 14), bd=5)
                    lbl_department.grid(row=3, sticky=W)
                    lbl_position = Label(ContactForm, text="Position", font=('Times New Roman', 14), bd=5)
                    lbl_position.grid(row=4, sticky=W)

                    # ENTRY
                    username = Entry(ContactForm, textvariable=ADMIN_USERNAME, font=('Times New Roman', 14))
                    username.grid(row=0, column=1)
                    password = Entry(ContactForm, textvariable=ADMIN_PASSWORD, font=('Times New Roman', 14))
                    password.grid(row=1, column=1)
                    email = Entry(ContactForm, textvariable=ADMIN_EMAIL, font=('Times New Roman', 14))
                    email.grid(row=2, column=1)
                    department = Entry(ContactForm, textvariable=ADMIN_DEPARTMENT, font=('Times New Roman', 14))
                    department.grid(row=3, column=1)
                    position = Entry(ContactForm, textvariable=ADMIN_POSITION, font=('Times New Roman', 14))
                    position.grid(row=4, column=1)

                    # BUTTONS
                    btn_addcon = Button(ContactForm, text="Save", width=50, font=('Times New Roman', 10, 'bold'),
                                        command=Admin_SubmitData)
                    btn_addcon.grid(row=7, columnspan=2, pady=10)

                Top = Frame(root_cms_admin_manager, width=500, bd=1, relief=SOLID)
                Top.pack(side=TOP)
                Mid = Frame(root_cms_admin_manager, width=500, bg="#ffffff")
                Mid.pack(side=TOP)
                MidLeft = Frame(Mid, width=100)
                MidLeft.pack(side=LEFT, pady=10)
                MidLeftPadding = Frame(Mid, width=370, bg="#ffffff")
                MidLeftPadding.pack(side=LEFT)
                MidRight = Frame(Mid, width=100)
                MidRight.pack(side=RIGHT, pady=10)
                TableMargin = Frame(root_cms_admin_manager, width=500)
                TableMargin.pack(side=TOP)

                # ADMIN LABELS
                lbl_admin_title = Label(Top, text="Contacts Management System", bg="#ffffff",
                                        font=('Times New Roman', 16),
                                        width=500)
                lbl_admin_title.pack(fill=X)

                # ADMIN BUTTONS
                btn_admin_add = Button(MidLeft, text="+Add New Admin", bg="light green",
                                       font=('Times New Roman', 12, 'bold'),
                                       command=Admin_AddNewWindow)
                btn_admin_add.pack(side=LEFT)

                btn_admin_delete = Button(MidRight, text="-Delete Admin", bg="yellow",
                                          font=('Times New Roman', 12, 'bold'),
                                          command=Admin_DeleteData)
                btn_admin_delete.pack(side=RIGHT)

                scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
                scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
                tree = ttk.Treeview(TableMargin, columns=(
                    "Admin_ID", "Username", "Password", "Email", "Department", "Position"),
                                    height=400, selectmode="extended", yscrollcommand=scrollbary.set,
                                    xscrollcommand=scrollbarx.set)

                scrollbary.config(command=tree.yview)
                scrollbary.pack(side=RIGHT, fill=Y)
                scrollbarx.config(command=tree.xview)
                scrollbarx.pack(side=BOTTOM, fill=X)
                tree.heading('Admin_ID', text="Admin_ID", anchor=W)
                tree.heading('Username', text="Username", anchor=W)
                tree.heading('Password', text="Password", anchor=W)
                tree.heading('Email', text="Email", anchor=W)
                tree.heading('Department', text="Department", anchor=W)
                tree.heading('Position', text="Position", anchor=W)
                tree.column('#0', stretch=NO, minwidth=0, width=0)
                tree.column('#1', stretch=NO, minwidth=0, width=0)
                tree.column('#2', stretch=NO, minwidth=0, width=150)
                tree.column('#3', stretch=NO, minwidth=0, width=0)
                tree.column('#4', stretch=NO, minwidth=0, width=150)
                tree.column('#5', stretch=NO, minwidth=0, width=150)
                tree.column('#6', stretch=NO, minwidth=0, width=150)
                tree.pack()
                tree.bind('<Double-Button-1>', Admin_OnSelected)

                if __name__ == '__main__':
                    Admin_Database()
                    root_cms_admin_manager.mainloop()
                    root_cms_admin_manager.quit()

            def Database():
                conn = sqlite3.connect("ContactsDataSource.db")
                cursor = conn.cursor()
                cursor.execute(
                    "CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, "
                    "firstname TEXT, "
                    "lastname TEXT, gender TEXT, age TEXT, address TEXT, contact TEXT, reminder TEXT)")
                cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data))
                cursor.close()
                conn.close()

            def SubmitData():
                if FIRSTNAME.get() == "" or LASTNAME.get() == "" or GENDER.get() == "" or AGE.get() == "" or \
                        ADDRESS.get() == "" or CONTACT.get() == "" or REMINDER.get() == "":
                    result = tkMessageBox.showwarning('Oops!', 'Please Complete The Required Fields', icon="warning")
                else:
                    tree.delete(*tree.get_children())
                    conn = sqlite3.connect("ContactsDataSource.db")
                    cursor = conn.cursor()
                    cursor.execute(
                        "INSERT INTO `member` (firstname, lastname, gender, age, address, contact, reminder) VALUES(?, "
                        "?, ?, ?, ?, ?, ?)", (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()),
                                              str(AGE.get()), str(ADDRESS.get()), str(CONTACT.get()),
                                              str(REMINDER.get())))
                    conn.commit()
                    cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
                    fetch = cursor.fetchall()
                    for data in fetch:
                        tree.insert('', 'end', values=(data))
                    cursor.close()
                    conn.close()
                    FIRSTNAME.set("")
                    LASTNAME.set("")
                    GENDER.set("")
                    AGE.set("")
                    ADDRESS.set("")
                    CONTACT.set("")
                    REMINDER.set("")
                    tkMessageBox.showwarning('Confirmation', 'Contact Saved Successfully', icon="info")

            def UpdateData():
                if GENDER.get() == "":
                    result = tkMessageBox.showwarning('Oops', 'Please Complete The Required Fields', icon="warning")
                else:
                    tree.delete(*tree.get_children())
                    conn = sqlite3.connect("ContactsDataSource.db")
                    cursor = conn.cursor()
                    cursor.execute(
                        "UPDATE `member` SET `firstname` = ?, `lastname` = ?, `gender` = ?, `age` = ?,  `address` = ?, "
                        "`contact`= "
                        "?, `reminder` = "
                        "? WHERE `mem_id` = ?",
                        (str(FIRSTNAME.get()), str(LASTNAME.get()), str(GENDER.get()), str(AGE.get()),
                         str(ADDRESS.get()),
                         str(CONTACT.get()), str(REMINDER.get()), int(mem_id)))
                    conn.commit()
                    cursor.execute("SELECT * FROM `member` ORDER BY `lastname` ASC")
                    fetch = cursor.fetchall()
                    for data in fetch:
                        tree.insert('', 'end', values=(data))
                    cursor.close()
                    conn.close()
                    FIRSTNAME.set("")
                    LASTNAME.set("")
                    GENDER.set("")
                    AGE.set("")
                    ADDRESS.set("")
                    CONTACT.set("")
                    REMINDER.set("")
                    tkMessageBox.showwarning('Confirmation', 'Contact Updated Successfully', icon="info")

            def OnSelected(event):
                global mem_id, UpdateWindow
                curItem = tree.focus()
                contents = (tree.item(curItem))
                selecteditem = contents['values']
                try:
                    mem_id = selecteditem[0]
                    FIRSTNAME.set("")
                    LASTNAME.set("")
                    GENDER.set("")
                    AGE.set("")
                    ADDRESS.set("")
                    CONTACT.set("")
                    REMINDER.set("")
                    FIRSTNAME.set(selecteditem[1])
                    LASTNAME.set(selecteditem[2])
                    AGE.set(selecteditem[4])
                    ADDRESS.set(selecteditem[5])
                    CONTACT.set(selecteditem[6])
                    REMINDER.set(selecteditem[7])
                    UpdateWindow = Toplevel()
                    try:
                        p2 = PhotoImage(file="cms_icon.png", master=UpdateWindow)
                        UpdateWindow.iconphoto(0, p2)
                        UpdateWindow.title("Contacts Management System")
                        width = 500
                        height = 400
                        screen_width = root.winfo_screenwidth()
                        screen_height = root.winfo_screenheight()
                        x = ((screen_width / 2) + 450) - (width / 2)
                        y = ((screen_height / 2) + 20) - (height / 2)
                        UpdateWindow.resizable(0, 0)
                        UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
                        if 'NewWindow' in globals():
                            NewWindow.destroy()

                        # FRAMES
                        FormTitle = Frame(UpdateWindow)
                        FormTitle.pack(side=TOP)
                        ContactForm = Frame(UpdateWindow)
                        ContactForm.pack(side=TOP, pady=10)
                        RadioGroup = Frame(ContactForm)
                        Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",
                                           font=('Times New Roman', 14)).pack(
                            side=LEFT)
                        Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",
                                             font=('Times New Roman', 14)).pack(side=LEFT)

                        # LABELS
                        lbl_title = Label(FormTitle, text="Updating Contacts", font=('Times New Roman', 16), bg="orange",
                                          width=300)
                        lbl_title.pack(fill=X)
                        lbl_firstname = Label(ContactForm, text="Firstname", font=('Times New Roman', 14), bd=5)
                        lbl_firstname.grid(row=0, sticky=W)
                        lbl_lastname = Label(ContactForm, text="Lastname", font=('Times New Roman', 14), bd=5)
                        lbl_lastname.grid(row=1, sticky=W)
                        lbl_gender = Label(ContactForm, text="Gender", font=('Times New Roman', 14), bd=5)
                        lbl_gender.grid(row=2, sticky=W)
                        lbl_age = Label(ContactForm, text="Age", font=('Times New Roman', 14), bd=5)
                        lbl_age.grid(row=3, sticky=W)
                        lbl_address = Label(ContactForm, text="Address", font=('Times New Roman', 14), bd=5)
                        lbl_address.grid(row=4, sticky=W)
                        lbl_contact = Label(ContactForm, text="Contact", font=('Times New Roman', 14), bd=5)
                        lbl_contact.grid(row=5, sticky=W)
                        lbl_reminder = Label(ContactForm, text="Reminder", font=('Times New Roman', 14), bd=5)
                        lbl_reminder.grid(row=6, sticky=W)

                        # ENTRY
                        firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('Times New Roman', 14))
                        firstname.grid(row=0, column=1)
                        lastname = Entry(ContactForm, textvariable=LASTNAME, font=('Times New Roman', 14))
                        lastname.grid(row=1, column=1)
                        RadioGroup.grid(row=2, column=1)
                        age = Entry(ContactForm, textvariable=AGE, font=('Times New Roman', 14))
                        age.grid(row=3, column=1)
                        address = Entry(ContactForm, textvariable=ADDRESS, font=('Times New Roman', 14))
                        address.grid(row=4, column=1)
                        contact = Entry(ContactForm, textvariable=CONTACT, font=('Times New Roman', 14))
                        contact.grid(row=5, column=1)
                        reminder = Entry(ContactForm, textvariable=REMINDER, font=('Times New Roman', 14))
                        reminder.grid(row=6, column=1)

                        # BUTTONS
                        btn_updatecon = Button(ContactForm, text="Update", width=50, font=('Times New Roman', 10, 'bold'),
                                               command=UpdateData)
                        btn_updatecon.grid(row=7, columnspan=2, pady=10)
                    except TclError:
                        tkMessageBox.showwarning('Oops!', 'Do not close the main Window!..Application will now Exit',
                                                 icon="warning")
                except IndexError:
                    tkMessageBox.showwarning('Oops!', 'Please Select The Contact First!', icon="warning")

            def DeleteData():

                if not tree.selection():
                    result = tkMessageBox.showwarning('Oops!', 'Please Select The Contact First!', icon="warning")
                else:
                    result = tkMessageBox.askquestion('Confirm?', 'Are you sure you want to delete this record?',
                                                      icon="warning")
                    if result == 'yes':
                        curItem = tree.focus()
                        contents = (tree.item(curItem))
                        selecteditem = contents['values']
                        tree.delete(curItem)
                        conn = sqlite3.connect("ContactsDataSource.db")
                        cursor = conn.cursor()
                        cursor.execute("DELETE FROM `member` WHERE `mem_id` = %d" % selecteditem[0])
                        conn.commit()
                        cursor.close()
                        conn.close()
                        tkMessageBox.showwarning('Confirmation', 'Contact Deleted Successfully', icon="info")

            def AddNewWindow():
                global NewWindow
                FIRSTNAME.set("")
                LASTNAME.set("")
                GENDER.set("")
                AGE.set("")
                ADDRESS.set("")
                CONTACT.set("")
                REMINDER.set("")
                NewWindow = Toplevel()
                p2 = PhotoImage(file="cms_icon.png", master=NewWindow)
                NewWindow.iconphoto(0, p2)
                NewWindow.title("Contacts Management System")
                width = 500
                height = 400
                screen_width = root_cms.winfo_screenwidth()
                screen_height = root_cms.winfo_screenheight()
                x = ((screen_width / 2) - 455) - (width / 2)
                y = ((screen_height / 2) + 20) - (height / 2)
                NewWindow.resizable(0, 0)
                NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
                if 'UpdateWindow' in globals():
                    UpdateWindow.destroy()

                # FRAMES
                FormTitle = Frame(NewWindow)
                FormTitle.pack(side=TOP)
                ContactForm = Frame(NewWindow)
                ContactForm.pack(side=TOP, pady=10)
                RadioGroup = Frame(ContactForm)
                Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male", font=('Times New Roman', 14)).pack(
                    side=LEFT)
                Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",
                                     font=('Times New Roman', 14)).pack(side=LEFT)

                # LABELS
                lbl_title = Label(FormTitle, text="Adding New Contacts", font=('Times New Roman', 16), bg="#66ff66",
                                  width=300)
                lbl_title.pack(fill=X)
                lbl_firstname = Label(ContactForm, text="Firstname", font=('Times New Roman', 14), bd=5)
                lbl_firstname.grid(row=0, sticky=W)
                lbl_lastname = Label(ContactForm, text="Lastname", font=('Times New Roman', 14), bd=5)
                lbl_lastname.grid(row=1, sticky=W)
                lbl_gender = Label(ContactForm, text="Gender", font=('Times New Roman', 14), bd=5)
                lbl_gender.grid(row=2, sticky=W)
                lbl_age = Label(ContactForm, text="Age", font=('Times New Roman', 14), bd=5)
                lbl_age.grid(row=3, sticky=W)
                lbl_address = Label(ContactForm, text="Address", font=('Times New Roman', 14), bd=5)
                lbl_address.grid(row=4, sticky=W)
                lbl_contact = Label(ContactForm, text="Contact", font=('Times New Roman', 14), bd=5)
                lbl_contact.grid(row=5, sticky=W)
                lbl_reminder = Label(ContactForm, text="Reminder", font=('Times New Roman', 14), bd=5)
                lbl_reminder.grid(row=6, sticky=W)

                # ENTRY
                firstname = Entry(ContactForm, textvariable=FIRSTNAME, font=('Times New Roman', 14))
                firstname.grid(row=0, column=1)
                lastname = Entry(ContactForm, textvariable=LASTNAME, font=('Times New Roman', 14))
                lastname.grid(row=1, column=1)
                RadioGroup.grid(row=2, column=1)
                age = Entry(ContactForm, textvariable=AGE, font=('Times New Roman', 14))
                age.grid(row=3, column=1)
                address = Entry(ContactForm, textvariable=ADDRESS, font=('Times New Roman', 14))
                address.grid(row=4, column=1)
                contact = Entry(ContactForm, textvariable=CONTACT, font=('Times New Roman', 14))
                contact.grid(row=5, column=1)
                reminder = Entry(ContactForm, textvariable=REMINDER, font=('Times New Roman', 14))
                reminder.grid(row=6, column=1)

                # BUTTONS
                btn_addcon = Button(ContactForm, text="Save", width=50, font=('Times New Roman', 10, 'bold'),
                                    command=SubmitData)
                btn_addcon.grid(row=7, columnspan=2, pady=10)

            # FRAMES
            Top = Frame(root_cms, width=500, bd=1, relief=SOLID)
            Top.pack(side=TOP)
            Mid = Frame(root_cms, width=500, bg="#ffffff")
            Mid.pack(side=TOP)
            MidLeft = Frame(Mid, width=100)
            MidLeft.pack(side=LEFT, pady=10)
            MidLeftPadding = Frame(Mid, width=370, bg="#ffffff")
            MidLeftPadding.pack(side=LEFT)
            MidRight = Frame(Mid, width=100)
            MidRight.pack(side=RIGHT, pady=10)
            TableMargin = Frame(root_cms, width=500)
            TableMargin.pack(side=TOP)

            # LABELS
            lbl_title = Label(Top, text="Contacts Management System", bg="#ffffff", font=('Times New Roman', 16), width=500)
            lbl_title.pack(fill=X)

            # BUTTONS
            btn_add = Button(MidLeft, text="+Add New Contact", bg="light green", font=('Times New Roman', 12, 'bold'),
                             command=AddNewWindow)
            btn_add.pack(side=LEFT)

            btn_admin = Button(Mid, text="Manage Admins", bg="#eb9e34", font=('Times New Roman', 12, 'bold'),
                               command=Admin_Manager)
            btn_admin.place(x=250, y=10)

            btn_delete = Button(MidRight, text="-Delete Contact", bg="yellow", font=('Times New Roman', 12, 'bold'),
                                command=DeleteData)
            btn_delete.pack(side=RIGHT)

            # TABLE
            scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
            scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
            tree = ttk.Treeview(TableMargin, columns=(
                "MemberID", "Firstname", "Lastname", "Gender", "Age", "Address", "Contact", "Reminder"),
                                height=400, selectmode="extended", yscrollcommand=scrollbary.set,
                                xscrollcommand=scrollbarx.set)

            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('MemberID', text="MemberID", anchor=W)
            tree.heading('Firstname', text="Firstname", anchor=W)
            tree.heading('Lastname', text="Lastname", anchor=W)
            tree.heading('Gender', text="Gender", anchor=W)
            tree.heading('Age', text="Age", anchor=W)
            tree.heading('Address', text="Address", anchor=W)
            tree.heading('Contact', text="Contact", anchor=W)
            tree.heading('Reminder', text="Reminder", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=0)
            tree.column('#2', stretch=NO, minwidth=0, width=80)
            tree.column('#3', stretch=NO, minwidth=0, width=120)
            tree.column('#4', stretch=NO, minwidth=0, width=90)
            tree.column('#5', stretch=NO, minwidth=0, width=80)
            tree.column('#6', stretch=NO, minwidth=0, width=120)
            tree.column('#7', stretch=NO, minwidth=0, width=120)
            tree.column('#8', stretch=NO, minwidth=0, width=120)
            tree.pack()
            tree.bind('<Double-Button-1>', OnSelected)

            # MainMethod
            if __name__ == '__main__':
                Database()
                root_cms.mainloop()
                root_cms.quit()

        else:
            ms.showerror('Oops!', 'Username Not Found. Invalid Credentials.')

    # Frame Packing Methods
    def log(self):
        self.username.set('')
        self.password.set('')
        self.crf.pack_forget()
        self.head['text'] = ' Admin Login '
        self.logf.pack()

    # Draw Widgets
    def widgets(self):
        self.head = Label(self.master, text='Head Administrator Login', bg='light blue', font=('Times New Roman',
                                                                                                    30, UNDERLINE),
                          pady=10)
        self.head.pack()
        self.logf = Frame(self.master, padx=10, pady=10)
        Label(self.logf, text='Username: ', font=('Times New Roman', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.username, bd=5, font=('Times New Roman', 15)).grid(row=0, column=1)
        Label(self.logf, text='Password: ', font=('Times New Roman', 20), pady=5, padx=5).grid(sticky=W)
        Entry(self.logf, textvariable=self.password, bd=5, font=('Times New Roman', 15), show='*').grid(row=1, column=1)
        Button(self.logf, text=' Login ', bg='light green', bd=3, font=('Times New Roman', 15),
               command=self.login).grid(row=2, columnspan=1)
        Button(self.logf, text=' Forgot Password? ', bg='yellow', bd=3, font=('Times New Roman', 15),
                command=self.contact_admin).place(x=170, y=90)
        self.logf.pack()


if __name__ == '__main__':
    # Create Object
    # and setup window
    root = Tk()
    root.title('Contacts Management System')
    root.config(bg="#ffffff")
    p1 = PhotoImage(file="admin_icon.png")

    root.iconphoto(0, p1)
    width = 425
    height = 230
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    root.config(bg="#ffffff")
    AdminMain(root)
    root.mainloop()

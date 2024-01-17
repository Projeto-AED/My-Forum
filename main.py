from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk

fUsers = "files/users.txt"
fWaitingUsers = "files\waitingUsers.txt"
fCategories = "files\categories.txt"
fNotifications = "files\notifications.txt"

window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
window.geometry("1000x500")
window.title('my Forum')

# Main Page (With Image, Login, Registration and Leave Buttons)
def indexPage():
    # Action Window, where the User inputs performs Actions
    actionWindow = PanedWindow(window, width=750, height=450)
    actionWindow.place(x=250, y=50)

    mainBGImg = Canvas(actionWindow, width=750, height=500)
    mainBGImg.place(x=0, y=0)
    global img
    img = PhotoImage(file="images\\mainpage_bg.png")
    mainBGImg.create_image(375, 225, image=img)

    # Index
    indexMenu = PanedWindow(window, bg="#3c72c2", width=250, height=500)
    indexMenu.place(x=0, y=0)

    imageLogin = Image.open("images\\loginIMG.png")
    resizedLoginIMG = imageLogin.resize((50, 50))
    imgLogin = ImageTk.PhotoImage(resizedLoginIMG)
    btnLogin = Button(indexMenu, image=imgLogin, width = 230 , height = 50, relief="sunken", compound=LEFT, text="Login", font="Calibri, 11", command=loginPanel)
    btnLogin.image = imgLogin
    btnLogin.place(x=5, y=50)

    imageConta = Image.open("images\\registerIMG.png")
    resizedContaIMG = imageConta.resize((50, 50))
    imgConta = ImageTk.PhotoImage(resizedContaIMG)
    btnRegister = Button(indexMenu, image=imgConta, width = 230 , height = 50, relief="sunken", compound=LEFT, text="Register", font="Calibri, 11", command=registerPanel)
    btnRegister.image = imgConta
    btnRegister.place(x=5, y=210)

    imageSair = Image.open("images\\removeUserIMG.png")
    resizedSairIMG = imageSair.resize((50, 50))
    imgSair = ImageTk.PhotoImage(resizedSairIMG)
    btnLeave = Button(indexMenu, image=imgSair, width = 230 , height = 50,text="Leave App", relief="sunken", compound=LEFT, font="Calibri, 11", command=window.destroy)
    btnLeave.image = imgSair
    btnLeave.place(x=5, y=370)

# Admin Dashboard
def adminDashboard():
    adminMenu = PanedWindow(window, bg="#3c72c2", width=250, height=500)
    adminMenu.place(x=0, y=0)

    imageApprovedUsers = Image.open("images\\approveUsersIMG.png")
    resizedApprovedUsersIMG = imageApprovedUsers.resize((50, 50))
    imgApprovedUsers = ImageTk.PhotoImage(resizedApprovedUsersIMG)
    btnApprovedUsers = Button(adminMenu, image=imgApprovedUsers, width = 230 , height = 50, relief="sunken", compound=LEFT, text="Approve Users", font="Calibri, 11", command=approvingUsersPanel)
    btnApprovedUsers.image = imgApprovedUsers
    btnApprovedUsers.place(x=5, y=50)

    imageCategorySettings = Image.open("images\\settingsIMG.png")
    resizedCategorySettingsIMG = imageCategorySettings.resize((50, 50))
    imgCategorySettings = ImageTk.PhotoImage(resizedCategorySettingsIMG)
    btnCategorySettings = Button(adminMenu, image=imgCategorySettings, width = 230 , height = 50, relief="sunken", compound=LEFT, text="Category Settings", font="Calibri, 11", command=categorySettingsPanel)
    btnCategorySettings.image = imgCategorySettings
    btnCategorySettings.place(x=5, y=160)

    imageNotificationSettings = Image.open("images\\settingsIMG.png")
    resizedNotificationSettingsIMG = imageNotificationSettings.resize((50, 50))
    imgNotificationSettings = ImageTk.PhotoImage(resizedNotificationSettingsIMG)
    btnNotificationSettings = Button(adminMenu, image=imgNotificationSettings, width = 230 , height = 50, relief="sunken", compound=LEFT, text="Notification Settings", font="Calibri, 11", command=notificationSettingsPanel)
    btnNotificationSettings.image = imgNotificationSettings
    btnNotificationSettings.place(x=5, y=270)

    imageLeave = Image.open("images\\removeUserIMG.png")
    resizedLeaveIMG = imageLeave.resize((50, 50))
    imgLeave = ImageTk.PhotoImage(resizedLeaveIMG)
    btnLeave = Button(adminMenu, image=imgLeave, width = 230 , height = 50,text="Leave App", relief="sunken", compound=LEFT, font="Calibri, 11", command=window.destroy)
    btnLeave.image = imgLeave
    btnLeave.place(x=5, y=370)

def userDashboard(userName):
    userMenu = PanedWindow(window, bg="#3c72c2", width=250, height=500)
    userMenu.place(x=0, y=0)

def approvingUsersPanel():
    panelApprovingUsers = PanedWindow(window, width=750, height=450, relief = "sunken")
    panelApprovingUsers.place(x=250, y=50)

    treeviewPanel = PanedWindow(panelApprovingUsers, width = 720, height = 150, bd = "3", relief = "sunken")
    treeviewPanel.place(x=175, y=10)

    def readUsersToTreeview(treeview):
        with open(fWaitingUsers, "r", encoding="utf-8") as file:
            waiting_users_list = file.readlines()

        treeview.delete(*treeview.get_children())

        for line in waiting_users_list:
            username, password = line.strip().split(";")
            treeview.insert("", "end", values=(username, password))

    def approveUser():
        selected_item = treeview.selection()
        if not selected_item:
            messagebox.showinfo("Approve User", "Please select a user to approve.")
            return

        username, password = treeview.item(selected_item, "values")

        with open(fUsers, "a", encoding="utf-8") as users_file:
            users_file.write(f"{username};{password}\n")

        with open(fWaitingUsers, "r", encoding="utf-8") as waiting_file:
            waiting_users_list = waiting_file.readlines()

        with open(fWaitingUsers, "w", encoding="utf-8") as waiting_file:
            for line in waiting_users_list:
                if line.strip().split(";")[0] != username:
                    waiting_file.write(line)

        readUsersToTreeview(treeview)
        messagebox.showinfo("Approve User", f"The user {username} has been approved.")

    def removeUser():
        selected_item = treeview.selection()
        if not selected_item:
            messagebox.showinfo("Remove User", "Please select a user to remove.")
            return

        username = treeview.item(selected_item, "values")[0]

        with open(fWaitingUsers, "r", encoding="utf-8") as file:
            waiting_users_list = file.readlines()

        with open(fWaitingUsers, "w", encoding="utf-8") as file:
            for line in waiting_users_list:
                if line.strip().split(";")[0] != username:
                    file.write(line)

        readUsersToTreeview(treeview)
        messagebox.showinfo("Remove User", f"The user {username} has been removed.")

    treeview = ttk.Treeview(treeviewPanel, columns=("Username", "Password"), show="headings")
    treeview.heading("Username", text="Username")
    treeview.heading("Password", text="Password")

    vsb = ttk.Scrollbar(treeviewPanel, orient="vertical", command=treeview.yview)
    treeview.configure(yscrollcommand=vsb.set)

    hsb = ttk.Scrollbar(treeviewPanel, orient="horizontal", command=treeview.xview)
    treeview.configure(xscrollcommand=hsb.set)

    treeview.grid(column=0, row=0, sticky="nsew")
    vsb.grid(column=1, row=0, sticky="ns")
    hsb.grid(column=0, row=1, sticky="ew")

    treeviewPanel.columnconfigure(0, weight=1)
    treeviewPanel.rowconfigure(0, weight=1)

    btnRemoveUser = Button(panelApprovingUsers, text="Remove User", width=12, height=4, fg="black", command=removeUser)
    btnRemoveUser.place(x=450, y=304)

    btnApproveUser = Button(panelApprovingUsers, text="Approve User", width=12, height=4, fg="black", command=approveUser)
    btnApproveUser.place(x=210, y=304)

    readUsersToTreeview(treeview)

# Categories Panel
def categorySettingsPanel():
    categoryPanel = PanedWindow(window, width=750, height=450, relief="sunken")
    categoryPanel.place(x=250, y=50)

    def addCategory():
        new_category = category.get()
        with open(fCategories, "a", encoding="utf-8") as file:
            file.write(new_category + "\n")
        tViewCategories.insert("", "end", values=(new_category,))
        category.set("")

    def removeCategory():
        selected_item = tViewCategories.selection()
        if not selected_item:
            messagebox.showinfo("Remove Category", "Please select a category to remove.")
            return

        category = tViewCategories.item(selected_item, "values")[0]

        with open(fCategories, "r", encoding="utf-8") as file:
            categoriesList = file.readlines()

        with open(fCategories, "w", encoding="utf-8") as file:
            for line in categoriesList:
                if line.strip().split(";")[0] != category:
                    file.write(line)

        refreshCategoriesView()

        messagebox.showinfo("Remove User", f"The category {category} has been removed.")
    
    def refreshCategoriesView():
        with open(fCategories, "r", encoding="utf-8") as file:
            categories_list = [category.strip() for category in file.readlines()]

        tViewCategories.delete(*tViewCategories.get_children())
        for category in categories_list:
            tViewCategories.insert("", "end", values=(category,))

    # Category Treeview Panel
    treeViewPanel = PanedWindow(categoryPanel, width=250, height=300, bd="3", relief="sunken")
    treeViewPanel.place(x=20, y=75)

    # Category Treeview
    tViewCategories = ttk.Treeview(treeViewPanel, columns=("Categories",), show="headings")
    tViewCategories.heading("Categories", text="Categories")

    vsb = ttk.Scrollbar(treeViewPanel, orient="vertical", command=tViewCategories.yview)
    tViewCategories.configure(yscrollcommand=vsb.set)

    tViewCategories.grid(column=0, row=0, sticky="nsew")
    vsb.grid(column=1, row=0, sticky="ns")

    treeViewPanel.columnconfigure(0, weight=1)
    treeViewPanel.rowconfigure(0, weight=1)

    # Add Category Panel
    inputCategoryPanel = PanedWindow(categoryPanel, width=350, height=100, bd="3", relief="sunken")
    inputCategoryPanel.place(x=300, y=75)

    # Label
    lblCategory = Label(inputCategoryPanel, text="Category:", fg="blue", font=("Helvetica", 9))
    lblCategory.place(x=20, y=30)

    # Entry
    category = StringVar()
    txtCategory = Entry(inputCategoryPanel, width=35, textvariable=category)
    txtCategory.place(x=80, y=30)

    # Buttons
    btnAdd = Button(categoryPanel, text="Add", width=12, height=4, fg="black", command=addCategory)
    btnAdd.place(x=300, y=304)

    btnRemove = Button(categoryPanel, text="Remove", width=12, height=4, fg="black", command=removeCategory)
    btnRemove.place(x=423, y=304)

    # Reads the existing categories from the file
    fileCategories = open(fCategories, "r", encoding="utf-8")
    categoriesList = fileCategories.readlines()
    fileCategories.close()

    for line in categoriesList:
        tViewCategories.insert("", "end", values=(line.strip(),))

def notificationSettingsPanel():

    fNotifications = "files\notifications.txt"
    
    categoryPanel = PanedWindow(window, width=750, height=450, relief = "sunken")
    categoryPanel.place(x=250, y=50)

# Registration Page
def registerPanel():
    panelRegister = PanedWindow(window, width=750, height=450, relief="sunken")
    panelRegister.place(x=250, y=50)

    labelNewUser = Label(panelRegister, text="New Username:", font="Calibri, 11")
    labelNewUser.place(x=140, y=100)
    newUser = StringVar()
    txtNewUser = Entry(panelRegister, width=40, textvariable=newUser)
    txtNewUser.place(x=280, y=100)

    labelNewPass = Label(panelRegister, text="New Password:", font="Calibri, 11")
    labelNewPass.place(x=140, y=150)
    newPass = StringVar()
    txtNewPass = Entry(panelRegister, width=40, textvariable=newPass, show="*")
    txtNewPass.place(x=280, y=150)

    labelRewritePass = Label(panelRegister, text="Rewrite Password:", font="Calibri, 11")
    labelRewritePass.place(x=140, y=200)
    rewritePass = StringVar()
    txtRewritePass = Entry(panelRegister, width=40, textvariable=rewritePass, show="*")
    txtRewritePass.place(x=280, y=200)

    btnSubmit = Button(panelRegister, text="Submit", font="Calibri, 11", width=25, height=3, command=lambda: createAccount(newUser.get(), newPass.get(), rewritePass.get(), panelRegister))
    btnSubmit.place(x=260, y=250)

# Login Page
def loginPanel():
    panelUsers = PanedWindow(window, width=750, height=450, relief = "sunken")
    panelUsers.place(x=250, y=50)

    labelUsers = Label(panelUsers, text ="Username:", font="Calibri, 11")
    labelUsers.place(x=200, y= 100)
    userName = StringVar()
    txtUser = Entry(panelUsers, width=40, textvariable = userName)
    txtUser.place(x=280, y= 100)

    labelPass = Label(panelUsers, text ="Password:", font="Calibri, 11")
    labelPass.place(x=200, y= 150)
    userPass = StringVar()
    txtPass = Entry(panelUsers, width=40, textvariable = userPass, show = "*")
    txtPass.place(x=280, y= 150)

    btnLogin = Button(panelUsers, text = "Login", font="Calibri, 11", width=25, height=3, command = lambda: checkUser(userName.get(), userPass.get(), panelUsers))
    btnLogin.place(x=260, y= 200)

# User Authentication Functions (Login and Register):
def checkUser(userName, userPass, panelUsers):
    fileUsers=open(fUsers, "r", encoding="utf-8")
    usersList = fileUsers.readlines()
    fileUsers.close()

    if userName == "admin" and userPass == "admin":
        messagebox.showinfo("Login", "Welcome Admin!")
        panelUsers.destroy()
        adminDashboard()
    else:
        for line in usersList:
            if line.strip() == f"{userName};{userPass}":
                msg = "Welcome " + userName
                messagebox.showinfo("Login", msg)
                # has userName as input because it'll be needed to identify the User throughout posts and such.
                userDashboard(userName)
                return msg
        messagebox.showerror("Login Failed", "Your Username or Password are Incorrect!")
    return ""

# Working
def createAccount(userName, userPass, userPassConfirm, panelUsers):

    if userPass != userPassConfirm:
        messagebox.showerror("Create Account Error", "Your passwords are different!")
        return  
    if userName == "" or userPass == "":
        messagebox.showerror("Create Account Error", "Username and Password can't be blank!")
        return         
    fileUsers=open(fUsers, "r", encoding="utf-8")
    usersList = fileUsers.readlines()
    fileUsers.close()
    for line in usersList:
        fields = line.split(";")
        if fields[0] == userName:
            messagebox.showerror("Create Account Error", "Try another username!")
            return 
    fileWaitingUsers = open(fWaitingUsers, "a")
    line = userName + ";" + userPass + "\n"
    fileWaitingUsers.write(line)
    fileWaitingUsers.close()
    messagebox.showinfo("Create Account", "Successful! Wait until an Admin approves your request!")
    panelUsers.destroy()

#Launch My Forum!
indexPage()
window.mainloop()
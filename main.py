from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk

fUsers = "files/users.txt"

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

    fWaitingUsers = "files\waitingUsers.txt"

    """with open(fWaitingUsers, "r") as file:
        waitingUsers = file.readlines()

    initialX = 280
    initialY = 50

    if not waitingUsers:
        labelNoWaitingUsers = Label(panelApprovingUsers, text="No Waiting Users", font=("Helvetica", 12), bg="#3498db", fg="white")
        labelNoWaitingUsers.place()
    else:
        for waitingUser in waitingUsers:
            waitingUserLabel = Label(panelApprovingUsers, text="Waiting User:", font=("Helvtica", 12), bg="#3498db", fg="white")
            waitingUserLabel.place(x=initialX, y=initialY)

            btn_aprovar = Button(panelApprovingUsers, text="Aprovar", command=lambda u=waitingUser: aprovar_utilizador(u), bg="#2ecc71", fg="white", font=("Helvetica", 12), padx=5)
            btn_aprovar.place(x=int(initialX), y=int(initialY+30))

            btn_rejeitar = Button(panelApprovingUsers, text="Rejeitar", command=lambda u=waitingUser: rejeitar_utilizador(u), bg="#e74c3c", fg="white", font=("Helvetica", 12), padx=5)
            btn_rejeitar.place(x=int(initialX+30), y=int(initialY+30))"""

# Categories Panel
def categorySettingsPanel():

    fCategories = "files\categories.txt"
    
    categoryPanel = PanedWindow(window, width=750, height=450, relief = "sunken")
    categoryPanel.place(x=250, y=50)

    def addCategory():
        new_category = category.get()
        with open(fCategories, "a", encoding="utf-8") as file:
            file.write(new_category + "\n")
        lboxCategories.insert("end", new_category)
        category.set("")
    
    def saveCategoriesToFile():
        categories = lboxCategories.get(0, "end")
        categories = [category for category in categories if category]
        with open(fCategories, "w", encoding="utf-8") as file:
            file.write("\n".join(categories))

    def removeCategory():
        selectedIndex = lboxCategories.curselection()

        if selectedIndex:
            selectedCategory = lboxCategories.get(selectedIndex)
            lboxCategories.delete(selectedIndex)

            with open(fCategories, "r", encoding="utf-8") as file:
                categoriesList = file.readlines()

            with open(fCategories, "w", encoding="utf-8") as file:
                for line in categoriesList:
                    if line.strip() != selectedCategory:
                        file.write(line)

    # Category ListBox Panel
    listBoxPanel = PanedWindow(categoryPanel, width = 250, height = 300, bd = "3", relief = "sunken")
    listBoxPanel.place(x=20, y=75)

    # Category ListBox
    lboxCategories=Listbox(listBoxPanel, width = 35, height=15, bd="3", selectmode = "single", selectbackground="blue")
    lboxCategories.place(x=13, y= 25)

    # Add Category Panel
    inputCategoryPanel = PanedWindow(categoryPanel, width = 350, height = 100, bd = "3", relief = "sunken")
    inputCategoryPanel.place(x=300, y=75)
    # Label
    lblCategory=Label(inputCategoryPanel, text="Category:", fg="blue", font=("Helvetica", 9))
    lblCategory.place(x=20, y=30)
    # Entry
    category = StringVar()
    txtCategory = Entry(inputCategoryPanel, width = 35, textvariable = category)
    txtCategory.place(x=80, y=30)

    #Buttons
    btnAdd = Button(categoryPanel, text="Add", width=12, height=4, fg="black", command = addCategory)
    btnAdd.place(x=300, y=304)

    btnRemove = Button(categoryPanel, text="Remove", width=12, height=4, fg="black", command = removeCategory)
    btnRemove.place(x=423, y=304)

    btnSaveCategories = Button(categoryPanel, text="Save Categories", width=12, height=4, command = saveCategoriesToFile)
    btnSaveCategories.place(x=545, y=304)

    # Reads the existing categories on the file
    fileCategories = open(fCategories, "r", encoding="utf-8")
    categoriesList = fileCategories.readlines()
    fileCategories.close()
    for line in categoriesList:
        lboxCategories.insert("end", line)

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

    fWaitingUsers = "files\waitingUsers.txt"

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
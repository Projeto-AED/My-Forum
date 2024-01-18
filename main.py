from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk
import os

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
    
    imageProfileStats = Image.open("images\\registerIMG.png")
    resizedProfileStatsIMG = imageProfileStats.resize((50, 50))
    imgProfileStats = ImageTk.PhotoImage(resizedProfileStatsIMG)
    btnProfileStats = Button(userMenu, image=imgProfileStats, width = 230 , height = 50, relief="sunken", compound=LEFT, text = (userName)+"'s Statistics", font="Calibri, 11")
    btnProfileStats.image = imgProfileStats
    btnProfileStats.place(x=5, y=20)

    imageNewPost = Image.open("images\\postIMG.png")
    resizedNewPostIMG = imageNewPost.resize((50, 50))
    imgNewPost = ImageTk.PhotoImage(resizedNewPostIMG)
    btnNewPost = Button(userMenu, image=imgNewPost, width = 230 , height = 50, relief="sunken", compound=LEFT, text="New Post", font="Calibri, 11")
    btnNewPost.image = imgNewPost
    btnNewPost.place(x=5, y=100)

    imageViewPosts = Image.open("images\\viewPostsIMG.png")
    resizedViewPostsIMG = imageViewPosts.resize((50, 50))
    imgViewPosts = ImageTk.PhotoImage(resizedViewPostsIMG)
    btnViewPosts = Button(userMenu, image=imgViewPosts, width = 230 , height = 50, relief="sunken", compound=LEFT, text="View Posts", font="Calibri, 11")
    btnViewPosts.image = imgViewPosts
    btnViewPosts.place(x=5, y=180)

    imageLikedPosts = Image.open("images\\likedPostsIMG.png")
    resizedLikedPostsIMG = imageLikedPosts.resize((50, 50))
    imgLikedPosts = ImageTk.PhotoImage(resizedLikedPostsIMG)
    btnLikedPosts = Button(userMenu, image=imgLikedPosts, width = 230 , height = 50, relief="sunken", compound=LEFT, text="Liked Posts", font="Calibri, 11")
    btnLikedPosts.image = imgLikedPosts
    btnLikedPosts.place(x=5, y=260)

    imageViewNotifs = Image.open("images\\viewNotifsIMG.png")
    resizedViewNotifsIMG = imageViewNotifs.resize((50, 50))
    imgViewNotifs = ImageTk.PhotoImage(resizedViewNotifsIMG)
    btnViewNotifs = Button(userMenu, image=imgViewNotifs, width = 230 , height = 50, relief="sunken", compound=LEFT, text="Notifications", font="Calibri, 11", command = userNotificationsPanel)
    btnViewNotifs.image = imgViewNotifs
    btnViewNotifs.place(x=5, y=340)

    imageLeave = Image.open("images\\removeUserIMG.png")
    resizedLeaveIMG = imageLeave.resize((50, 50))
    imgLeave = ImageTk.PhotoImage(resizedLeaveIMG)
    btnLeave = Button(userMenu, image=imgLeave, width = 230 , height = 50,text="Leave App", relief="sunken", compound=LEFT, font="Calibri, 11", command=window.destroy)
    btnLeave.image = imgLeave
    btnLeave.place(x=5, y=420)

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

    # Category Panel
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
    notificationAdminPanel = PanedWindow(window, width=750, height=450, relief = "sunken")
    notificationAdminPanel.place(x=250, y=50)

    def sendNotification(title, text):
        notifications_file_path = "files\\notifications.txt"

        if title and text:
            with open(notifications_file_path, "a", encoding="utf-8") as notifications_file:
                notifications_file.write(f"{title};{text}\n")
            messagebox.showinfo("Send Notification", "Notification sent successfully!")

            readNotificationsToTreeview(treeviewNotifications)
        else:
            messagebox.showerror("Send Notification", "Title and Text cannot be empty!")

    def clearBoxes():
        notifTitle.set("")
        notifText.delete("1.0", "end")

    def editNotification():
        selected_item = treeviewNotifications.selection()
        if not selected_item:
            messagebox.showinfo("Edit Notification", "Please select a notification to edit.")
            return

        title, _ = treeviewNotifications.item(selected_item, "values")
        updated_title = notifTitle.get()
        updated_notification = notifText.get("1.0", "end-1c")

        notifications_file_path = os.path.join("files", "notifications.txt")

        with open(notifications_file_path, "r", encoding="utf-8") as file:
            notifications_list = file.readlines()

        with open(notifications_file_path, "w", encoding="utf-8") as file:
            for line in notifications_list:
                if line.strip().split(";")[0] != title:
                    file.write(line)
            file.write(f"{updated_title};{updated_notification}\n")

        readNotificationsToTreeview(treeviewNotifications)
        messagebox.showinfo("Edit Notification", "Notification edited successfully.")

    # Send Notifications Panel
    inputNotificationsPanel = PanedWindow(notificationAdminPanel, width=730, height=200, bd="3", relief="sunken")
    inputNotificationsPanel.place(x=10, y=10)

    lblNotifTitle = Label(inputNotificationsPanel, text="Title:", fg="blue", font=("Helvetica", 9))
    lblNotifTitle.place(x=20, y=10)

    notifTitle = StringVar()
    txtNotifTitle = Entry(inputNotificationsPanel, width=35, textvariable=notifTitle)
    txtNotifTitle.place(x=80, y=10)

    # Long Text Input Box
    lblNotifText = Label(inputNotificationsPanel, text="Notification Text:", fg="blue", font=("Helvetica", 9))
    lblNotifText.place(x=20, y=40)

    notifText = Text(inputNotificationsPanel, width=50, height=7)
    notifText.place(x=20, y=70)

    btnClearBoxes = Button(inputNotificationsPanel, text="Clear Boxes", width=12, height=2, fg="black", command=clearBoxes)
    btnClearBoxes.place(x=550, y=20)

    btnEditNotification = Button(inputNotificationsPanel, text="Edit\nNotification", width=12, height=2, fg="black", command = editNotification)
    btnEditNotification.place(x=550, y=70)

    btnSendNotification = Button(inputNotificationsPanel, text="Send\nNotification", width=12, height=2, fg="black", command=lambda: sendNotification(notifTitle.get(), notifText.get("1.0", "end-1c")))
    btnSendNotification.place(x=550, y=120)

    # Manage Already Existing Notifications
    def readNotificationsToTreeview(treeview):
        notifications_file_path = "files\\notifications.txt"

        with open(notifications_file_path, "r", encoding="utf-8") as file:
            notifications_list = file.readlines()

        treeview.delete(*treeview.get_children())

        for line in notifications_list:
            title, text = line.strip().split(";")
            treeview.insert("", "end", values=(title, text))

    def removeNotification(treeview):
        selected_item = treeview.selection()
        if not selected_item:
            messagebox.showinfo("Remove Notification", "Please select a notification to remove.")
            return

        title, notification = treeview.item(selected_item, "values")

        notifications_file_path = os.path.join("files", "notifications.txt")

        with open(notifications_file_path, "r", encoding="utf-8") as file:
            notifications_list = file.readlines()

        with open(notifications_file_path, "w", encoding="utf-8") as file:
            for line in notifications_list:
                if line.strip().split(";")[0] != title:
                    file.write(line)

        readNotificationsToTreeview(treeview)
        messagebox.showinfo("Remove Notification", f"The notification with title '{title}' has been removed.")

    manageNotificationsPanel = PanedWindow(notificationAdminPanel, width=730, height=180, bd="3", relief="sunken")
    manageNotificationsPanel.place(x=10, y=220)

    treeviewNotifications = ttk.Treeview(manageNotificationsPanel, columns=("Title", "Notification"), show="headings", height=8)
    treeviewNotifications.heading("Title", text="Title")
    treeviewNotifications.heading("Notification", text="Notification")

    vsbNotifications = ttk.Scrollbar(manageNotificationsPanel, orient="vertical", command=treeviewNotifications.yview)
    treeviewNotifications.configure(yscrollcommand=vsbNotifications.set)

    hsbNotifications = ttk.Scrollbar(manageNotificationsPanel, orient="horizontal", command=treeviewNotifications.xview)
    treeviewNotifications.configure(xscrollcommand=hsbNotifications.set)

    treeviewNotifications.grid(column=0, row=0, sticky="nsew")
    vsbNotifications.grid(column=1, row=0, sticky="ns")
    hsbNotifications.grid(column=0, row=1, sticky="ew")

    manageNotificationsPanel.columnconfigure(0, weight=1)
    manageNotificationsPanel.rowconfigure(0, weight=1)

    def onTreeviewSelect(event):
        selected_item = treeviewNotifications.selection()
        if selected_item:
            title, notification = treeviewNotifications.item(selected_item, "values")
            notifTitle.set(title)
            notifText.delete("1.0", "end")
            notifText.insert("1.0", notification)

    treeviewNotifications.bind("<<TreeviewSelect>>", onTreeviewSelect)

    btnRemoveNotification = Button(notificationAdminPanel, text="Remove\nNotification", width=12, height=4, fg="black", command=lambda: removeNotification(treeviewNotifications))
    btnRemoveNotification.place(x=555, y=280)

    readNotificationsToTreeview(treeviewNotifications)

def userNotificationsPanel():
    panelUserNotifs = PanedWindow(window, width=750, height=450, relief="sunken")
    panelUserNotifs.place(x=250, y=50)

    notifTreeviewPanel = PanedWindow(panelUserNotifs, width=730, height=350, bd="3", relief="sunken")
    notifTreeviewPanel.place(x=10, y=10)

    def readNotificationsToTreeview(treeview):
        notifications_file_path = "files\\notifications.txt"

        with open(notifications_file_path, "r", encoding="utf-8") as file:
            notifications_list = file.readlines()

        treeview.delete(*treeview.get_children())

        for line in notifications_list:
            title, text = line.strip().split(";")
            treeview.insert("", "end", values=(title, text))

    def onTreeviewSelect(event):
        selected_item = treeviewNotifications.selection()
        if not selected_item:
            return

        item_values = treeviewNotifications.item(selected_item, "values")
        if item_values:
            title, notification = item_values
            lblSelectedTitle.config(text=f"Title: {title}")
            lblSelectedNotification.config(text=f"Notification: {notification}")

    treeviewNotifications = ttk.Treeview(notifTreeviewPanel, columns=("Title", "Notification"), show="headings", height=8)
    treeviewNotifications.heading("Title", text="Title")
    treeviewNotifications.heading("Notification", text="Notification")

    treeviewNotifications.column("Title", width=150)
    treeviewNotifications.column("Notification", width=550)

    vsbNotifications = ttk.Scrollbar(notifTreeviewPanel, orient="vertical", command=treeviewNotifications.yview)
    treeviewNotifications.configure(yscrollcommand=vsbNotifications.set)

    hsbNotifications = ttk.Scrollbar(notifTreeviewPanel, orient="horizontal", command=treeviewNotifications.xview)
    treeviewNotifications.configure(xscrollcommand=hsbNotifications.set)

    treeviewNotifications.grid(column=0, row=0, sticky="nsew")
    vsbNotifications.grid(column=1, row=0, sticky="ns")
    hsbNotifications.grid(column=0, row=1, sticky="ew")

    notifTreeviewPanel.columnconfigure(0, weight=1)
    notifTreeviewPanel.rowconfigure(0, weight=1)

    readNotificationsToTreeview(treeviewNotifications)

    notificationDetailsPanel = PanedWindow(panelUserNotifs, width=730, height=120, bd="3", relief="sunken")
    notificationDetailsPanel.place(x=10, y=240)

    lblSelectedTitle = Label(notificationDetailsPanel, text="Title:", fg="blue", font=("Helvetica", 9), wraplength=180, justify="left")
    lblSelectedTitle.place(x=20, y=10)

    lblSelectedNotification = Label(notificationDetailsPanel, text="Notification:", fg="blue", font=("Helvetica", 9), wraplength=500, justify="left")
    lblSelectedNotification.place(x=20, y=40)

    btnForward = Button(panelUserNotifs, text="Next\nNotification", width=15, height=4, command=lambda: moveNotification(treeviewNotifications, 1))
    btnForward.place(x=620, y=365)

    btnBackward = Button(panelUserNotifs, text="Previous\nNotification", width=15, height=4, command=lambda: moveNotification(treeviewNotifications, -1))
    btnBackward.place(x=480, y=365)

    treeviewNotifications.bind("<<TreeviewSelect>>", onTreeviewSelect)

    def moveNotification(treeview, direction):
        selected_item = treeview.selection()
        if not selected_item:
            messagebox.showinfo("Move Notification", "Please select a notification.")
            return

        current_index = treeview.index(selected_item)
        total_items = len(treeview.get_children())

        new_index = (current_index + direction) % total_items

        treeview.selection_set(treeview.get_children()[new_index])
        treeview.focus(treeview.get_children()[new_index])
        treeview.see(treeview.get_children()[new_index])

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
                panelUsers.destroy()
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
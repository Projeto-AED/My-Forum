from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import messagebox
from datetime import datetime, timedelta
import datetime
import os

fUsers = "files/users.txt"
fWaitingUsers = "files/waitingUsers.txt"
fCategories = "files/categories.txt"
fNotifications = "files/notifications.txt"
fPosts = "files/posts.txt"
fLikedPosts = "files/likedPosts.txt"
fComments = "files/comments.txt"

window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
window.geometry("1000x500")
window.title('my Forum')

# Main Page (With Image, Login, Registration and Leave Buttons)
def indexPage():
    # Action Window, where the User performs Actions
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
    btnNewPost = Button(userMenu, image=imgNewPost, width = 230 , height = 50, relief="sunken", compound=LEFT, text="New Post", font="Calibri, 11", command = lambda: newPostPanel(userName))
    btnNewPost.image = imgNewPost
    btnNewPost.place(x=5, y=100)

    imageViewPosts = Image.open("images\\viewPostsIMG.png")
    resizedViewPostsIMG = imageViewPosts.resize((50, 50))
    imgViewPosts = ImageTk.PhotoImage(resizedViewPostsIMG)
    btnViewPosts = Button(userMenu, image=imgViewPosts, width = 230 , height = 50, relief="sunken", compound=LEFT, text="View Posts", font="Calibri, 11", command = lambda: viewPostsPanel(userName))
    btnViewPosts.image = imgViewPosts
    btnViewPosts.place(x=5, y=180)

    imageLikedPosts = Image.open("images\\likedPostsIMG.png")
    resizedLikedPostsIMG = imageLikedPosts.resize((50, 50))
    imgLikedPosts = ImageTk.PhotoImage(resizedLikedPostsIMG)
    btnLikedPosts = Button(userMenu, image=imgLikedPosts, width = 230 , height = 50, relief="sunken", compound=LEFT, text="Liked Posts", font="Calibri, 11", command = lambda: likedPostsPanel(userName))
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

def newPostPanel(userName):
    userNewPostPanel = PanedWindow(window, width=750, height=450, relief="sunken")
    userNewPostPanel.place(x=250, y=50)

    inputPostPanel = PanedWindow(userNewPostPanel, width=730, height=280, bd="3", relief="sunken")
    inputPostPanel.place(x=10, y=10)

    def get_next_post_id():
        try:
            with open(fPosts, "r", encoding="utf-8") as posts_file:
                lines = posts_file.readlines()
                if lines:
                    last_post = lines[-1].split(";")
                    return int(last_post[0]) + 1
                else:
                    return 0
        except FileNotFoundError:
            return 0
        
    selected_file_path = None

    def selectFiles():
        nonlocal selected_file_path
        selected_file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])

    def postButtonClicked():
        nonlocal selected_file_path

        category = categoryVar.get()
        title = titleVar.get()
        message = messageText.get("1.0", "end-1c")

        if not category or not title or not message or not selected_file_path:
            messagebox.showerror("Error", "All inputs, including the PNG file, must be filled.")
            return

        post_id = get_next_post_id()

        date_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

        post_data = f"{post_id};{userName};{category};{title};{message};{selected_file_path};{date_time}\n"
        with open(fPosts, "a", encoding="utf-8") as posts_file:
            posts_file.write(post_data)

        updateTreeView()

        messagebox.showinfo("Success", "Post successfully created!")

    def updateTreeView():
        for item in treeviewPosts.get_children():
            treeviewPosts.delete(item)

        with open(fPosts, "r", encoding="utf-8") as posts_file:
            for line in posts_file:
                post_info = line.strip().split(";")
                if post_info[1] == userName:
                    treeviewPosts.insert("", "end", values=(post_info[3], post_info[2], post_info[6]))

    def onTreeviewSelect(event):
        selection = treeviewPosts.selection()
        if selection:
            item_values = treeviewPosts.item(selection[0], 'values')
            selected_title = item_values[0]

            with open(fPosts, "r", encoding="utf-8") as posts_file:
                for line in posts_file:
                    post_info = line.strip().split(";")
                    if post_info[3] == selected_title:
                        categoryVar.set(post_info[2])
                        titleVar.set(post_info[3])
                        messageText.delete(1.0, END)
                        messageText.insert(END, post_info[4])
                        nonlocal selected_file_path
                        selected_file_path = post_info[5]
                        break

    def removePost():
        selected_item = treeviewPosts.selection()
        if not selected_item:
            messagebox.showinfo("Remove Post", "Please select a post to remove.")
            return

        selected_values = treeviewPosts.item(selected_item, "values")
        if not selected_values:
            messagebox.showinfo("Remove Post", "Unable to retrieve post information.")
            return

        selected_title = selected_values[0]
        selected_date_time = selected_values[2]

        with open(fPosts, "r", encoding="utf-8") as posts_file:
            posts_list = posts_file.readlines()

        with open(fPosts, "w", encoding="utf-8") as posts_file:
            for line in posts_list:
                post_info = line.strip().split(";")
                post_title = post_info[3]
                post_date_time = post_info[6]
                if post_title != selected_title or post_date_time != selected_date_time:
                    posts_file.write(line)

        updateTreeView()
        clearBoxes()
        messagebox.showinfo("Remove Post", f"The post with title '{selected_title}' and date_time '{selected_date_time}' has been removed.")

    def clearBoxes():
        categoryVar.set(categories[0])
        titleVar.set("")
        messageText.delete("1.0", END)
        nonlocal selected_file_path
        selected_file_path = None

    def editPost():
        selected_item = treeviewPosts.selection()
        if not selected_item:
            messagebox.showinfo("Edit Post", "Please select a post to edit.")
            return

        selected_values = treeviewPosts.item(selected_item, "values")
        if not selected_values:
            messagebox.showinfo("Edit Post", "Unable to retrieve post information.")
            return

        selected_title = selected_values[0]
        selected_date_time = selected_values[2]

        with open(fPosts, "r", encoding="utf-8") as posts_file:
            posts_list = posts_file.readlines()

        with open(fPosts, "w", encoding="utf-8") as posts_file:
            for line in posts_list:
                post_info = line.strip().split(";")
                post_title = post_info[3]
                post_date_time = post_info[6]
                if post_title != selected_title or post_date_time != selected_date_time:
                    posts_file.write(line)

        postButtonClicked()
        updateTreeView()

        messagebox.showinfo("Edit Post", f"The post with title '{selected_title}' and Date '{selected_date_time}' has been edited successfully.")

    categories = []
    with open(fCategories, "r", encoding="utf-8") as file:
        categories = [line.strip() for line in file.readlines()]

    categoryLabel = Label(inputPostPanel, text="Select Category:", font=("Helvetica", 9))
    categoryLabel.place(x=20, y=20)

    categoryVar = StringVar()
    categoryCombobox = ttk.Combobox(inputPostPanel, values=categories, textvariable=categoryVar, state="readonly")
    categoryCombobox.place(x=150, y=20)
    categoryCombobox.current(0)

    titleLabel = Label(inputPostPanel, text="Title:", font=("Helvetica", 9))
    titleLabel.place(x=350, y=20)

    titleVar = StringVar()
    titleEntry = Entry(inputPostPanel, width=40, textvariable=titleVar)
    titleEntry.place(x=420, y=20)

    messageLabel = Label(inputPostPanel, text="Message:", font=("Helvetica", 9))
    messageLabel.place(x=20, y=60)

    messageText = Text(inputPostPanel, width=60, height=8)
    messageText.place(x=150, y=60)

    selectFilesButton = Button(inputPostPanel, text="Select PNG Files", command = selectFiles)
    selectFilesButton.place(x=150, y=200)

    postButton = Button(inputPostPanel,width=12, height=4, text="Post!", command = postButtonClicked)
    postButton.place(x=600, y=200)

    editButton = Button(inputPostPanel,width=12, height=4, text="Edit Post", command = editPost)
    editButton.place(x=500, y=200)

    clearButton = Button(inputPostPanel,width=12, height=4, text="Clear Boxes", command = clearBoxes)
    clearButton.place(x=400, y=200)

    removeButton = Button(userNewPostPanel,width=12, height=4, text="Delete Post", command = removePost)
    removeButton.place(x=510, y=330)

    myPostsTviewPanel = PanedWindow(userNewPostPanel, width=730, height=180, bd="3", relief="sunken")
    myPostsTviewPanel.place(x=10, y=300)

    treeviewPosts = ttk.Treeview(myPostsTviewPanel, columns=("Title", "Category", "date_time"), show="headings", height=5)
    treeviewPosts.heading("Title", text="Title")
    treeviewPosts.heading("Category", text="Category")
    treeviewPosts.heading("date_time", text="Date and Time")
    treeviewPosts.grid(column=0, row=0, sticky="nsew")

    treeviewPosts.column("Title", width=150)
    treeviewPosts.column("Category", width=100)
    treeviewPosts.column("date_time", width=100)

    vsbPosts = ttk.Scrollbar(myPostsTviewPanel, orient="vertical", command=treeviewPosts.yview)
    treeviewPosts.configure(yscrollcommand=vsbPosts.set)
    vsbPosts.grid(column=1, row=0, sticky="ns")

    myPostsTviewPanel.columnconfigure(0, weight=1)
    myPostsTviewPanel.rowconfigure(0, weight=1)

    treeviewPosts.bind("<<TreeviewSelect>>", onTreeviewSelect)

    updateTreeView()

def viewPostsPanel(userName):
    panelViewPosts = PanedWindow(window, width=750, height=450, relief="sunken")
    panelViewPosts.place(x=250, y=50)

    def readPosts():
        with open(fPosts, "r", encoding="utf-8") as postsFile:
            return postsFile.readlines()

    def displayPost(postIndex, postsList=None):
        if postsList is None:
            postsList = readPosts()

        if 0 <= postIndex < len(postsList):
            postInfo = postsList[postIndex].strip().split(";")

            postContent = f"Title: {postInfo[3]}\nCategory: {postInfo[2]}\nMessage: {postInfo[4]}\nAuthor: {postInfo[1]}\nDate and Time: {postInfo[6]}"
            postLabel.config(text=postContent)

            imagePath = postInfo[5]
            if imagePath.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                imagePost = Image.open(imagePath)
                resizedPostIMG = imagePost.resize((320, 170))
                imgPost = ImageTk.PhotoImage(resizedPostIMG)
                imageLabel.config(image=imgPost)
                imageLabel.image = imgPost
            else:
                imageLabel.config(image="")
                imageLabel.image = None
        
        # Code Regarding Comment Section:
        for item in commentsTreeview.get_children():
            commentsTreeview.delete(item)

        post_id = postInfo[0]

        with open(fComments, "r", encoding="utf-8") as commentsFile:
            for commentLine in commentsFile:
                commentInfo = commentLine.strip().split(";")
                if commentInfo[0] == post_id:
                    commentsTreeview.insert("", "end", values=(commentInfo[1], commentInfo[2]))

    def likePost():
        postsList = readPosts()
        if 0 <= currentPostIndex < len(postsList):
            postInfo = postsList[currentPostIndex].strip().split(";")
            post_id = postInfo[0]
            author = postInfo[1]

            with open(fLikedPosts, "r", encoding="utf-8") as liked_file:
                liked_posts = liked_file.readlines()

            for liked_post in liked_posts:
                liked_info = liked_post.strip().split(";")
                if liked_info[0] == post_id and liked_info[1] == author and liked_info[2] == userName:
                    messagebox.showinfo("Like Post", "You have already liked this post.")
                    return

            with open(fLikedPosts, "a", encoding="utf-8") as liked_file:
                liked_file.write(f"{post_id};{author};{userName}\n")

            messagebox.showinfo("Like Post", "Post liked successfully.")

    def nextPost():
        nonlocal currentPostIndex
        currentPostIndex = (currentPostIndex + 1) % len(readPosts())
        displayPost(currentPostIndex)

    def previousPost():
        nonlocal currentPostIndex
        currentPostIndex = (currentPostIndex - 1) % len(readPosts())
        displayPost(currentPostIndex)

    viewSinglePostPanel = PanedWindow(panelViewPosts, width=730, height=180, bd="3", relief="sunken")
    viewSinglePostPanel.place(x=10, y=10)

    btnForward = Button(panelViewPosts, text="Next\nPost", width=8, height=2, command=nextPost)
    btnForward.place(x=670, y=390)

    btnBackward = Button(panelViewPosts, text="Previous\nPost", width=8, height=2, command=previousPost)
    btnBackward.place(x=600, y=390)

    btnLikePost = Button(panelViewPosts, text="Like\nPost", width=8, height=2, command = likePost)
    btnLikePost.place(x=530, y=390)

    postLabel = Label(viewSinglePostPanel, text="", font=("Helvetica", 9), wraplength=380, justify="left")
    postLabel.place(x=10, y=10)

    imageLabel = Label(viewSinglePostPanel)
    imageLabel.place(x=390, y=0)

    commentsPostPanel = PanedWindow(panelViewPosts, width=510, height=240, bd="3", relief="sunken")
    commentsPostPanel.place(x=10, y=200)

    def addComment():
        comment_text = commentEntry.get("1.0", "end-1c").strip()
        if not comment_text:
            messagebox.showinfo("Add Comment", "Please enter a comment.")
            return

        postsList = readPosts()
        if 0 <= currentPostIndex < len(postsList):
            postInfo = postsList[currentPostIndex].strip().split(";")
            post_id = postInfo[0]

            with open(fComments, "a", encoding="utf-8") as comments_file:
                comments_file.write(f"{post_id};{userName};{comment_text}\n")

            commentsTreeview.insert("", "end", values=(userName, comment_text))

            messagebox.showinfo("Add Comment", "Comment added successfully.")
            commentEntry.delete("1.0", END)

    def onCommentSelected(event):
        selected_item = commentsTreeview.selection()
        if selected_item:
            values = commentsTreeview.item(selected_item, 'values')
            if values:
                selected_comment = values[1]
                commentEntry.delete("1.0", END)
                commentEntry.insert(END, selected_comment)

    def deleteComment():
        selected_item = commentsTreeview.selection()
        if selected_item:
            values = commentsTreeview.item(selected_item, 'values')
            if values:
                comment_author = values[0]
                if comment_author == userName:
                    commentsTreeview.delete(selected_item)

                    with open(fComments, "r", encoding="utf-8") as comments_file:
                        lines = comments_file.readlines()

                    with open(fComments, "w", encoding="utf-8") as comments_file:
                        deleted = False
                        for line in lines:
                            commentInfo = line.strip().split(";")
                            post_id = commentInfo[0]
                            if post_id == commentInfo[0] and commentInfo[1] == userName and commentInfo[2] == values[1]:
                                deleted = True
                                continue
                            comments_file.write(line)

                        if deleted:
                            messagebox.showinfo("Delete Comment", "Comment deleted successfully.")

    commentLabel = Label(commentsPostPanel, text="Comment:", font=("Helvetica", 9))
    commentLabel.place(x=10, y=10)

    commentEntry = Text(commentsPostPanel, width=52, height=3)
    commentEntry.place(x=80, y=10)

    addCommentButton = Button(commentsPostPanel, text="Add Comment", width=12, height=2, command=addComment)
    addCommentButton.place(x=400, y=70)

    deleteCommentButton = Button(commentsPostPanel, text="Delete Comment", width=12, height=2, command=deleteComment)
    deleteCommentButton.place(x=400, y=120)

    commentsTreeview = ttk.Treeview(commentsPostPanel, columns=("User", "Comment"), show="headings", height=6)
    commentsTreeview.heading("User", text="Author")
    commentsTreeview.heading("Comment", text="Comment")
    commentsTreeview.place(x=10, y=70)

    commentsTreeview.column("User", width=100)
    commentsTreeview.column("Comment", width=280)

    commentsTreeview.bind("<ButtonRelease-1>", onCommentSelected)

    filterPostsPanel = PanedWindow(panelViewPosts, width=220, height=180, bd="3", relief="sunken")
    filterPostsPanel.place(x=520, y=200)

    def applyFilters():
        selectedAuthor = authorComboBox.get()
        selectedCategory = categoryComboBox.get()
        selectedTimeFilter = timeFilterComboBox.get()

        postsList = readPosts()
        filteredPosts = []

        for post in postsList:
            postInfo = post.strip().split(";")
            post_author = postInfo[1]
            post_category = postInfo[2]
            post_date = datetime.datetime.strptime(postInfo[6], "%d-%m-%Y %H:%M")

            author_match = not selectedAuthor or selectedAuthor == post_author
            category_match = not selectedCategory or selectedCategory == post_category
            time_match = True

            if selectedTimeFilter:
                filter_date = datetime.datetime.now() - timedelta(days=1) if selectedTimeFilter == "< 1 day" else \
                    datetime.datetime.now() - timedelta(weeks=1) if selectedTimeFilter == "< 1 week" else \
                    datetime.datetime.now() - timedelta(weeks=4) if selectedTimeFilter == "< 1 month" else \
                    datetime.datetime.now() - timedelta(weeks=52) if selectedTimeFilter == "< 1 year" else None

                time_match = not filter_date or post_date >= filter_date

            if author_match and category_match and time_match:
                filteredPosts.append(post)

        if not filteredPosts:
            messagebox.showinfo("No Posts", "No posts match the selected filters.")
        else:
            displayPost(0, filteredPosts)

    def clearSelection():
        authorComboBox.set("")
        categoryComboBox.set("")
        timeFilterComboBox.set("")


    authorLabel = Label(filterPostsPanel, text="Post Author:", font=("Helvetica", 9))
    authorLabel.place(x=10, y=10)
    postAuthors = set(post[1] for post in [line.strip().split(";") for line in readPosts()])
    authorComboBox = ttk.Combobox(filterPostsPanel, values=list(postAuthors), state="readonly", width = 15)
    authorComboBox.place(x=85, y=10)

    categoryLabel = Label(filterPostsPanel, text="Category:", font=("Helvetica", 9))
    categoryLabel.place(x=10, y=40)
    categories = set(post[2] for post in [line.strip().split(";") for line in readPosts()])
    categoryComboBox = ttk.Combobox(filterPostsPanel, values=list(categories), state="readonly", width = 15)
    categoryComboBox.place(x=85, y=40)

    timeFilterLabel = Label(filterPostsPanel, text="Time Filter:", font=("Helvetica", 9))
    timeFilterLabel.place(x=10, y=70)
    timeFilterComboBox = ttk.Combobox(filterPostsPanel, values=["< 1 day", "< 1 week", "< 1 month", "< 1 year"], state="readonly", width = 15)
    timeFilterComboBox.place(x=85, y=70)

    applyButton = Button(filterPostsPanel, text="Apply", width=12, height=2, command = applyFilters)
    applyButton.place(x=10, y=115)

    clearSelectionButton = Button(filterPostsPanel, text="Clear Selection", width=12, height=2, command = clearSelection)
    clearSelectionButton.place(x=110, y=115)

    currentPostIndex = 0
    displayPost(currentPostIndex)

def likedPostsPanel(userName):
    panelLikedPosts = PanedWindow(window, width=750, height=450, relief="sunken")
    panelLikedPosts.place(x=250, y=50)

    def readLikedPosts():
        with open(fLikedPosts, "r", encoding="utf-8") as likedFile:
            return likedFile.readlines()

    def readPosts():
        with open(fPosts, "r", encoding="utf-8") as postsFile:
            return postsFile.readlines()

    def displayLikedPost(postIndex, likedPostsList=None):
        if likedPostsList is None:
            likedPostsList = readLikedPosts()

        if 0 <= postIndex < len(likedPostsList):
            likedPostInfo = likedPostsList[postIndex].strip().split(";")
            post_id = likedPostInfo[0]

            postsList = readPosts()
            postInfo = next((post.strip().split(";") for post in postsList if post.startswith(post_id)), None)

            if postInfo and likedPostInfo[2] == userName:  # Ensure the like is from the specified user
                postContent = f"Title: {postInfo[3]}\nCategory: {postInfo[2]}\nMessage: {postInfo[4]}\nAuthor: {postInfo[1]}\nDate and Time: {postInfo[6]}"
                postLabel.config(text=postContent)

                imagePath = postInfo[5]
                if imagePath.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    imagePost = Image.open(imagePath)
                    resizedPostIMG = imagePost.resize((320, 170))
                    imgPost = ImageTk.PhotoImage(resizedPostIMG)
                    imageLabel.config(image=imgPost)
                    imageLabel.image = imgPost
                else:
                    imageLabel.config(image="")
                    imageLabel.image = None

                # Code Regarding Comment Section:
                for item in commentsTreeview.get_children():
                    commentsTreeview.delete(item)

                currentDisplayedPostId = postInfo[0]

                with open(fComments, "r", encoding="utf-8") as commentsFile:
                    for commentLine in commentsFile:
                        commentInfo = commentLine.strip().split(";")
                        if commentInfo[0] == currentDisplayedPostId:
                            commentsTreeview.insert("", "end", values=(commentInfo[1], commentInfo[2]))

    def nextLikedPost():
        nonlocal currentLikedPostIndex
        likedPostsList = readLikedPosts()

        while currentLikedPostIndex < len(likedPostsList) - 1:
            currentLikedPostIndex = (currentLikedPostIndex + 1) % len(likedPostsList)
            if shouldDisplayLikedPost(likedPostsList[currentLikedPostIndex]):
                break

        displayLikedPost(currentLikedPostIndex)

    def previousLikedPost():
        nonlocal currentLikedPostIndex
        likedPostsList = readLikedPosts()

        while currentLikedPostIndex > 0:
            currentLikedPostIndex = (currentLikedPostIndex - 1) % len(likedPostsList)
            if shouldDisplayLikedPost(likedPostsList[currentLikedPostIndex]):
                break

        displayLikedPost(currentLikedPostIndex)

    def shouldDisplayLikedPost(likedPostInfo):
        post_id, _, liked_user = likedPostInfo.strip().split(";")
        postsList = readPosts()

        postInfo = next((post.strip().split(";") for post in postsList if post.startswith(post_id)), None)
        return postInfo is not None and liked_user == userName
    
    def unlikePost():
        likedPostsList = readLikedPosts()

        if 0 <= currentLikedPostIndex < len(likedPostsList):
            post_id, author, liked_user = likedPostsList[currentLikedPostIndex].strip().split(";")

            likedPostsList.pop(currentLikedPostIndex)

            with open(fLikedPosts, "w", encoding="utf-8") as likedFile:
                likedFile.writelines(likedPostsList)

            messagebox.showinfo("Unlike Post", "Post unliked successfully!")

            nextLikedPost()

    viewSinglePostPanel = PanedWindow(panelLikedPosts, width=730, height=180, bd="3", relief="sunken")
    viewSinglePostPanel.place(x=10, y=10)

    btnForward = Button(panelLikedPosts, text="Next\nLiked Post", width=12, height=4, command=nextLikedPost)
    btnForward.place(x=640, y=365)

    btnBackward = Button(panelLikedPosts, text="Previous\nLiked Post", width=12, height=4, command=previousLikedPost)
    btnBackward.place(x=530, y=365)

    btnUnlikePost = Button(panelLikedPosts, text="Unlike\nPost", width=12, height=4, command = unlikePost)
    btnUnlikePost.place(x=640, y=200)

    postLabel = Label(viewSinglePostPanel, text="", font=("Helvetica", 9), wraplength=380, justify="left")
    postLabel.place(x=10, y=10)

    imageLabel = Label(viewSinglePostPanel)
    imageLabel.place(x=390, y=0)

    commentsPostPanel = PanedWindow(panelLikedPosts, width=510, height=240, bd="3", relief="sunken")
    commentsPostPanel.place(x=10, y=200)

    commentsTreeview = ttk.Treeview(commentsPostPanel, columns=("User", "Comment"), show="headings", height=9)
    commentsTreeview.heading("User", text="Author")
    commentsTreeview.heading("Comment", text="Comment")
    commentsTreeview.place(x=10, y=10)

    commentsTreeview.column("User", width=100)
    commentsTreeview.column("Comment", width=380)

    currentLikedPostIndex = 0
    displayLikedPost(currentLikedPostIndex)

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

#Launch My Forum!
indexPage()
window.mainloop()
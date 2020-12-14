from tkinter import *
from tkinter import messagebox
from ClientSide import ClientScript as CS

""""
BELOW ARE THE CONSTANT VARIABLES FROM THE SERVER
"""

localClient = CS.client


class Person:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Users:
    def __init__(self):
        self.names = []

    def add_user(self, person):
        self.names.append(person)

    def print_users(self):
        for i in range(0, len(self.names)):
            print(self.names[i].username)


users = Users()


class Login:
    def __init__(self):
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        self.showing_password = False

        self.username_label = Label(self.root, text="Username").pack()

        self.username_entry = Entry(self.root)
        self.username_entry.pack()

        self.password_label = Label(self.root, text="Password").pack()

        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()

        def login_request():
            self.login_call()

        self.login_button = Button(self.root, text="Login", command=login_request)
        self.login_button.pack()

        def show_password_request():
            self.show_password_call()

        self.show_password_button = Button(self.root, text="Show password", command=show_password_request)
        self.show_password_button.pack()

        def register_request():
            self.register_call()

        self.register_button = Button(self.root, text="Register", command=register_request)
        self.register_button.pack()

        self.root.mainloop()

    def login_call(self):
        for i in range(0, len(users.names)):


            self.current_user = users.names[i].username
            self.current_password = users.names[i].password
            print(self.current_user)

            if self.username_entry.get() == "Admin":
                if self.password_entry.get() == "Admin":
                    print("Admin has been accessed")
                    self.root.destroy()
                    task = localClient.send("ADMIN")
                    break

            elif self.username_entry.get() == self.current_user:
                if self.password_entry.get() == self.current_password:
                    print(self.username_entry.get(), "has logged in")
                    self.root.destroy()
                    home = Home(i)
                    break

        else:
            print("Login Error")
            messagebox.showinfo("Error", "Username or password is incorrect")

    def show_password_call(self):
        if self.showing_password:
            self.password_entry.config(show="*")
            self.showing_password = False
            self.show_password_button.config(text="Show Button")
        else:
            self.password_entry.config(show="")
            self.showing_password = True
            self.show_password_button.config(text="Hide Password")

    def register_call(self):
        self.root.destroy()
        register = Register()

    def callback(self):
        if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
            self.root.destroy()
            localClient.send(localClient.disconnect_message)
            sys.exit(0)


class Home:
    def __init__(self, user_position):
        self.user_position = user_position

        self.home_win = Tk()

        self.welcome_label = Label(self.home_win, text="Welcome " + users.names[user_position].username)
        self.welcome_label.pack()

        self.home_win.mainloop()


class Register:
    def __init__(self):
        self.register_win = Tk()

        self.showing_password = False

        self.email_signup_label = Label(self.register_win, text="Enter email:")
        self.email_signup_label.pack()

        self.email_signup_entry = Entry(self.register_win)
        self.email_signup_entry.pack()

        self.username_signup_label = Label(self.register_win, text="Enter username:")
        self.username_signup_label.pack()

        self.username_signup_entry = Entry(self.register_win)
        self.username_signup_entry.pack()

        self.password_signup_label = Label(self.register_win, text="Enter password: ")
        self.password_signup_label.pack()

        self.password_signup_entry = Entry(self.register_win, show="*")
        self.password_signup_entry.pack()

        self.password_check_signup_label = Label(self.register_win, text="Verify password: ")
        self.password_check_signup_label.pack()

        self.password_signup_verify_entry = Entry(self.register_win, show="*")
        self.password_signup_verify_entry.pack()

        def register_button_request():
            self.register_button_call()

        self.register_button = Button(self.register_win, text="Register", command=register_button_request)
        self.register_button.pack()

        def show_password_request():
            self.shown_password_button()

        self.show_password_button = Button(self.register_win, text="Show password", command=show_password_request)
        self.show_password_button.pack()

        def return_call_request():
            self.return_call()

        self.return_button = Button(self.register_win, text="Return", command=return_call_request)
        self.return_button.pack()

        self.register_win.mainloop()

    def register_button_call(self):
        if len(self.email_signup_entry.get()) >= 10:

            if len(self.username_signup_entry.get()) >= 5:

                if len(self.password_signup_entry.get()) > 8:

                    if self.password_signup_entry.get() == self.password_signup_verify_entry.get():

                        for i in range(0, len(users.names)):

                            self.current_username = users.names[i].username
                            self.current_email = users.names[i].email

                            if self.username_signup_entry == self.current_username or self.email_signup_entry == self.current_email:
                                print("Error")
                                messagebox.showinfo("Error", "Username or Email is already taken")
                                break

                            else:
                                person = Person(self.username_signup_entry.get(),
                                                self.email_signup_entry.get(),
                                                self.password_signup_entry.get())

                                messagebox.showinfo("Nice", "You have signed up")
                                users.add_user(person)
                                self.register_win.destroy()
                                login_new = Login()

                    else:
                        print("error")
                        messagebox.showinfo("Error", "Passwords do not match")

                elif len(self.password_signup_entry.get()) == 0:
                    print("error")
                    messagebox.showinfo("Error", "Please enter a password")

                else:
                    print("error")
                    messagebox.showinfo("Error", "Password needs more than 9 characters")

            elif len(self.username_signup_entry.get()) == 0:
                print("error")
                messagebox.showinfo("Error", "Please enter a username")

            else:
                print("error")
                messagebox.showinfo("Error", "Username needs more than 5 characters")

        elif len(self.email_signup_entry.get()) == 0:
            print("error")
            messagebox.showinfo("Error", "Please enter an email")

        else:
            print("error")
            messagebox.showinfo("Error", "Your email isn't valid")

    def shown_password_button(self):
        if self.showing_password:
            self.password_signup_verify_entry.config(show="*")
            self.showing_password = False
            self.show_password_button.config(text="Show Button")
        else:
            self.password_signup_verify_entry.config(show="")
            self.showing_password = True
            self.show_password_button.config(text="Hide Password")

    def return_call(self):
        self.register_win.destroy()
        login = Login()


if localClient.connected:
    login = Login()

from backend import services
from tkinter import *

app = Tk()
app.title("Authentication")
app.geometry("500x400")

label = Label(app, text="Login", font=("Arial", 24))
label.pack(side=TOP, pady=40)

username_frame = Frame(app)
username_frame.pack(pady=(10, 10))
Label(username_frame, text="Username:", font=("Arial", 16)).pack(side=LEFT, padx=20)
username_field = Entry(username_frame, font=("Arial", 16))
username_field.pack(padx=20)

password_frame = Frame(app)
password_frame.pack(pady=(40, 10))
Label(password_frame, text="Password:", font=("Arial", 16)).pack(side=LEFT, padx=20)
password_field = Entry(password_frame, show="*", font=("Arial", 16))
password_field.pack(padx=20)


def authenticate():
    services.authenticate(username_field.get(), password_field.get())


submit_button = Button(app, text="Login", font=("Arial", 16), compound=CENTER, fg="white", bg="blue", height=2, width=10, padx=15, pady=5, border=0, command=authenticate)
submit_button.pack(pady=(40,0))



app.mainloop()

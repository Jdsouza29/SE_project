from pathlib import Path
import re

from tkinter import Toplevel, Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
from controller import *
from PIL import ImageTk, Image

# from ..main_window.main import mainWindow
# from ..createuser.createUser import CreateUser

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def CreateUser():
    create()
    return
class create(Toplevel):

    def check_create(self):
        global user
        patt = re.compile("^(?=.*[a-z])(?=.*\d)(?=.*[^\da-zA-Z]).{8,}$")
        if len(self.username.get())<5 or len(self.password.get())<8:
            messagebox.showerror(
                title="Invalid Credentials",
                message="The lenght of username and password should be more than 7",
            )
        # print(patt.match(self.password.get()),self.password.get())
        elif (patt.match(self.password.get())==None):
            messagebox.showerror(
                title="Invalid Password",
                message="Password should be 8 characters long and should have at least\n 1 lowercase, 1 number",
            )
        elif checkUser(self.username.get().lower(),self.password.get()):
            messagebox.showerror(
                title="Invalid",
                message="Username and password already exists",
            )
        else:
            createuser(self.username.get().lower(),self.password.get())
            self.destroy()
            return
            


    def __init__(self, *args, **kwargs):

        Toplevel.__init__(self, *args, **kwargs)

        self.title("Login - Conference Book")

        self.geometry("780x550")
        self.configure(bg="#5E95FF")

        self.canvas = Canvas(
            self,
            bg="#5E95FF",
            height=550,
            width=780,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            150.0, 10.0, 630.0, 540.0, fill="#FFFFFF", outline=""
        )

        entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(400.0, 331.0, image=entry_image_1)
        self.password = Entry(self.canvas, 
                                bd=0, 
                                bg="#EFEFEF", 
                                highlightthickness=0,
                                font=("Montserrat Bold", 16 * -1),
                                foreground="#777777",
                                show="•")
        self.password.place(x=225.0, y=311.0, width=306.0, height=22.0)

        entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(400.0, 229.0, image=entry_image_2)
        self.username = Entry(self.canvas, 
                                bd=0, 
                                bg="#EFEFEF", 
                                highlightthickness=0,
                                font=("Montserrat Bold", 16 * -1),
                                foreground="#777777",
                                )
        self.username.place(x=225.0, y=209.0, width=306.0, height=22.0)

        self.canvas.create_text(
            220.0,
            276.0,
            anchor="nw",
            text="Password",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        self.canvas.create_text(
            220.0,
            171.0,
            anchor="nw",
            text="Username",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )

        button_image_3 = ImageTk.PhotoImage(Image.open(relative_to_assets("button_3.jpg"))) 
        button_3 = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.check_create,
            relief="flat"
        )
        button_3.place(x=300.0,y=400.0,width=190.0, height=48.0)

        self.canvas.create_text(
            220.0,
            75.0,
            anchor="nw",
            text="Enter Username and Password",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )

        self.canvas.create_text(
            220.0,
            104.0,
            anchor="nw",
            text="Username and password should be atleast 8 characters long",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )
        
        self.canvas.create_text(
            220.0,
            133.0,
            anchor="nw",
            text="Password should have numbers and letters",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )
        print("HERE")
        self.resizable(False, False)
        self.mainloop()
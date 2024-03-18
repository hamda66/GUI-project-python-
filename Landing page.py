#Landing page

import tkinter
import os
import customtkinter

customtkinter.set_appearance_mode("light")

customtkinter.set_default_color_theme("green")

def gologin():
    print("do nothing")

def signuppage():
    print("do nothing")


root = customtkinter.CTk()

root.geometry("300x150")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

loginbtn = customtkinter.CTkButton(master=frame, text="LOGIN HERE", command=gologin)
loginbtn.pack(padx=12, pady=10)

signup = customtkinter.CTkButton(master=frame, text="SIGN UP HERE", command=signuppage)
signup.pack(padx=12,pady=10)

root.mainloop()




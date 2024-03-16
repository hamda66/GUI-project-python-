#Landing page

import tkinter
import os
import customtkinter

customtkinter.set_appearance_mode("light")

customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

loginbtn = customtkinter.CTkButton(master=root, text="LOGIN HERE", command=gologin)
loginbtn.pack(padx=12, pady=10)



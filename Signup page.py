#Signup page
import os
import fileinput
import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("blue")

root= customtkinter.CTk()

root.geometry("700x700")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=20, pady=70, fill="both", expand=True)

firstname = customtkinter.CTkEntry(master=frame, placeholder_text="First Name")
firstname.pack(padx=12 , pady=10)

#name = customtkinter.CTkLabel()



root.mainloop()
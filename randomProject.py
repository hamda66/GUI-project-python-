import os
import fileinput
import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    if input1 == "user1":
        print("CORRECT")
    else:
        print("INCORRECT")       
   # print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login")

label.pack(pady=12, padx=10)

input1 = customtkinter.CTkEntry(master=frame, placeholder_text="username") 
input1.pack(padx=12, pady=10)

input2 = customtkinter.CTkEntry(master= frame, placeholder_text="Password", show="*")
input2.pack(padx=12, pady=10)

button = customtkinter.CTkButton(master=frame,text="login", command=login)
button.pack(padx=12, pady=10)

Checkbox = customtkinter.CTkCheckBox(master=frame, text="remember me")
Checkbox.pack(padx=12, pady=10)

root.mainloop()


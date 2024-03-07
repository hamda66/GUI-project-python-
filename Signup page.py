#Signup page
import os
import fileinput
import tkinter
import customtkinter
from tkinter import filedialog

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("blue")

root= customtkinter.CTk()

root.geometry("700x450")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=50, pady=30, fill="both", expand=True)

Signuppagelb = customtkinter.CTkLabel(master=frame, text="Sign up", text_color="red", font=("Arial", 40) ) 
Signuppagelb.pack()

firstname = customtkinter.CTkLabel(master=frame, text="First name")
firstname.pack()
firstnameEnter = customtkinter.CTkEntry(master=frame, placeholder_text="Enter First Name")
firstnameEnter.pack(padx=12 , pady=10)

Lastname = customtkinter.CTkLabel(master=frame, text="Last Name")
Lastname.pack()
lastnameEnter = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Last Name")
lastnameEnter.pack()

Email=customtkinter.CTkLabel(master=frame, text="Email")
Email.pack()
EmailEnter = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Email")
EmailEnter.pack()

Password = customtkinter.CTkLabel(master=frame, text="Password")
Password.pack()
PasswordEnter = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
PasswordEnter.pack()

def cred():
    print ("Login saved!")
     
     savecred = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Text files","*.txt"),("All files","*.*")])
    if savecred:
       try:
          with open(savecred,'w') as file:
             file_content = firstnameEnter.get("1.0","end-1c")
 
    with open("usercred.txt","a") as targetfile:
        targetfile.write(f"{firstnameEnter.get()},{lastnameEnter.get()},{EmailEnter.get()},{PasswordEnter.get()}")
        targetfile.write("\n")
        
Signupbtn = customtkinter.CTkButton(master=frame, text="Sign up", command="cred")
Signupbtn.pack()

root.mainloop()
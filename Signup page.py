#Signup page
import os
import fileinput
import tkinter
import customtkinter

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("blue")

root= customtkinter.CTk()

root.geometry("500x350")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=20, pady=70, fill="both", expand=True)

Signuppagelb = customtkinter.CTkLabel(master=frame, text="Sign up", text_color="red", font=("Arial", 25) ) 

firstname = customtkinter.CTkLabel(master=frame, text="First name")
firstname.pack()
firstnameEnter = customtkinter.CTkEntry(master=frame, placeholder_text="Enter First Name")
firstnameEnter.pack(padx=12 , pady=10)

Lastname = customtkinter.CTkLabel(master=frame, text="Last Name")
Lastname.pack()
lastnameEnter = customtkinter.CTkEntry(master=frame, placeholder_text="Enter Last Name")
lastnameEnter.pack()

#name = customtkinter.CTkLabel()



root.mainloop()
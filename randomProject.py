import os
import fileinput
import tkinter
import customtkinter

#inputCVS = input("Input CVS File: ")
Filepath = "C:\\Users\\user\\Downloads\\"
#filename = Filepath +inputCVS
 

## for line in fileinput.input(Filepath+filename):
##    print(line, end='')
#####make a gui version of this

#root = tkinter.Tk()
#label = tkinter.Label(root, )
#label.pack()

customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)
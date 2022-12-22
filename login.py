from PIL import Image, ImageTk
import tkinter
import requests
import customtkinter
# import psycopg2
from tkinter import messagebox
import os, time
import tkintermapview


# def query():
#     #Configure and connect to postgres
#     conn = psycopg2.connect(
#         host = "127.0.0.1",
#         database = "AircraftDb",
#         user = "akobiir",
#         password = "1234",
#         port = "8080",
#         email = "akobir@gmail.com"
#     )

#     #Create a cursor
#     c = conn.cursor()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root_tk = customtkinter.CTk()
root_tk.geometry("720x480")
root_tk.title("Login Page")
    

def login():
    input = f'http://{entry_server.get()}/login'
    request = requests.post(input, 
                            json={
                                "email": entry_email.get(),
                                "password": entry_password.get()
                            })
    print(request.text)
    result = request.json()
    try:
        token = result["token"]
        print(token)
        root_tk.destroy()
    except:
        messagebox.showerror(title="Error", message="Invalid Login")
        app.destroy()       
       
        

frame = customtkinter.CTkFrame(master=root_tk)
frame.pack(pady=0, padx=0, fill="both", expand=True)

# my_image = customtkinter.CTkImage(light_image=Image.open("/home/akobir/Development/Aircraft_Communication/iut-logo-blue.png"), size=(30, 30))
# button = customtkinter.CTkButton(root_tk, image=my_image)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("SF Pro", 24))
label.pack(pady=40, padx=15) 

entry_server = customtkinter.CTkEntry(master=frame, placeholder_text="IP", width=160, height=40, corner_radius=0)
entry_server.pack(padx=10, pady=12)

entry_email = customtkinter.CTkEntry(master=frame, placeholder_text = "Email", width=160, height=40, corner_radius=0)
entry_email.pack(padx=10, pady=12)

entry_password = customtkinter.CTkEntry(master=frame, placeholder_text = "Password", width=160, height=40, show="*", corner_radius=0)
entry_password.pack(padx=10, pady=12)

button = customtkinter.CTkButton(master=frame, text="Login", command=login, corner_radius=20, height=30, width=100)
button.pack(padx=10, pady=12)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(padx=10, pady=12)


root_tk.mainloop()

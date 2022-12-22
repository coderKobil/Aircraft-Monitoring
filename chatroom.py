import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("900x600")
root.title("Chatroom")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1,  weight=1)

frame = customtkinter.CTkFrame(root)
frame.pack(padx=0, pady=0, fill='both', expand=True)

textbox = customtkinter.CTkTextbox(frame, width=750, height=500)
textbox.grid(row=0, column=0, padx=10, pady=10)
#textbox.configure(state="disabled") #read-only state

scrollbar = customtkinter.CTkScrollbar(frame, command=textbox.yview, corner_radius=0, hover=True)
scrollbar.grid(row=0, column=1, padx=10, pady=10, sticky="ns")

textbox.configure(yscrollcommand=scrollbar.set)

def send():
    send = "You -> " + entry.get()
    textbox.insert(tk.END, "\n" + send)
 
    user = entry.get().lower()
 
    if (user == "hello"):
        textbox.insert(tk.END, "\n" + "Dispatcher -> Hi there, how can I help?")
 
    elif (user == "hi" or user == "hii" or user == "hiiii"):
        textbox.insert(tk.END, "\n" + "Dispatcher -> Hi there, what can I do for you?")
 
    elif (user == "how are you"):
        textbox.insert(tk.END, "\n" + "Dispatcher -> fine! and you")
 
    elif (user == "fine" or user == "i am good" or user == "i am doing good"):
        textbox.insert(tk.END, "\n" + "Dispatcher -> Great! how can I help you.")
 
    elif (user == "thanks" or user == "thank you" or user == "now its my time"):
        textbox.insert(tk.END, "\n" + "Dispatcher -> My pleasure !")
 
    elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
        textbox.insert(tk.END, "\n" + "Dispatcher -> We have coffee and tea")
 
    elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
        textbox.insert(
            END, "\n" + "Dispatcher -> What did the buffalo say when his son left for college? Bison.! ")
 
    elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
        textbox.insert(tk.END, "\n" + "Dispatcher -> Have a nice day!")
 
    else:
        textbox.insert(tk.END, "\n" + "Dispatcher -> Sorry! I didn't understand that")
 
    entry.delete(0, tk.END)

entry = customtkinter.CTkEntry(frame, placeholder_text="Type here...", width=670, height=40, corner_radius=0)
entry.grid(column=0, row=1, padx=5, pady=10)

send = customtkinter.CTkButton(frame, text="Send", command=send, width=100, height=40)
send.grid(column=1, row=1, padx=10, pady=10)


if __name__=="__main__":
    root.mainloop()
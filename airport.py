from tkinter import *
import requests
import random
token = "4d1bfa17b63fae0862f5ede36a209055"
 
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=35, fg='black',
                               font=('Arial',12,'italic'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
 
# take the data
code = input("CODE AIRPORT:")
req = requests.get(f'http://192.168.43.80/api/{token}/airports/{code}')
print(req.text)
response = req.json()

lst = [('Airport Name', response["name"]),
       ('Aircraft Code', response["code"]),
       ('Location', response["location"]),
       ('Weather', str(response["weather"])),
       ("Free Runways", random.randint(5, 15)),
       ]

  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
  
# create root window
root = Tk()
t = Table(root)
root.mainloop()
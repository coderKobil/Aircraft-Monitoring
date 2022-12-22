from tkinter import *
import requests
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
code = input("CODE AIRCRAFT:")
req = requests.get(f'http://192.168.43.80/api/{token}/aircrafts/{code}')
print(req.text)
response = req.json()

lst = [('Registration Number', response["regNumber"]),
       ('Aircraft Type', response["aircraftType"]),
       ('Coordinates', response["coordinates"]),
       ('Distance Flight', str(response["distanceFlight"]) + " in km"),
       ('Airport From', response["AirportFrom"]["name"]),
       ('Airport From Code', response["AirportFrom"]["code"]),
       ('Airport From Location', response["AirportFrom"]["location"]),
       ('Airport From Weather', response["AirportFrom"]["weather"]),
       ('Airport To', response["AirportTo"]["name"]),
       ('Airport To Code', response["AirportTo"]["code"]),
       ('Airport To Location', response["AirportTo"]["location"]),
       ('Airport To Weather', response["AirportTo"]["weather"])]

  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
  
# create root window
root = Tk()
t = Table(root)
root.mainloop()
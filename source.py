import tkinter
import tkintermapview
import customtkinter
import time
import os
from PIL import Image, ImageTk
from login import *


class App(customtkinter.CTk):

    APP_NAME = "Aircraft Monitoring"
    WIDTH = 1080
    HEIGHT = 720
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)
        #self.iconbitmap("/Aircraft-Monitoring/Images/favicon.ico")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Control-q>", self.on_closing)
        self.bind("<Control-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []

        #  create two CTkFrames ==

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # self.frame_left = customtkinter.CTkFrame(
        #     master=self, width=302, corner_radius=0)
        # self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1,
                              pady=0, padx=0, sticky="nsew")

        # ============ frame_left ============

        #self.frame_left.grid_rowconfigure(2, weight=1)
        

        # ============ frame_right ============

        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = tkintermapview.TkinterMapView(
            self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0,
                             columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="type address", corner_radius=0)
        self.entry.grid(row=0, column=0, sticky="we", padx=(10, 0), pady=12)
        self.entry.bind("<Return>", self.search_event)
        
        
        label = customtkinter.CTkLabel(master=self.frame_right, text="", font=("SF Pro", 24), anchor='e')
        label.grid(row=0, column=2, padx=0)

        def clock():
            hour = time.strftime("%H")
            minute = time.strftime("%M")
            label.configure(text=hour + ":" + minute)
        clock()
        

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Search",
                                                width=90,
                                                command=self.search_event)
        self.button_5.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)

        # Set default values
        self.map_widget.set_address("Uzbekistan")
        self.map_widget.set_position(41.3775, 64.5853)
        
        #Images here
        current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
        plane_image = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "icons8-airplane-48.png")))
        plane_image_1 = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "icons8-airplane-48 (1).png")))
        plane_image_2 = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "icons8-airplane-48 (2).png")))
        plane_image_3 = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "icons8-airplane-48 (3).png")))
        tash_airport = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "Tashkent_airport.jpg")).resize((100,100)))
        nav_airport = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "navoi_airport.jpg")).resize((100,100)))
        fer_airport = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "ferghana.webp")).resize((100,100)))
        nuk_airport = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "nukus.webp")).resize((100,100)))
        nam_airport = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "nam_airport.jpg")).resize((100,100)))
        ter_airport = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "termez_air.jpg")).resize((100,100)))
        urg_airport = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "urgench.jpg")).resize((100,100)))
        bukh_airport = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "bukhara.jpg")).resize((100,100)))
        sam_airport = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "samarkand.jpg")).resize((100,100)))
        and_airport = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "Images", "andijan.jpg")).resize((100,100)))
        
        #markers here
        marker_1 = self.map_widget.set_marker(41.2625, 69.2662, text='Tashkent Airport', font=("SF Pro", 7), image=tash_airport, image_zoom_visibility=[8,20])
        marker_2 = self.map_widget.set_marker(40.12264015785264, 65.17752751105178, text='Novoiy Airport', font=("SF Pro", 7), image=nav_airport, image_zoom_visibility=[8,20])
        marker_3 = self.map_widget.set_marker(40.37697369793979, 71.75265515560736, text='Ferghana Airport', font=("SF Pro", 7), image=fer_airport, image_zoom_visibility=[8,20])
        marker_4 = self.map_widget.set_marker(42.482381776487664, 59.61552454426035, text='Nukus Airport', font=("SF Pro", 7), image=nuk_airport, image_zoom_visibility=[8,20])
        marker_5 = self.map_widget.set_marker(40.98483855072645, 71.57300075031908, text='Namangan Airport', font=("SF Pro", 7), image=nam_airport, image_zoom_visibility=[8,20])
        marker_6 = self.map_widget.set_marker(37.27980999943849, 67.32017192709743, text='Termez International Airport', font=("SF Pro", 7), image=ter_airport, image_zoom_visibility=[8,20])
        marker_7 = self.map_widget.set_marker(41.58458979681407, 60.643375947991515, text='Urgench Interantional Airport', font=("SF Pro", 7), image=urg_airport, image_zoom_visibility=[8,20])
        marker_8 = self.map_widget.set_marker(39.76022182936773, 64.47549246113964, text='Bukhara International Airport', font=("SF Pro", 7), image=bukh_airport, image_zoom_visibility=[8,20])
        marker_9 = self.map_widget.set_marker(39.69934881990928, 66.98414321274417, text='Samarqand International Airport', font=("SF Pro", 7), image=sam_airport, image_zoom_visibility=[8,20])
        marker_10 = self.map_widget.set_marker(40.73910843722989, 72.31337086266667, text='Andijan Airport', font=("SF Pro", 7), image=and_airport, image_zoom_visibility=[8,20])
        #marker_11 = self.map_widget.set_marker(deg_x, deg_y)
        
        flight_marker = self.map_widget.set_marker(40.656322, 66.868303, icon=plane_image)
        flight_marker_1 = self.map_widget.set_marker(41.852002, 62.627580, icon=plane_image_1)
        flight_marker_2 = self.map_widget.set_marker(39.975892, 65.549944, icon=plane_image_2)
        flight_marker_3 = self.map_widget.set_marker(40.795964, 70.889299, icon=plane_image_3)
        #flight_marker_4 = self.map_widget.set_marker(40.656322, 66.868303, icon=plane_image)
        
        #polygon
        #polygon = self.map_widget.set_polygon(41.2625, 69.2662)

    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()

app = App()
app.start()
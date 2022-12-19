# import tkinter
# import tkintermapview
# import customtkinter


# # Modes: system (default), light, dark
# customtkinter.set_appearance_mode("dark")
# # Themes: blue (default), dark-blue, green
# customtkinter.set_default_color_theme("dark-blue")

# # create CTk window like you do with the Tk window
# root = customtkinter.CTk()
# root.title("Aircraft Monitoring")
# root.iconbitmap("Aircraft-Monitoring/Images/favicon.ico")
# root.geometry("1200x720")


# # create map widget
# map_widget = tkintermapview.TkinterMapView(
#     root, width=1200, height=720, corner_radius=0)
# map_widget.place(relx=0.6, rely=0.6, anchor=tkinter.CENTER)


# # Tashkent, Uzbekistan
# map_widget.set_position(41.297659604019294, 69.2564965072215)
# map_widget.set_zoom(10)
# # def button_function():
# #   print("button pressed")


# # Use CTkButton instead of tkinter Button
# # button = customtkinter.CTkButton(
# #    master=app, text="CTkButton", command=button_function)
# # button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# root.mainloop()

import customtkinter
from tkintermapview import TkinterMapView

customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):

    APP_NAME = "Aircraft Monitoring"
    WIDTH = 1200
    HEIGHT = 720

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Command-q>", self.on_closing)
        self.bind("<Command-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []

        # ============ create two CTkFrames ============

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=302, corner_radius=0, fg_color=None)
        self.frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

        self.frame_right = customtkinter.CTkFrame(master=self, corner_radius=0)
        self.frame_right.grid(row=0, column=1, rowspan=1,
                              pady=0, padx=0, sticky="nsew")

        # ============ frame_left ============

        self.frame_left.grid_rowconfigure(2, weight=1)

        # ============ frame_right ============

        self.frame_right.grid_rowconfigure(1, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=0)
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=0)
        self.frame_right.grid_columnconfigure(2, weight=1)

        self.map_widget = TkinterMapView(self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0,
                             columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(12, 0), pady=12)
        self.entry.bind("<Return>", self.search_event)

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Search",
                                                width=90,
                                                command=self.search_event)
        self.button_5.grid(row=0, column=1, sticky="w", padx=(12, 0), pady=12)

        # Set default values
        self.map_widget.set_address("Tashkent")

    def search_event(self, event=None):
        self.map_widget.set_address(self.entry.get())

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()

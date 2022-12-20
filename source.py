import tkinter
import tkintermapview
import customtkinter


class App(customtkinter.CTk):

    APP_NAME = "Aircraft Monitoring"
    WIDTH = 800
    HEIGHT = 480

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(str(App.WIDTH) + "x" + str(App.HEIGHT))
        self.minsize(App.WIDTH, App.HEIGHT)
        self.iconbitmap("Aircraft-Monitoring/Images/favicon.ico")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.bind("<Control-q>", self.on_closing)
        self.bind("<Control-w>", self.on_closing)
        self.createcommand('tk::mac::Quit', self.on_closing)

        self.marker_list = []

        #  create two CTkFrames ==

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=302, corner_radius=0, fg_color='#2a9d8f')
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

        self.map_widget = tkintermapview.TkinterMapView(
            self.frame_right, corner_radius=0)
        self.map_widget.grid(row=1, rowspan=1, column=0,
                             columnspan=3, sticky="nswe", padx=(0, 0), pady=(0, 0))

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            placeholder_text="type address")
        self.entry.grid(row=0, column=0, sticky="we", padx=(10, 0), pady=12)
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


app = App()
app.start()

import customtkinter as ctk



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x450")
        self.title("QuickNote")
        self.minsize(width=400, height=450)
        self.maxsize(width=400, height=450)

        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.textbox = ctk.CTkTextbox(master=self, width=400, height=450, corner_radius=0, font=("Consolas", 21, "bold"), text_color=("purple"))
        self.textbox.grid(row=0, column=0, sticky="nsew")


        #WIDGETS 
        


        #METHODS
        self.iconbitmap("assets/icon.ico")
        







if __name__ == "__main__":
    app = App()
    app.mainloop()
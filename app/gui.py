import customtkinter as ctk



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x450")
        self.title("QuickNote")
        self.minsize(width=400, height=450)
        self.maxsize(width=400, height=450)
    

        #WIDGETS 


    #METHODS

        







if __name__ == "__main__":
    app = App()
    app.mainloop()
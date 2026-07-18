import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x450")
        self.title("QuickNote")
        self.minsize(400, 450)
        self.maxsize(400, 450)

        self.iconbitmap("assets/icon.ico")

        # Configuración del grid
        self.grid_rowconfigure(0, weight=1)  # El textbox se expande
        self.grid_rowconfigure(1, weight=0)  # El botón no
        self.grid_columnconfigure(0, weight=1)

        # Textbox
        self.textbox = ctk.CTkTextbox(
            self,
            corner_radius=0,
            font=("Consolas", 22, "bold"),
            text_color="white"
        )
        self.textbox.grid(row=0, column=0, sticky="nsew")

        # Botón
        self.button = ctk.CTkButton(
            self,
            text="Guardar",
            command=self.button_event
        )
        self.button.grid(row=1, column=0, pady=10)

    def button_event(self):
        texto = self.textbox.get("1.0", "end")
        print(texto)



if __name__ == "__main__":
    app = App()
    app.mainloop()
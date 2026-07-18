from pathlib import Path

pth = r"C:\Users\shiva\Desktop\path"


class NotesManager:

    @staticmethod
    def guardar_nota(texto):
        carpeta = Path(pth)
        carpeta.mkdir(parents=True, exist_ok=True)

        ruta = carpeta / "notas.txt"

        with open(ruta, "a", encoding="utf-8") as archivo:
            archivo.write(texto + "\n\n")

        print("Nota guardada correctamente.")
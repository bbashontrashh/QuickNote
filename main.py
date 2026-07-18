import os
import customtkinter as ctk
import keyboard
import pathlib
from pathlib import Path
import datetime
import pystray
import winsound

from app.gui import App
from app.notes import NotesManager


def main():
    print("Starting...")
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
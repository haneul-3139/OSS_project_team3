import tkinter
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo,showerror
from typing.fibonacci import Fibonacci
import sqlite3


class typingGame(typingApp):
    def __init__(self,user_id):
        self.user_id = user_id
    def user_info(self):
        print(Fibonacci)
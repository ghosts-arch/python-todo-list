from tkinter import Tk
from tkinter.ttk import Style
from view import View
from styles import theme


class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("Todo List")
        self.state("zoomed")
        self.config(bg="#DCE9F2")
        style = Style()
        style.theme_create("custom", parent="clam", settings=theme)
        style.theme_use("custom")
        View(self)

    def start(self) -> None:
        self.mainloop()

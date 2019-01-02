import tkinter as tk
from Resources.Values import strings, colors


class ReceiveItemPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.__controller = controller
        self.config(bg=colors.bgColor)
        self.columnconfigure(0, weight=1)

        self.__initUI()

    def start(self, args):
        pass

    def __initUI(self):
        pass
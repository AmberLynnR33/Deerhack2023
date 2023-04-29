import tkinter as tk
import openpyxl
from tkinter.filedialog import askopenfilename

class View:
    """
    The UI for the Financial Tracker
    """
    base_screen: tk.Tk
    main_frame: tk.Frame
    main_menu: tk.Menu

    def __init__(self):
        self.base_screen = tk.Tk()
        self.base_screen.title("Financial Tracker")

        self.main_frame = self.create_main_frame()
        self.main_frame.grid(row=0, col=0, sticky='n s e w')

        self.main_menu = self.create_menu()

    def create_main_frame() -> tk.Frame:
        pass

    def frame_tab_month() -> tk.Frame:
        pass

    def frame_money_out() -> tk.Frame:
        pass

    def frame_money_in() -> tk.Frame:
        pass

    def frame_display_money() -> tk.Frame:
        pass

    def frame_goals() -> tk.Frame:
        pass

    def create_menu() -> tk.Menu:
        pass
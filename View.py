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

        self.create_main_frame()
        self.create_menu()

    def create_main_frame(self) -> tk.Frame:
        self.main_frame = tk.Frame(self.base_screen)

    def frame_tab_month(self) -> None:
        pass

    def frame_money_out(self) -> None:
        pass

    def frame_money_in(self) -> None:
        pass

    def frame_display_money(self) -> None:
        pass

    def frame_goals(self) -> None:
        pass

    def create_menu(self) -> None:
        pass

    def _configure_main_screen(self) -> None:
        self.main_frame.grid(row=0, col=0, sticky='n s e w')

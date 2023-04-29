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

    _tab_out_frame: tk.Frame
    _money_out_frame: tk.Frame
    _money_in_frame: tk.Frame
    _display_money_frame: tk.Frame
    _goals_frame: tk.Frame


    def __init__(self):
        self.base_screen = tk.Tk()
        self._configure_main_screen

        self.create_main_frame()
        self.create_menu()

    def create_main_frame(self) -> tk.Frame:
        self.main_frame = tk.Frame(self.base_screen)

        # Each subframe
        self.frame_tab_month()
        self.frame_money_in()
        self.frame_money_out()
        self.frame_display_money()
        self.frame_goals()

    def frame_tab_month(self) -> None:
        self._tab_month_frame = tk.Frame(self.main_frame)

    def frame_money_out(self) -> None:
        self._money_out_frame = tk.Frame(self.main_frame)

    def frame_money_in(self) -> None:
        self._money_in_frame = tk.Frame(self.main_frame)

    def frame_display_money(self) -> None:
        self._display_money_frame = tk.Frame(self.main_frame)

    def frame_goals(self) -> None:
        self._goals_frame = tk.Frame(self.main_frame)

    def create_menu(self) -> None:
        pass

    def _configure_main_screen(self) -> None:
        self.main_frame.grid(row=0, col=0, sticky='n s e w')
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.base_screen.title("Financial Tracker")

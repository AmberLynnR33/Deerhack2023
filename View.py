import tkinter as tk
import openpyxl
from tkinter.filedialog import askopenfilename

class View:
    """
    The UI for the Financial Tracker
    """
    base_screen: tk.Tk
    _main_frame: tk.Frame
    _main_menu: tk.Menu

    _tab_out_frame: tk.Frame
    _money_out_frame: tk.Frame
    _money_in_frame: tk.Frame
    _display_money_frame: tk.Frame
    _goals_frame: tk.Frame

    def __init__(self):
        self.base_screen = tk.Tk()
        self._configure_main_screen

        self._create_main_frame()
        self._create_menu()

    def _create_main_frame(self) -> tk.Frame:
        self._main_frame = tk.Frame(self.base_screen)

        # Each subframe
        self._frame_tab_month()
        self._frame_money_in()
        self._frame_money_out()
        self._frame_display_money()
        self._frame_goals()

    def _frame_tab_month(self) -> None:
        self._tab_month_frame = tk.Frame(self._main_frame)

    def _frame_money_out(self) -> None:
        self._money_out_frame = tk.Frame(self._main_frame)

    def _frame_money_in(self) -> None:
        self._money_in_frame = tk.Frame(self._main_frame)

    def _frame_display_money(self) -> None:
        self._display_money_frame = tk.Frame(self._main_frame)

    def _frame_goals(self) -> None:
        self._goals_frame = tk.Frame(self._main_frame)

    def _create_menu(self) -> None:
        self._main_menu = tk.Menu(self.base_screen)


    def _configure_main_screen(self) -> None:
        self._main_frame.grid(row=0, col=0, sticky='n s e w')
        self._main_frame.columnconfigure(0, weight=1)
        self._main_frame.rowconfigure(0, weight=1)
        self.base_screen.title("Financial Tracker")

        self.base_screen['menu'] = self._main_menu

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import openpyxl
from typing import Optional

from Model import Model
from CategoryCombobox import CategoryCombobox

class View:
    """
    The UI for the Financial Tracker
    """

    model: Model
    base_screen: tk.Tk

    _main_frame: tk.Frame
    _main_menu: tk.Menu

    _tab_out_frame: tk.Frame
    _button_month_selection: ttk.Button
    _combobox_month_select: ttk.Combobox
    _combobox_year_select: ttk.Combobox


    _money_out_frame: tk.Frame
    _money_in_frame: tk.Frame
    _display_money_frame: tk.Frame
    _goals_frame: tk.Frame

    def __init__(self):
        self.base_screen = tk.Tk()

        self._create_main_frame()
        self._create_menu()
        self._configure_main_screen()

    def _create_main_frame(self) -> tk.Frame:
        self._main_frame = tk.Frame(self.base_screen)

        # Each subframe
        self._frame_tab_month()
        self._frame_display_money()
        self._frame_money_in()
        self._frame_money_out()
        self._frame_goals()

    def _frame_tab_month(self) -> None:
        self._tab_month_frame = tk.Frame(self._main_frame)

        month_vals = ['January', 'February', 'March', 'April', 'May', 'June',
                      'July', 'August', 'September', 'October', 'November',
                      'December']
        
        year_vals = ['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']

        self._combobox_month_select = ttk.Combobox(self._tab_month_frame, values=month_vals)
        self._combobox_month_select.set('Select Month')
        self._combobox_month_select['state'] = 'readonly'

        self._combobox_year_select = ttk.Combobox(self._tab_month_frame, values=year_vals)
        self._combobox_month_select.set('Select Year')
        self._combobox_month_select['state'] = 'readonly'

        self._button_month_selection = ttk.Button(self._tab_month_frame, text="Get Month's Finances", 
                                                  justify='center',
                                                  command=self.model.page_exists(self._combobox_month_select.get(),
                                                                                 self._combobox_year_select.get()))

        self._button_month_selection.grid(row=0, column=0)
        self._button_month_selection.columnconfigure(0, weight=1)
        self._button_month_selection.rowconfigure(0, weight=1)

        self._combobox_month_select.grid(row=1, column=0)
        self._combobox_month_select.columnconfigure(0, weight=1)
        self._combobox_month_select.rowconfigure(0, weight=1)

        self._combobox_year_select.grid(row=2, column=0)
        self._combobox_year_select.columnconfigure(0, weight=1)
        self._combobox_year_select.rowconfigure(0, weight=1)

    def _frame_money_out(self) -> None:
        self._money_out_frame = tk.Frame(self._main_frame)

        self._money_out_cat = CategoryCombobox(self._money_out_frame)
        self._money_out_cat.configure_combobox()

        self._money_out_str = tk.StringVar()

        self._money_out_entry = ttk.Entry(self._money_out_frame, self._money_out_entry)

        self._submit_money_out = ttk.Button(self._money_out_frame, text="Add Money Spent", 
                                           justify='center',
                                           command=self.money_output)
        
        self._submit_money_out.grid(row=0, column=0)
        self._submit_money_out.columnconfigure(0, weight=1)
        self._submit_money_out.rowconfigure(0, weight=1)

        self._money_out_cat.grid(row=1, column=0)
        self._money_out_cat.columnconfigure(0, weight=1)
        self._money_out_cat.rowconfigure(0, weight=1)

        self._money_out_entry.grid(row=0, column=0)
        self._money_out_entry.columnconfigure(0, weight=1)
        self._money_out_entry.rowconfigure(0, weight=1)

    def _frame_money_in(self) -> None:
        self._money_in_frame = tk.Frame(self._main_frame)

        self._money_in_str = tk.StringVar()
        self._money_in_entry = ttk.Entry(self._money_in_frame, self._money_in_entry)

        self._submit_money_in = ttk.Button(self._money_in_frame, text="Add Money Earned", 
                                           justify='center',
                                           command=self.money_input)

        self._submit_money_in.grid(row=0, column=0)
        self._submit_money_in.columnconfigure(0, weight=1)
        self._submit_money_in.rowconfigure(0, weight=1)

        self._money_in_entry.grid(row=1, column=0)
        self._money_in_entry.columnconfigure(0, weight=1)
        self._money_in_entry.rowconfigure(0, weight=1)


    def money_input(self) -> None:
        self.model.add_money_in(self._money_in_entry.get())
        self._money_update()


    def money_output(self) -> None:
        self.model.add_money_out(self._money_out_entry.get(), self._money_out_cat.get())
        self._money_update()


    def _frame_display_money(self) -> None:
        self._display_money_frame = tk.Frame(self._main_frame)

        self._money_earned_entry = tk.StringVar()
        self._money_earned = ttk.Label(self._display_money_frame)
        self._money_earned['textvariable'] = self._money_earned_entry

        self._money_spent_entry = tk.StringVar()
        self._money_spent = ttk.Label(self._display_money_frame)
        self._money_spent['textvariable'] = self._money_spent_entry

        self._money_spent_bills_e = tk.StringVar()
        self._money_spent_bills = ttk.Label(self._display_money_frame)
        self._money_spent_bills['textvariable'] = self._money_spent_bills_e

        self._money_spent_sub_e = tk.StringVar()
        self._money_spent_sub = ttk.Label(self._display_money_frame)
        self._money_spent_sub['textvariable'] = self._money_spent_sub_e

        self._money_spent_essn_e = tk.StringVar()
        self._money_spent_essn = ttk.Label(self._display_money_frame)
        self._money_spent_essn['textvariable'] = self._money_spent_essn_e

        self._money_spent_edu_e = tk.StringVar()
        self._money_spent_edu = ttk.Label(self._display_money_frame)
        self._money_spent_edu['textvariable'] = self._money_spent_edu_e

        self._money_spent_lux_e = tk.StringVar()
        self._money_spent_lux = ttk.Label(self._display_money_frame)
        self._money_spent_lux['textvariable'] = self._money_spent_lux_e

        self._money_update()

        self._money_earned.grid(row=0, column=0)
        self._money_earned.columnconfigure(0, weight=1)
        self._money_earned.rowconfigure(0, weight=1)

        self._money_spent.grid(row=1, column=0)
        self._money_spent.columnconfigure(0, weight=1)
        self._money_spent.rowconfigure(0, weight=1)

        self._money_spent_bills.grid(row=2, column=0)
        self._money_spent_bills.columnconfigure(0, weight=1)
        self._money_spent_bills.rowconfigure(0, weight=1)

        self._money_spent_sub.grid(row=3, column=0)
        self._money_spent_sub.columnconfigure(0, weight=1)
        self._money_spent_sub.rowconfigure(0, weight=1)

        self._money_spent_essn.grid(row=4, column=0)
        self._money_spent_essn.columnconfigure(0, weight=1)
        self._money_spent_essn.rowconfigure(0, weight=1)

        self._money_spent_edu.grid(row=5, column=0)
        self._money_spent_edu.columnconfigure(0, weight=1)
        self._money_spent_edu.rowconfigure(0, weight=1)

        self._money_spent_lux.grid(row=6, column=0)
        self._money_spent_lux.columnconfigure(0, weight=1)
        self._money_spent_lux.rowconfigure(0, weight=1)


    def _money_update(self) -> None:
        self._money_earned_entry.set('$' + str(self.model.total_amount_earned()))
        self._money_spent_entry.set('$' + str(self.model.total_spent()))

        self._money_spent_bills_e.set('$' + str(self.model.total_spent('bills')))
        self._money_spent_sub_e.set('$' + str(self.model.total_spent('subscriptions')))
        self._money_spent_essn_e.set('$' + str(self.model.total_spent('essentials')))
        self._money_spent_edu_e.set('$' + str(self.model.total_spent('edu')))
        self._money_spent_lux_e.set('$' + str(self.model.total_spent('luxury')))
        

    def _frame_goals(self) -> None:
        self._goals_frame = tk.Frame(self._main_frame)

    def _create_menu(self) -> None:
        self._main_menu = tk.Menu(self.base_screen)

        #to create new files and load up existing ones
        self._file_menu = tk.Menu(self._main_menu)
        self._main_menu.add_cascade(menu=self._file_menu, label='Load New Tracker', command=self.model.create_file)
        self._main_menu.add_cascade(menu=self._file_menu, label='Load Existing Tracker', command=self.model.open_file(self.load_file_path))
                                    
    def _load_file_path() -> Optional[str]:
        
        try:
            return askopenfilename()
        except FileNotFoundError:
            return None
        

    def _configure_main_screen(self) -> None:
        self._main_frame.grid(row=0, col=0, sticky='n s e w')
        self._main_frame.columnconfigure(0, weight=1)
        self._main_frame.rowconfigure(0, weight=1)
        self.base_screen.title("Financial Tracker")

        self.base_screen['menu'] = self._main_menu


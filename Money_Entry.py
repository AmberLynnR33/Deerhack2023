from tkinter import ttk
import tkinter as tk
import re

class Money_Entry(ttk.Entry):
    """
    This is a button that only allows allows the user to enter float values,
    Or a cost
    """

def valid_amount() -> bool:
        cur_val = a.get()

        valid_decimal = True
        valid_char = True
        num_after_decimal = 0
        num_decimals = 0

        for char in cur_val:
            if not (char in '1234567890.'):
                 valid_char = False
                 break

            if num_decimals > 0:
                num_after_decimal += 1

            if char in '.':
                 num_decimals += 1
                 if num_decimals > 1:
                      valid_decimal = False
                      break

        return valid_char and valid_decimal and (num_after_decimal < 3)
    

if __name__ == '__main__':
    screen = tk.Tk()
    main_frame = tk.Frame(screen)

    main_frame.grid(row=0, column=0, sticky='n s e w')
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)

    b = tk.StringVar()

    a = Money_Entry(main_frame, textvariable=b, validate='all', validatecommand=valid_amount)

    
    a.grid(row=0, column=0)

    screen.mainloop()

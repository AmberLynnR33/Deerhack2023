import tkinter as tk
from tkinter import ttk


def valid_amount(text) -> bool:

    try:
        float(text)
    except ValueError:
        return False
    else:
        str_rep = str(text)
        at_decimal = False
        decimal_places = 0
        for char in str_rep:
            if at_decimal:
                decimal_places += 1

            if char == '.':
                at_decimal = True
        return decimal_places <= 2
    
if __name__ == '__main__':
    screen = tk.Tk()
    main_frame = tk.Frame(screen)
    hi = screen.register(valid_amount)

    b = tk.StringVar()

    a = tk.Entry(screen, textvariable=b, validate="key", validatecommand=(hi, '%P'))

    a.grid(row=0, column=0)

    screen.mainloop()

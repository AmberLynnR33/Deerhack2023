import tkinter as tk

class Money_Entry(tk.Frame):
    """
    This is a button that only allows allows the user to enter float values,
    Or a cost

    def __init__(self, master: Misc | None = None, widget: str | None = None, *, background: str = ..., class_: str = ..., exportselection: bool = ..., font: _FontDescription = ..., foreground: str = ..., invalidcommand: _EntryValidateCommand = ..., justify: Literal['left', 'center', 'right'] = ..., name: str = ..., show: str = ..., state: str = ..., style: str = ..., takefocus: _TakeFocusValue = ..., textvariable: Variable = ..., validate: Literal['none', 'focus', 'focusin', 'focusout', 'key', 'all'] = ..., validatecommand: _EntryValidateCommand = ..., width: int = ..., xscrollcommand: _XYScrollCommand = ...) -> None:
        super().__init__(master, widget, background=background, class_=class_, cursor=cursor, exportselection=exportselection, font=font, foreground=foreground, invalidcommand=invalidcommand, justify=justify, name=name, show=show, state=state, style=style, takefocus=takefocus, textvariable=textvariable, validate=validate, validatecommand=validatecommand, width=width, xscrollcommand=xscrollcommand):
        self.master.register(valid_amount, '%P')
    """

    pass


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

        if valid_char and valid_decimal and (num_after_decimal < 3):
            return True
        else:
            return False
    

if __name__ == '__main__':
    screen = tk.Tk()
    main_frame = tk.Frame(screen)
    valid_str = screen.register(valid_amount, '%P')

    main_frame.grid(row=0, column=0, sticky='n s e w')
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)

    a = tk.Entry(main_frame, validate='key', validatecommand=valid_str)
    
    a.grid(row=0, column=0)

    screen.mainloop()

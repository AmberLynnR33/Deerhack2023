from tkinter import ttk

class Money_Entry(ttk.Entry):
    """
    This is a button that only allows allows the user to enter float values,
    Or a cost
    """

    def valid_amount(self, new_char: str) -> bool:
        cur_val = self.get()

        contains_decimal = False
        num_after_decimal = 0

        for char in cur_val:
            if contains_decimal == True:
                num_after_decimal += 1

            if char in '.':
                contains_decimal = True

        valid_char = new_char in '123456789.'
        valid_decimal = True

        if new_char in '.' and contains_decimal:
            valid_decimal = False

        return valid_char and valid_decimal and num_after_decimal < 3

from tkinter import ttk
import tkinter as tk

class CategoryCombobox(ttk.Combobox):
    """
    A combobox that is configued to have the categories of spending for the
    money tracker
    """

    def configure_combobox(self):

        self['values'] = ['Bills', 'Subscriptions', 'Essentials', 'Education / Work', 'Luxuries']
        self.set('Select Category')
        self['state'] = 'readonly'

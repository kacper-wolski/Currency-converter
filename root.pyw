import tkinter as tk
import ttkbootstrap as ttk

# My libraries
import http_request
import all_tools
from Currency_convert import currency_convert


# Main window
root = tk.Tk()
style = ttk.Style(theme='journal')
root.title('Currency converter')
root.geometry('600x400')
root.resizable(False,False)
root.iconbitmap("Files\icon.ico")

currencies = all_tools.import_currencies() # Import all data needed

from_currency = tk.StringVar() # Main variables using StringVar to collect data up to date 
to_currency = tk.StringVar()
user_value = tk.StringVar()
from_currency.set('PLN') # Set their initial values
to_currency.set('USD')

from_currency_str = from_currency.get() # Make a stable strings and ints
to_currency_str = to_currency.get()
user_value_int = user_value.get()

equals = currency_convert(from_currency_str, to_currency_str, user_value_int)

title_text = ttk.Label(root, text = 'Currency converter', font = ('Microsoft JhengHei UI', 30)) # Top title
title_text.grid(row=0, column=0, columnspan=2, pady=10)

main_frame = ttk.Frame(root) # Frame 
main_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky='n')

root.columnconfigure(0, weight=1) # Set positions
root.columnconfigure(1, weight=1)
root.rowconfigure(1, weight=1)

user_entry = ttk.Entry(main_frame, textvariable=user_value, font = ('Microsoft JhengHei UI', 15)) # Place for user to enter his numbers
user_entry.grid(row=0, column=0)
user_entry.bind('<KeyRelease>', lambda event: all_tools.on_user_value_changed(user_value, from_currency, to_currency, result_entry))

result_entry = ttk.Entry(main_frame, state="readonly", textvariable=equals, font = ('Microsoft JhengHei UI', 15)) # Place with result of conversion
result_entry.grid(row=1, column=0)

currency_list = ttk.Combobox(main_frame, state = 'readonly', textvariable = from_currency, font = ('Microsoft JhengHei UI', 15)) # First dropdown list aka 'from currency'
currency_list['values'] = list(currencies)
currency_list.set(from_currency_str)
currency_list.grid(row=0, column=1)
currency_list.bind('<<ComboboxSelected>>')

currency_list2 = ttk.Combobox(main_frame, state = 'readonly', textvariable = to_currency, font = ('Microsoft JhengHei UI', 15)) # Second dropdown list aka 'to currency'
currency_list2['values'] = list(currencies)
currency_list2.set(to_currency_str)
currency_list2.grid(row=1, column=1)
currency_list2.bind('<<ComboboxSelected>>')

root.mainloop()
import tkinter as tk
import ttkbootstrap as ttk

import http_request
import all_tools


def currency_convert(from_currency, to_currency, user_value):

    currencies = all_tools.import_currencies()

    exchange_rates = all_tools.import_rates()
    equals = 0

    try:
        user_value = float(user_value)  # Convert the user input to a floating-point number
    except ValueError:
        return equals  # Return 0 if the input is not a valid number

    if from_currency in exchange_rates:
        exchange_rate = exchange_rates[from_currency]
        equals = user_value / exchange_rate
    else:
        return equals


    if to_currency in exchange_rates:
        exchange_rate = exchange_rates[to_currency]
        return equals * exchange_rate
    else:
        return equals * exchange_rate
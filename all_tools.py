import http_request

def import_currencies():
    currency_data = http_request.data_request()
    currencies = currency_data["rates"].keys()

    return currencies


def import_rates():
    currency_data = http_request.data_request()
    exchange_rates = currency_data["rates"]

    return exchange_rates


def on_user_value_changed(user_value, from_currency, to_currency, result_entry):
    import tkinter as tk
    from Currency_convert import currency_convert

    user_input = user_value.get().strip()
    if not user_input: # Check if user input is empty 
        result_entry.config(state='normal')
        result_entry.delete(0, tk.END)
        result_entry.insert(0, "Enter a value") # Type error message if it is empty
        result_entry.config(state='readonly')
        return

    try:
        value = float(user_input)  # Try to convert the user input to a floating-point number
    except ValueError:
        try:
            value = int(user_input)  # If conversion to float fails, try conversion to integer
        except ValueError:
            result_entry.config(state='normal')
            result_entry.delete(0, tk.END)
            result_entry.insert(0, "Invalid input")  # Insert an error message for invalid input
            result_entry.config(state='readonly')
            return

    converted_value = currency_convert(from_currency.get(), to_currency.get(), value) 
    formatted_value = "{:.3f}".format(converted_value)  # Format the converted value with three decimal places
    result_entry.config(state='normal')
    result_entry.delete(0, tk.END)
    result_entry.insert(0, formatted_value)
    result_entry.config(state='readonly')
# Program Name: Assignment3.py
# Course: IT3883/Section 01
# Student Name: Benel Kawata
# Assignment Number: Assignment 3
# Due Date: 10/10/2027
# Purpose:  The program aims to convert miles per gallon to kilometers per liter in a GUI.
#           It also updates the result as the user types and handles invalid input without crashing.
# Resources:
# W3Schools, "Python Try Except": handling invalid numeric input.
# https://www.w3schools.com/python/python_try_except.asp

import math  # This module provides isfinite() to reject infinity as invalid input.
import tkinter as tk  # This package provides GUI tools; "tk" is a shorter name for tkinter.
from tkinter import ttk  # This submodule from the tkinter module the ttk Provides themed widgets for the labels, entry box, and frame.

# Here a function is defined to convert the input into a result or a helpful message for special events.
# Also, this function is created outside of the main function and will be called inside instead
def convert_mpg(input_text):
    if input_text.strip() == "":
        return ""

    try:
        miles_per_gallon = float(input_text)
    except ValueError:
        return "The entry could not be seen or processed"

    # The 'isfinite' parameter allows to reject special values such as infinity or Null.
    if not math.isfinite(miles_per_gallon):
        return "Please enter a valid number"

    kilometers_per_liter = miles_per_gallon * 0.425143707
    return f"{kilometers_per_liter:.4f}"

def main():
    # It creates the window and variables connected to its widgets.
    ww = tk.Tk()
    ww.title("MPG to km/L Converter")
    ww.minsize(440, 160)
    mpg_input = tk.StringVar(master=ww)
    conversion_output = tk.StringVar(master=ww)

    # This function is created within the main funcion and will be Called automatically whenever the input text changes.
    def update_result(*args):
        conversion_output.set(convert_mpg(mpg_input.get()))

    # This block will arrange the input and result with clearly labeled units.
    frm = ttk.Frame(ww, padding=20)
    frm.grid(row=0, column=0, sticky="nsew")
    ww.columnconfigure(0, weight=1)
    ww.rowconfigure(0, weight=1)
    frm.columnconfigure(1, weight=1)

    ttk.Label(frm, text="Miles per gallon (mpg):").grid(
        row=0, column=0, padx=(0, 12), pady=8, sticky="w"
    )
    input_box = ttk.Entry(frm, textvariable=mpg_input, width=28)
    input_box.grid(row=0, column=1, pady=8, sticky="ew")

    ttk.Label(frm, text="Kilometers per liter (km/L):").grid(
        row=1, column=0, padx=(0, 12), pady=8, sticky="w"
    )
    ttk.Label(frm, textvariable=conversion_output, wraplength=240).grid(
        row=1, column=1, pady=8, sticky="w"
    )
    ttk.Label(frm, text="The result updates as you type.").grid(
        row=2, column=0, columnspan=2, pady=(8, 0), sticky="w"
    )

    # This allows the user to watch all changes, including typing, pasting, and deleting text.
    mpg_input.trace_add("write", update_result)
    input_box.focus_set()
    ww.mainloop()

if __name__ == "__main__":
    main()

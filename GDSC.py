import random
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time

# Initialize debit and daily debit limit variables
debit = 0
daily_debit_limit = 200

# Function to generate a random bank SMS message for credit
def generate_credit_sms():
    amount = round(random.uniform(1, 1000), 2)
    current_date = datetime.now()
    sms = f"Credit of Rs. {amount:.2f} received on {current_date.strftime('%Y-%m-%d')}."
    return sms

# Function to generate a random bank SMS message for debit
def generate_debit_sms():
    max_debit_amount = min(daily_debit_limit - debit, 80)  # Limit debit to daily and per transaction limit
    if max_debit_amount <= 0:
        return ""  # No more debits allowed for the day
    amount = round(random.uniform(1, max_debit_amount), 2)
    current_date = datetime.now()
    sms = f"Rs. {amount:.2f} withdrawn on {current_date.strftime('%Y-%m-%d')} at ATM."
    return sms

# Function to show a warning pop-up
def show_warning_popup():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showwarning("GPay Locked", "Your GPay account has been locked for today due to excessive debits.")
    root.destroy()  # Close the hidden main window

# Function to update the debit amount label in the GUI
def update_debit_label():
    global debit
    debit_label.config(text=f"Total Debit: Rs. {debit:.2f}")
    root.update_idletasks()

# Function to simulate virtual days indefinitely
def simulate_virtual_days():
    global debit, daily_debit_limit
    day = 1  # Initialize the day counter
    warning_shown = False  # Flag to track whether a warning has been shown

    while True:
        # Reset debit variable and daily debit limit at the start of each new day
        debit = 0
        daily_debit_limit = 200
        
        print(f"Day {day}:\n")

        # Add a time lag of 5 seconds at the beginning of each new day
        time.sleep(1)

        # Generate a random number of messages for the day (between 1 and 5)
        num_messages = random.randint(1, 8)

        for _ in range(num_messages):
            # Check if debit has reached daily debit limit or a warning has been shown
            if debit >= daily_debit_limit or warning_shown:
                break  # Stop generating messages for the day

            # Generate random credit and debit SMS messages
            credit_sms = generate_credit_sms()
            debit_sms = generate_debit_sms()

            if not debit_sms:
                break  # No more debits allowed for the day

            print("Credit SMS:", credit_sms)
            print("Debit SMS:", debit_sms)

            # Process debit SMS and update debit variable
            debit_amount = get_debit_amount(debit_sms)
            debit += debit_amount
            update_debit_label()  # Update the debit label in the GUI

            # Check if debit exceeds daily debit limit and show a warning
            if debit >= daily_debit_limit:
                show_warning_popup()
                warning_shown = True  # Set the warning flag

            # Check if debit exceeds 200 and show a warning
            if debit >= 200:
                show_custom_warning_popup("Warning", "Debit exceeds Rs. 200!")

        print(f"\nTotal Debit for Day {day}: Rs. {debit:.2f}\n")

        # Increment day counter
        day += 1

        # Check if a warning has been shown
        if warning_shown:
            warning_shown = False  # Reset warning flag and continue simulating from the next day

# Function to extract debit amount from an SMS
def get_debit_amount(sms):
    amount = None
    try:
        # Extract amount from SMS using regular expression
        import re
        match = re.search(r'Rs\. (\d+\.\d{2}) withdrawn', sms)
        if match:
            amount = float(match.group(1))
    except Exception as e:
        print(f"Error extracting debit amount: {e}")

    return amount

# Function to show a custom warning pop-up
def show_custom_warning_popup(title, message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    messagebox.showwarning(title, message)
    root.destroy()  # Close the hidden main window

# Create a centered and visually appealing GUI
root = tk.Tk()
root.title("Transaction Simulator")
root.geometry("400x200")  # Increased window size

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - root.winfo_reqwidth()) / 2
y_position = (screen_height - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x_position, y_position))

debit_label = tk.Label(root, text=f"Total Debit: Rs. {debit:.2f}", font=("Helvetica", 16))
debit_label.pack(pady=20)

# Start simulating virtual days indefinitely
simulate_virtual_days()

root.mainloop()

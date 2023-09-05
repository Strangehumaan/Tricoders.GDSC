# Tricoders.GDSC
This is a tool that will help students to save their money and spend responsibly

The provided code is a Python program that simulates a transaction history for a virtual bank account using a graphical user interface (GUI). Here's a brief explanation of the code:

Initialization: It initializes variables for debit, daily debit limit, and other necessary parameters.

Functions for Generating SMS Messages: It includes functions to generate random SMS messages for credit and debit transactions.(will be replaced by real life time bank sms in the near future)

Warning Pop-up: There's a function to show a warning pop-up message when certain conditions are met, such as exceeding a daily debit limit or reaching a debit threshold.
The above feature will be replaced such that your money transaction application for say GPay will get automatically locked and a random password will be generated that will be sent to user's Guardian.

Updating Debit Label: A function updates a label in the GUI to display the total debit amount.

Simulation Loop: The simulate virtual days function runs an infinite loop simulating virtual days. It generates random transaction messages for each day, updates the debit amount, and shows warning pop-ups when necessary.

Extracting Debit Amount: A function extracts the debit amount from transaction SMS messages.

Creating a Custom Warning Pop-up: Another function displays a custom warning pop-up when needed.

Creating a Centered and Appealing GUI: The code creates a GUI window using Tkinter, a Python GUI library. It sets the window size, centers it on the screen, and displays the total debit amount.

Starting the Simulation: The script initiates the virtual day simulation by calling the simulate virtual days function.

Overall, this code provides a user-friendly way to visualize and interact with a simulated bank transaction history, with warnings and messages displayed in a GUI window.


Cryptocurrency Price Tracker
This Python script is a simple PyQt5 application that displays the current price of a selected cryptocurrency (Bitcoin, Ethereum, or Litecoin) in USD (U.S. Dollars) and updates the price every 5 seconds. It uses the CryptoCompare API to fetch cryptocurrency prices and PyQt5 for the graphical user interface.

Code Overview
Import Necessary Libraries:

sys: Provides access to interpreter variables and functions for interaction with the interpreter.
PyQt5.QtWidgets: Offers classes for creating graphical user interfaces.
PyQt5.QtCore: Contains core non-GUI functionality.
requests: A library for making HTTP requests.
json: Used for parsing JSON data.
cryptocompare: A library for working with cryptocurrency data.
Replace 'KEY_HERE' with Your API Key:

You need to replace the placeholder 'KEY_HERE' in the script with your actual API key for accessing cryptocurrency data.
Define the CryptoPrice Class:

Represents the main application window.
Includes a user interface with a label for displaying the selected cryptocurrency, a label for displaying the price, and a combo box for selecting the cryptocurrency to display.
Initialize the UI:

The initUI method sets up the user interface layout, including labels and the combo box.
It connects the combo box's activated signal to the get_price method and sets up a timer to periodically call get_price every 5 seconds.
The get_price Method:

Fetches the price of the selected cryptocurrency from the CryptoCompare API.
Parses the JSON response and updates the labels with the cryptocurrency symbol and its current price.
Application Entry Point:

The if __name__ == '__main__': block is the entry point of the script.
It creates an instance of the CryptoPrice class, shows the GUI window, and starts the PyQt5 application event loop.
When you run this script, it will display a GUI window that allows you to select a cryptocurrency from the combo box (BTC, ETH, or LTC), and it will continuously update the price of the selected cryptocurrency every 5 seconds. It uses the CryptoCompare API to obtain the cryptocurrency price data.

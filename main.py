import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox
from PyQt5.QtCore import QTimer
import requests
import json
import cryptocompare


# Replace 'KEY_HERE' with your actual API key
API_KEY = 'cryptocompare.cryptocompare._set_api_key_parameter'

# Set the API key parameter
cryptocompare.cryptocompare._set_api_key_parameter(API_KEY)

class CryptoPrice(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.crypto_label = QLabel(self)
        self.price_label = QLabel(self)

        self.crypto_combo = QComboBox(self)
        self.crypto_combo.addItem('BTC')
        self.crypto_combo.addItem('ETH')
        self.crypto_combo.addItem('LTC')

        self.layout.addWidget(self.crypto_label)
        self.layout.addWidget(self.price_label)
        self.layout.addWidget(self.crypto_combo)

        self.setLayout(self.layout)

        self.crypto_combo.activated.connect(self.get_price)

        self.timer = QTimer()
        self.timer.timeout.connect(self.get_price)
        self.timer.start(5000) # Refresh every 5 seconds

        self.get_price()

    def get_price(self):
        crypto = self.crypto_combo.currentText()

        try:
            response = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={crypto}&tsyms=USD')
            data = response.json()

            self.crypto_label.setText(f'{crypto} Price:')
            self.price_label.setText(f'${data["USD"]}')

        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CryptoPrice()
    ex.show()
    sys.exit(app.exec_())

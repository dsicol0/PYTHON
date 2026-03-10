import sys
import requests
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):

    def __init__ (self):
        # INITIALIZE THE PARENT QWIDGET CLASS.
        # Is not our business knowing HOW it is implemented
        super().__init__() 

        # Create UI components
        self.city_label = QLabel("Enter city name : ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)  # Button to trigger weather fetch
        
        # Labels to display weather results (placeholder values for now)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    ## INITIALIZES THE USER INTERFACE
    def initUI(self):
        self.setWindowTitle("Weather App")

        # Create a vertical layout and add all widgets in order
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)    # APPLY THE LAYOUT TO THE WINDOW

        # ALLIGNS THE LAYOUT TO THE CENTER 
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # In Qt/CSS stylesheet works with names set using setObjectName():
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # SOME DECORATORS IN CSS (dont mind)
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibri;     
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 30px;          
            }
            QPushButton#get_weather_button {
                font-size: 30 px;
                font-weight: bold;               
            }
            QLabel#temperature_label {
                font-size: 75px;               
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segoe UI emoji
            }
            QLabel#description_label {
                font-size: 50px;               
            }
        """)

        # WHEN USER CLICKS ON THE BUTTON get_weather WILL BE CALLED
        self.get_weather_button.clicked.connect(self.get_weather)
        
    def get_weather(self):
        pass

    def display_error(self, message):
        pass

    def display_weather(self, data):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weatherApp = WeatherApp()
    weatherApp.show()
    sys.exit(app.exec_())       # Start the event loop; exit cleanly when window is closed
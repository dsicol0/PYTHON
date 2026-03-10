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
                font-size: 90px;
                font-family: Segoe UI emoji
            }
            QLabel#description_label {
                font-size: 50px;               
            }
        """)

        # WHEN USER CLICKS ON THE BUTTON get_weather WILL BE CALLED
        self.get_weather_button.clicked.connect(self.get_weather)
        
    def get_weather(self):
        
        api_key = "f030089a65dc30ce65772b1bc1904bb4"    # from openweather

        city = self.city_input.text()           # gets the text from the input box
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"   # API call

        # cod is a field in the json format that tells us information :
        # - 200 --> city found (succesful response)
        # - 404 --> city not found
        # - 401 --> invalid API key
        # ...
        # WE CAN USE A TRY BLOCK
        try:
            response = requests.get(url)
            response.raise_for_status()         # raise an excpetion if theres an HTTPError
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)
            
        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad Request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized\nInvalid API key")
                case 403:
                    self.display_error("Forbidden\nAccess is denied")
                case 404:
                    self.display_error("City not found :(")
                case 500:
                    self.display_error("Internal Server Error\nPlease try again later")
                case 502:
                    self.display_error("Bad Gateway\nInvalid response from the server")
                case 503:
                    self.display_error("Service Unavailable\nServer is down :(")
                case 504:
                    self.display_error("Gateway Timeout\nNo response from the server")
                case _:
                    self.display_error(f"HTTP error occured\n{http_error}")
        
        # SOME OTHER ERRORS WE CAN GET
        except requests.exceptions.ConnectionError:                         # Connection error
            self.display_error("Connection Error :\nCheck yout internet connection")   
        except requests.exceptions.RequestException as req_error:           # Request error
            self.display_error(f"Request Error :\n{req_error}")


    def display_error(self, message):
        self.temperature_label.setStyleSheet("font-size: 30px;")
        self.temperature_label.setText(message)
        self.emoji_label.clear()
        self.description_label.clear()

    def display_weather(self, data):

        # WE'LL SEARCH FOR "main" IN THE JSON FILE WHICH STORES
        # A DICTIONARY WITH THE INFORMATIONS. Temperature is stored in
        # Kelvin format so we need to convert it to Celsius
        temperature_k = data["main"]["temp"]
        temperature_c = temperature_k - 273.15
        temperature_k = (temperature_k * 9/5) - 459.67

        weather_id = data["weather"][0]["id"]

        self.temperature_label.setStyleSheet("font-size: 50px;")            # SETS THE FONT TO ORIGINAL SIZE
        self.temperature_label.setText(f"{temperature_c:.0f}°C  |  {temperature_k:.0f}°F")  
        
        # FOR THE DESCRIPTION OF THE WEATHER INSTEAD IN THE JSON FILE
        # WE HAVE A LIST WITH ONLY ONE ELEMENT
        weather_description = data["weather"][0]["description"] 
        self.description_label.setText(weather_description)
        self.emoji_label.setText(self.get_weater_emoji(weather_id))
    
    @staticmethod    # we don't need an instance to use it
    def get_weater_emoji(weather_id):     

        # ALWAYS IN THE JSON FILE THERE IS AN ID OF THE WEATHER 
        # THAT CHANGES DEPENDING ON IT :
        # - 2xx --> Thunderstorm
        # - 3xx --> Drizzle
        # - 5xx --> Rain
        # ...
        if 200 <= weather_id <= 232:
            return "⛈️"
        elif 300 <= weather_id <= 321:
            return "🌦️"
        elif 500 <= weather_id <= 531:
            return "🌧️"
        elif 600 <= weather_id <= 622:
            return "🌨️"
        elif 701 <= weather_id <= 741:
            return "🌫️"
        elif weather_id == 800:
            return "☀️" 
        elif 801 <= weather_id <= 804:
            return "☁️"
        else:
            return ""
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weatherApp = WeatherApp()
    weatherApp.show()
    sys.exit(app.exec_())       # Start the event loop; exit cleanly when window is closed
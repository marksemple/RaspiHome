# Weather Module

# A Widget To Display
# A client to get Weather data

import sys
import time
import json
from PyQt5.QtCore import (QThread, pyqtSignal)
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QFormLayout)
from apixu.client import ApixuClient, ApixuException

with open('./weather_api_key.json') as data_file:
    api_key = json.load(data_file)['api_key']
    data_file.close()


class weatherWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.weatherThread = getWeatherThread()
        self.weatherThread.newWeather.connect(lambda x: self.updateFields(x))
        self.defineLayout()
        self.resize(250, 250)
        self.weatherThread.start()

    def defineLayout(self):
        self.cityLabel = QLabel("city")
        self.dateLabel = QLabel("date")
        self.tempLabel = QLabel("20.0")
        self.Symbol = QLabel("< >")
        self.feelslike = QLabel("feels like: {:.1f}".format(17))
        self.dailyHigh = QLabel("24.0")
        self.wind = QLabel("14kt")
        self.sunset = QLabel("18:45")
        formLayout = QFormLayout()
        formLayout.addRow(self.cityLabel, self.dateLabel)
        formLayout.addRow(self.tempLabel, self.Symbol)
        formLayout.addRow("Daily high", self.dailyHigh)
        formLayout.addRow("Wind", self.wind)
        formLayout.addRow("Sunset", self.sunset)
        self.setLayout(formLayout)

    def updateFields(self, resp={}):

        cityName = resp['location']['name']
        localTime = resp['location']['localtime']
        currentTemp = resp['current']['temp_c']
        condition = resp['current']['condition']['text']
        feelsLike = resp['current']['feelslike_c']
        wind = {'speed': resp['current']['wind_kph'],
                'dir': resp['current']['wind_dir']}
        dailyHi = resp['forecast']['forecastday'][0]['day']['maxtemp_c']
        sunset = resp['forecast']['forecastday'][0]['astro']['sunset']

        self.cityLabel.setText('{}'.format(cityName))
        self.dateLabel.setText('{}'.format(localTime))
        self.tempLabel.setText('{} ° C'.format(currentTemp))
        self.Symbol.setText('{}'.format(condition))
        self.feelslike.setText('{} ° C'.format(feelsLike))
        self.wind.setText('{} km/h {}'.format(wind['speed'], wind['dir']))
        self.dailyHigh.setText('{} ° C'.format(dailyHi))
        self.sunset.setText('{}'.format(sunset))


class getWeatherThread(QThread):
    """ upon creation, and then every x Minutes:
        go online and get new weather from apiXu client"""

    newWeather = pyqtSignal(dict)

    def __init__(self, city="Toronto", *args, **kwargs):
        super().__init__()
        self.city = city
        self.client = ApixuClient(api_key)

    def run(self):
        self.collectingWeather = True
        print("start collecting weather")
        count = -1
        nMins = 15

        while self.collectingWeather:
            count += 1
            print(count)
            forecast = self.client.getForecastWeather(q=self.city, days=1)
            self.newWeather.emit(forecast)
            time.sleep(60 * nMins)

            # dummy loop-ender
            # if count == 2:
            # self.collectingWeather = False

        print("stop collecting weather")

    def stopWeather(self):
        self.collectingWeather = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather = weatherWidget()
    weather.show()
    app.exec_()



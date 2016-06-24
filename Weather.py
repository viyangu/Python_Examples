from urllib.request import urlopen
from bs4 import BeautifulSoup

city = input("Enter city: ")

try:
    list1 = city.split(' ')
    list2 = []
    for x in list1:
        y = x.capitalize()
        list2.append(y)

    city = "-".join(list2)
    url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"

    html = urlopen(url)
    bs_obj = BeautifulSoup(html.read(), "html.parser")

    weather = bs_obj.findAll("span", {"class" : "phrase"})

    print ("\nWeather Forecast for " + city + " :")

    print ("\nfor 1-3 Days:\n " , weather[0].getText())
    print ("\nfor 4-7 Days:\n " , weather[1].getText())
    print ("\nfor 7-10 Days:\n " , weather[2].getText())
except:
    print ("Error: please try again.")

# API = Application programming interface

# are methods (functions) that allow computer programs to share
# data between each other over the internet/ a network

import requests
# modules are files of codes (objects with methods and perameters)
# with prewritten code to help us program

countryData = requests.get("https://restcountries.com/v3.1/all?fields=name.capital,currencies")

# JSON - JavaScript Object Notation
# this a object structed for computers and people to easily read
# short data.

print(countryData.json())
print(j)
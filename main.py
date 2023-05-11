# IP Location Finder using Python and Geocoder API.
# Date: 10/11/2022
# Version: 1.0
# Explanation: This program takes an IP address as input and returns the location of the IP address.

# modules required
import argparse
import requests, json
import sys
from sys import argv
import os

# arguments and parser

parser = argparse.ArgumentParser()
args = parser.parse_args()

# colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

# banner of script
# API used: https://ipgeolocation.io/
# API key: 4f5c3b5e4b5e4f5c3b5e4b5e4f5c3b5e

api = "https://ip-api.io/json/"

try:
        print("IP Location Finder made by Aayush Kumar (20BCY10045)")
        print("Enter the IP address to find the location of the IP address.")
        ip = input("\033[0;32mLocate The IP Address: \033[0;32m" )
        data = requests.get(api+ip).json()
        sys.stdout.flush()
        a = lgreen+bold
        b = lgreen+bold
        print("")
        print (a, "[Address IP]      >"  , data['ip'])
        print (a, "[Country Name]    >"  , data['country_name'])
        print (b, "[Region Name]     >"  , data['region_name'])
        print (b, "[City]            >"  , data['city'])
        print (b, "[Country Capital] >"  , data['countryCapital'])
        print (b, "[Country Code]    >"  , data['country_code'])
        print("")
        print (a, "[Time Zone]       >"  , data['time_zone'])
        print (a, "[Calling Code]    >"  , data['callingCode'])
        print (a, "[Currency]        >"  , data['currency'])
        print("")
        print (a, "[Organization]    >"  , data['organisation'])
        print (a, "[Latitude]        >"  , data['latitude'])
        print (b, "[Longitude]       >"  , data['longitude'])
        print ("")
        print (a, "[Suspicious IP]   >"  , data['suspiciousFactors'])
        print (" "+lgreen+bold)

except KeyboardInterrupt:
        print ('Keyboard interrupted'+lgreen)
        sys.exit(0)
except requests.exceptions.ConnectionError as e:
        print (red+"[~]"+"Check Your Connection and try again!"+clear)
sys.exit(1)

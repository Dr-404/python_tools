
import requests
import colorama
from colorama import Fore, Style
import json
from termcolor import colored, cprint
import pyfiglet

#My Banner

banner = pyfiglet.figlet_format("Real IP Finder", font = "slant"  )
cprint(banner, 'green', attrs=['blink'])
cprint("                                                 by Dr.404",'green',attrs=['blink'])

print()
# For colored Output

colorama.init(Style.BRIGHT)
blue = Fore.BLUE+Style.BRIGHT
green = Fore.GREEN+Style.BRIGHT
reset = Fore.RESET


# Requesting Input
cprint("Please edit the 'key' variable with your securityTrail API Key!!!! \n",'blue')
domain = str(input("Enter your domain : "))

# PLease type your API key in Key parameter
key = "mMj0B1p5L9onekkpAbnFOC57hMmcyc5S" # Edit this with your API key


# Requesting API json Data

url = "https://api.securitytrails.com/v1/history/"+domain+"/dns/a"
headers = {

    "Accept": "application/json",

    "APIKEY": key

}
response = requests.get(url, headers=headers)
response_json = response.json()
records = response_json['records']


# Extract Data and Print output
for record in records:
    #print(record.keys())
    for organization in record['organizations']:
        if str(organization) == "Cloudflare, Inc.":
            pass
        else:
            print(green+"This ip is last seen in :  ",blue+ record['last_seen']+reset)
            print(green+"The organization of Domain is :    ",blue+organization+reset)
            # ip_list = record['values']
            for ip_list in record['values']:
                print(green+"The"+Fore.RED+ " Real"+green+" ip of your domain may be : ",blue+ip_list['ip']+reset)
                print()




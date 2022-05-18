
import requests
import colorama
from colorama import Fore, Style
import json
from termcolor import colored, cprint
import pyfiglet


banner = pyfiglet.figlet_format("Real IP Finder", font = "slant"  )
#print(banner)

cprint(banner, 'green', attrs=['blink'])
cprint("                                                 by Dr.404",'green',attrs=['blink'])
colorama.init(Style.BRIGHT)


blue = Fore.BLUE+Style.BRIGHT
green = Fore.GREEN+Style.BRIGHT
reset = Fore.RESET


domain = str(input("Enter your domain : "))

key = "mMj0B1p5L9onekkpAbnFOC57hMmcyc5S"
url = "https://api.securitytrails.com/v1/history/"+domain+"/dns/a"
#print (url)
headers = {

    "Accept": "application/json",

    "APIKEY": "mMj0B1p5L9onekkpAbnFOC57hMmcyc5S"

}
response = requests.get(url, headers=headers)

response_json = response.json()


records = response_json['records']


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




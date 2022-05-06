import re
import requests



print("                                         ")
print("   ____     __   _____        __         ") 
print("  / ____ __/ /  / __(____ ___/ ___ ____  ")
print(" _\ \/ // / _ \/ _// / _ / _  / -_/ __/  ")
print("/___/\_,_/_.__/_/ /_/_//_\_,_/\__/_/     ")
print("                                         ")
print("                         +-+-+-+-+-+-+   ")
print("                         |D|r|.|4|0|4|   ")
print("                         +-+-+-+-+-+-+   ") 
print("                                         ") 

"""
First I make request to crt.sh to view certificate log
command ==> curl -X GET https://crt.sh/?q=nugmyanmar.org
"""

domain_name = input("Enter Domain Name : ")
print("\n")
prefix = "https://crt.sh/?q="

#matching subdomain using regex
pattern = str ("\w+\."+domain_name) #\w mean alphanumical

#Making request
sub_Raw= requests.get(prefix + domain_name)
result_Raw = str(sub_Raw.text)


# #Replacing and subsitube .org,.com,.edu with .com+newline
# char_to_replace = {".org":".org\n",
#                     ".com":".com\n",
#                     ".edu":".edu\n"
#                    }
#
# for key,value in char_to_replace.items():
#     result_Raw = result_Raw.replace(key,value)
# #result_Raw = result_Raw.replace(".org",".org\n")

patterm_www = "www." + domain_name





result_filter = re.findall(pattern, result_Raw)
result_list = []

for i in result_filter:

    result = i.replace("<BR>", "")
    result = result.replace("<TD>","")
    #print (result)

    result_list.append(result) # Dont use a = a.appnd(b) just use a.append(b)

result_rm_duplicate = list(set(result_list))

for resultFinal in result_rm_duplicate:
    if str(resultFinal) == str("www."+domain_name):
        pass
    else:
        print(resultFinal)



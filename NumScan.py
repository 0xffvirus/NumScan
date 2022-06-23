# coding=utf-8
import requests, os, sys
from termcolor import colored
os.system('color')
print(colored("""
███╗   ██╗██████╗  ██████╗ 
████╗  ██║╚════██╗██╔════╝ 
██╔██╗ ██║ █████╔╝███████╗ 
██║╚██╗██║ ╚═══██╗██╔═══██╗
██║ ╚████║██████╔╝╚██████╔╝
╚═╝  ╚═══╝╚═════╝  ╚═════╝                                     
""", 'red')),print(colored("@366f36", 'red'))
print("[ Only Saudi Numbers ]")
print("[ Don't Write +966 example : 558832003 ]")
usr = input(colored("Number >> ", 'cyan'))
def start(usr):
    try:
        url = "http://146.148.112.105/caller/index.php/UserManagement/search_number?number="+usr+"&country_code=SA"
        r = requests.get(url)
        num = str(r.json()['result'][0]['number'])
        name = str(r.json()['result'][0]['name']).encode("utf-8")
        country = str(r.json()['result'][0]['country_code'])
        id = str(r.json()['result'][0]['id'])
        print(colored("---- Coded By 6Virus ----", 'red'))
        print(colored("[!]", 'green'),colored("number :", 'cyan'),num)
        print(colored("[!]", 'green'),colored("name :",'cyan'),sys.stdout.buffer.write(name))
        print(colored("[!]", 'green'),colored("Country :", 'cyan'),country)
        print(colored("[!]", 'green'),colored("id :", 'cyan'),id)
        input("Press Any Key to Close ...")
    except:
        print(colored("[?]", 'red'),"Error Try Again")


start(usr)
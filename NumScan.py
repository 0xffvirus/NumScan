# -*- coding: utf-8 -*-
import requests
import os
from termcolor import colored
os.system('color')
print(colored("""
███╗   ██╗██████╗  ██████╗ 
████╗  ██║╚════██╗██╔════╝ 
██╔██╗ ██║ █████╔╝███████╗ 
██║╚██╗██║ ╚═══██╗██╔═══██╗
██║ ╚████║██████╔╝╚██████╔╝
╚═╝  ╚═══╝╚═════╝  ╚═════╝                                     
""", 'red')), print(colored("@366f36", 'red'))
print("[ Only Saudi Numbers ]")
print("[ Don't Write +966 example : 558832003 ]")


def start(usr):
    try:
        url = f"http://146.148.112.105/caller/index.php/UserManagement/search_number?number={usr}&country_code=SA"
        r = requests.get(url)  # GET Data from url

        # Decode Json Data recieved from the url
        num = str(r.json()['result'][0]['number'])
        name = str(r.json()['result'][0]['name'])
        country = str(r.json()['result'][0]['country_code'])
        id = str(r.json()['result'][0]['id'])
        # Printing the Data after decoding
        print(colored("---- Coded By 6Virus ----", 'red'))
        print(colored("[!]", 'green'), colored("number :", 'cyan'), num)
        print(colored("[!]", 'green'), colored("name :", 'cyan'), name)
        print(colored("[!]", 'green'), colored("Country :", 'cyan'), country)
        print(colored("[!]", 'green'), colored("id :", 'cyan'), id)
        input("Press Any Key to Close ...")
    except:
        # print error
        print(colored("[?]", 'red'), f"Error Try Again")


def check(usr):
    try:
        url = f"http://146.148.112.105/caller/index.php/UserManagement/search_number?number={usr}&country_code=SA"
        r = requests.get(url) # GET Data from url

        # Decode Json Data recieved from the url
        num = str(r.json()['result'][0]['number'])
        name = str(r.json()['result'][0]['name'])
        # Printing the Data after decodin
        print(colored("[!]", 'green'), num + " :", name)
    except:
        print(colored("[?]", 'red'), f"Error Try Again >> {usr}")


def listed():
    word = input("Wordlist : ") # Get File path
    print(colored("---- Coded By 6Virus ----", 'red'))
    with open(word, 'r') as usr:
        for tags in usr:
            # Get number by number
            tag = tags.strip()
            check(tag)


def options():
    print(colored("[1] One Number", "cyan"))
    print(colored("[2] List of Numbers", "cyan"))
    opt = input("Option : ")
    if opt == "1":
        usr = input(colored("Number >> ", 'cyan'))
        start(usr)
    elif opt == "2":
        listed()


options()

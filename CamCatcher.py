#!/usr/bin/env python3
# #-*- coding: utf-8 -*-
# https://github.com/Zrexer/camCatcher

import requests
import re 
from requests.structures import CaseInsensitiveDict
import time
import os 

os.system('')

class colors:
    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    yellow = '\033[93m'
    magenta = '\033[95m'
    cyan = '\033[96m'
    bold = '\033[1m'
    underline = '\033[4m'
    black='\033[30m'
    Backsilver='\033[100m'
    silver='\033[90m'
    Backwhite='\033[3m'
    Backgreen='\033[42m'
    Backyellow='\033[43m'
    BackBlue='\033[44m'
    Backpink='\033[45m'
    Backcyan='\033[46m'
    BackRed='\033[41m'
    green = '\033[32m' 
    red = '\033[31m' 
    blue = '\033[36m' 
    pink = '\033[35m' 
    yellow = '\033[93m' 
    darkblue = '\033[34m' 
    white = '\033[00m'
    bluo = '\033[34m'
    red_p = '\033[41m'
    green_p = '\033[42m'
    bluo_p = '\033[44m'
    pink_p = '\033[45m'
    blue_p = '\033[46m'
    white_p = '\033[47m'
    rd = '\033[91m'
    black='\033[30m'
    bold = '\033[1m'
    underline = '\033[4m'
    magenta = '\033[95m'
    
url = "http://www.insecam.org/en/jsoncountries/"

headers = CaseInsensitiveDict()
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
headers["Host"] = "www.insecam.org"
headers["Upgrade-Insecure-Requests"] = "1"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"


class CamCatcher:
    
    numberOFIP = 0
    numberOFIPx = 0
    
    def getCountries():
        try:

            resp = requests.get(url, headers=headers)

            data = resp.json()
            countries = data['countries']
            for key, value in countries.items():
                coTime = time.strftime("%H:%M:%S")
                print(f'\n{colors.white}[{colors.red}{coTime}{colors.white}] [{colors.green}info{colors.white}] {colors.bold}key{colors.white}: ({colors.underline}{key}{colors.white}) - {colors.bold}{value["country"]}{colors.white} : ({colors.BackRed}{value["count"]}{colors.white})\n')
        except Exception as EGC:
            print(f"\n{colors.white}{colors.BackRed}Error{colors.white}: {EGC}")
            pass
    
    def findIPS(countryCode):
        try:
            res = requests.get(
                f"http://www.insecam.org/en/bycountry/{countryCode}", headers=headers
            )
            last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

            for page in range(int(last_page)):
                res = requests.get(
                    f"http://www.insecam.org/en/bycountry/{countryCode}/?page={page}",
                    headers=headers
                )
                find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
                

                
                for ip in find_ip:
                    CamCatcher.numberOFIP += 1
                    print(f'\n{colors.white}[{colors.green}{CamCatcher.numberOFIP}{colors.white}] {colors.red}{ip}')
        except Exception as EFI:
            print(f"\n{colors.white}{colors.BackRed}Error{colors.white}: {EFI}")
            pass

    def findAndSaveIPS(countryCode, nameFile):
        try:
            res = requests.get(
                f"http://www.insecam.org/en/bycountry/{countryCode}", headers=headers
            )
            last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

            for page in range(int(last_page)):
                res = requests.get(
                    f"http://www.insecam.org/en/bycountry/{countryCode}/?page={page}",
                    headers=headers
                )
                find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
                
                for ip in find_ip:
                    
                    with open(nameFile, 'a') as save_find_ips:
                        save_find_ips.write(f'\n{ip}')
                    
                    CamCatcher.numberOFIPx += 1
                    print(f'\n{colors.white}[{colors.green}{CamCatcher.numberOFIPx}{colors.white}] {colors.red}{ip}')
                
        except Exception as EFASI:
            print(f"\n{colors.white}{colors.BackRed}Error{colors.white}: {EFASI}")
            pass
        
        finally:
            finnalyTime = time.strftime('%H:%M:%S')
            print(f'\n{colors.white}[{colors.red}{finnalyTime}{colors.white}] [{colors.green}info{colors.white}]{colors.yellow} ips saved in : {colors.red}{nameFile}')

class Helper:
    def commands(numberDict):
        dictX = {
            'commands' : [
                {
                    'command' : 'help',
                    'info' : "show this message",
                    'usage' : 'type " help "'
                },
                {
                    'command' : 'cams',
                    'info' : 'show avalaible cams to Catch',
                    'usage' : 'type " cams "'
                },
                {
                    'command' : 'catch',
                    'info' : 'get the country code Cams',
                    'usage' : 'catch #<country code> : catch IR'
                },
                {
                    'command' : 'exit',
                    'info' : 'exit and close the program',
                    'usage' : 'type " exit "'
                }
            ]
        }
        
        return dictX['commands'][numberDict]
    
    def banner():
        return f"""{colors.red}

 __ {colors.cyan}        {colors.red}__ {colors.cyan}    ,  {colors.red}__ {colors.cyan}.             {colors.yellow}({colors.BackRed}C{colors.white}{colors.yellow}){colors.red}
/  `{colors.cyan}_.._ _ {colors.red}/  `{colors.cyan} _.-+-{colors.red}/  `{colors.cyan}|_  _ ._.     {colors.yellow}({colors.BackRed}C{colors.white}{colors.yellow}){colors.red}
\__.{colors.cyan}( ][ |){colors.red}\__.{colors.cyan}(_] |{colors.red} \__.{colors.cyan}[ )(/,[       {colors.yellow}({colors.BackRed}C{colors.white}{colors.yellow}){colors.red}
{colors.white}
"""

    def Loading(msg, for_):
        party = ['< ', "_", "^", " >"]
        for i in range(for_):
            for p in party:
                print(f'\r{msg} {p}', end="")
                time.sleep(0.08)
        print()

class ConsoleHandler:
    def MainActivity():
        checkUpdateTime = time.strftime('%H:%M:%S')
            
        print(Helper.banner())
            
        Helper.Loading(msg=f'{colors.white}[{colors.red}{checkUpdateTime}{colors.white}] [{colors.green}info{colors.white}]{colors.yellow} Checking for updates', for_=15)

        startTime = time.strftime("%H:%M:%S")
        print(f"{colors.white}[{colors.red}{startTime}{colors.white}] [{colors.green}info{colors.white}]{colors.yellow} Welcome to {colors.red}CamCatcher{colors.yellow} , for see results type ' {colors.red}help {colors.yellow}'")
        
        while 1:
                 
            user = str(input(f"\n{colors.white}{colors.underline}CamCatcher{colors.white} > "))
            if user == "help":
                numberList = [0, 1, 2, 3]
                for numlist in numberList:
                    helpCommandTime = time.strftime('%H:%M:%S')
                    command = Helper.commands(numlist).get('command')
                    infoCommand = Helper.commands(numlist).get('info')
                    usageCommand = Helper.commands(numlist).get('usage')
                    print(f'\n{colors.white}[{colors.red}{helpCommandTime}{colors.white}] [{colors.Backpink}help{colors.white}] command : {colors.yellow}{command}\n{colors.white}[{colors.red}{helpCommandTime}{colors.white}] [{colors.Backpink}help{colors.white}] info : {colors.yellow}{infoCommand}\n{colors.white}[{colors.red}{helpCommandTime}{colors.white}] [{colors.Backpink}help{colors.white}] usage : {colors.yellow}{usageCommand}')

                print(f'\n{colors.white}[{colors.red}{helpCommandTime}{colors.white}] [{colors.BackRed}note{colors.white}] for save ips in a file :{colors.yellow} catch US -s / catch US --save {colors.white}=> ips save in {colors.red}ip200.txt{colors.white}and for set{colors.BackRed}name{colors.white} {colors.BackRed}file{colors.white} : {colors.yellow}catch US -s ips.txt / catch US --save ips.txt')
                    
            elif "cams" in user.split():
                CamCatcher.getCountries()
            
            elif "catch" in user.split():
                
                if user.split()[-2] == "--save" or user.split()[-2] == "-s":
                    fileNameToSave = user.split()[-1]
                    countryCode = user.split()[user.split().index('catch')+1]
                    CamCatcher.findAndSaveIPS(countryCode=countryCode, nameFile=fileNameToSave)
                    
                elif user.split()[-1] == "--save" or user.split()[-1] == "-s":
                    countryCode = user.split()[user.split().index('catch')+1]
                    CamCatcher.findAndSaveIPS(countryCode=countryCode, nameFile='ip200.txt')
                    
                else:
                    countryCode = user.split()[user.split().index('catch')+1]
                    CamCatcher.findIPS(countryCode=countryCode)
                    
            elif "exit" in user.split():
                exit()

if __name__ == "__main__":
    ConsoleHandler.MainActivity()

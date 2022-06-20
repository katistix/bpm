import os
import commands.getConfig as GET
from colorama import Fore
from colorama import Style

def list():
    for root, dirs, files in os.walk('boxes'):
        for directory in dirs:
            ver = "@v" + GET.read(directory)['version'] if 'version' in GET.read(directory) else ''
            description = GET.read(directory)['description'] if 'description' in GET.read(directory) else 'No description'
            print(f'{Fore.LIGHTYELLOW_EX}'+directory+f'{Style.RESET_ALL}' + '\t\t' + ver + "\t\t" + description)
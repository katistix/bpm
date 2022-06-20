import os
import commands.getConfig as GET
from colorama import Fore
from colorama import Style

def list():
    if len(os.listdir('boxes')) == 0:
        print(f'\n📦 No boxes installed')
        return
    for root, dirs, files in os.walk('boxes'):
        for directory in dirs:
            ver = "@v" + GET.read(directory)['version'] if 'version' in GET.read(directory) else ''
            description = GET.read(directory)['description'] if 'description' in GET.read(directory) else 'No description'
            print(f'{Fore.LIGHTYELLOW_EX}{directory}{Fore.LIGHTCYAN_EX} {ver}{Style.RESET_ALL}: {description}')
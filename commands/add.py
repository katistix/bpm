# To view https://api.github.com/repos/Box-Package-Manager/py_example/git/trees/master?recursive=1

import requests
import subprocess
import os
import json

def safeWrite(path, r):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'wb').write(r)

def getFileList(box, branch):
    url = f'https://api.github.com/repos/{box}/git/trees/{branch}?recursive=1'
    r = requests.get(url, allow_redirects=True)
    if r.status_code == 200:
        tree = r.json()['tree']
        filelist = []
        for file in tree:
            if file['type'] == 'blob':
                filelist.append(file['path'])
        return filelist
    else:
        return None

def getBoxIgnore(REPOSERVER, boxFolder):
    url = f'{REPOSERVER}/.boxignore'
    r = requests.get(url, allow_redirects=True)
    if not r.status_code == 200:
        print('\n⚠️ .boxignore not found, creating an empty one\n')
        safeWrite(boxFolder+'/.boxignore', b'# All files in this folder will be ignored when installing the box\n')
        return False
    else:
        ignorelist = []
        print('\n⚡ .boxignore found! Ignoring:')
        for line in r.text.splitlines():
            if line.startswith("#") or line.isspace():
                continue
            print(line)
            ignorelist.append(line)
        print()
        return ignorelist



def add(box):

    # Decide which repo to use
    if not '/' in box: # If using default repo
        repouser = 'Box-Package-Manager'
    else:
        repouser = box.split('/')[0]
        box = box.split('/')[1]
    
    # Decide which branch to use
    if not '@' in box: # If using default branch
        branch = 'HEAD'
    else:
        branch = box.split('@')[1]

    REPOSERVER = f"https://raw.githubusercontent.com/{repouser}/{box}/{branch}"

    # Check if box is already installed
    boxFolder = 'boxes/' + box
    if os.path.exists(boxFolder):
        print('📦 Box already installed')
        return

    # Get the 'files'
    filelist = getFileList(f'{repouser}/{box}', branch)
    print(f'🔍 Checking if repository is available at {REPOSERVER}')
    if filelist is None:
        print('❌ Repository not found')
        return
    else:
        print('✅ Repository found!\n\n🪛 Installing...\n')
        boxignore_files = getBoxIgnore(REPOSERVER, boxFolder)
        if boxignore_files is False:
            boxignore_files = []
        for file in filelist:
            if file in boxignore_files:
                continue
            url = f'{REPOSERVER}/{file}'
            r = requests.get(url, allow_redirects=True)
            safeWrite(boxFolder+'/'+file, r.content)
            print(f'Added: {file}')

    
    # Get the '.boxinstall'
    url = f'{REPOSERVER}/.boxinstall'
    r = requests.get(url, allow_redirects=True)
    if not r.status_code == 200:
        print('\n⚠️ .boxinstall not found, creating an empty one')
        safeWrite(boxFolder+'/.boxinstall', b'# All theese commands will run when installing the box\n')

    else:
        print('\n✅ .boxinstall found!')
        print('🪛 Running boxinstall ...')
        for line in r.text.splitlines():
            if line.startswith("#") or line.isspace() or not line.strip():
                continue
            print(f'\n⚡ .boxinstall: {line}')
            p = subprocess.Popen(line, cwd="boxes/"+box, shell=True)
            p.wait()
    

    # Get the 'box_config.json'
    url = f'{REPOSERVER}/box_config.json'
    r = requests.get(url, allow_redirects=True)
    if not r.status_code == 200:
        if not input('\n⚠️ box_config.json not found\n\nDo you want to create one? (Y/n) ').lower() == 'n':
            version = input('Version: ').replace('\\', '\\\\').replace('"', '\\"')
            description = input('Description: ').replace('\\', '\\\\').replace('"', '\\"')
            run = input('Run Command: ').replace('\\', '\\\\').replace('"', '\\"')
            config = '{\n\t'+ f'"version": "{version}",\n\t' + f'"description": "{description}",\n\t' + f'"run": "{run}"\n' + '}'
            safeWrite(boxFolder+'/box_config.json', config.encode())
            print('\n✅ box_config.json created!')
    else:
        print('\n✅ box_config.json found!')

    print('\n🎉 Box installed!')
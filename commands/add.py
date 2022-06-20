# To view https://stackoverflow.com/questions/23793987/write-file-to-a-directory-that-doesnt-exist

import requests
import subprocess
import os

def safeWrite(path, r):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'wb').write(r.content)


def add(box):

    # Decide which repo to use
    if not '/' in box: # If using default repo
        repouser = 'Box-Package-Manager'
    else:
        repouser = box.split('/')[0]
        box = box.split('/')[1]

    REPOSERVER = f"https://raw.githubusercontent.com/{repouser}/{box}/master"

    # Check if box is already installed
    boxFolder = 'boxes/' + box
    if os.path.exists(boxFolder):
        print('📦 Box already installed')
        return

    # Check if box is available in repo
    print(f'🔍 Checking if box is available at {REPOSERVER}/boxfiles')
    r = requests.get(f'{REPOSERVER}/boxfiles')
    if r.status_code == 200:
        print('✅ Box found!\n\n🪛 Installing...\n')
        # Create box folder
        os.mkdir(boxFolder)

    else:
        print('❌ Box not found')
        return


    # Get the 'files'
    url = f'{REPOSERVER}/boxfiles'
    r = requests.get(url, allow_redirects=True)
    files = r.text.splitlines()
    for file in files:
        if file.startswith("#") or file.isspace() or not file.strip():
            continue
        # Download file
        url = f'{REPOSERVER}/{file}'
        r = requests.get(url, allow_redirects=True)
        safeWrite(boxFolder+'/'+file, r)
        print(f'Added: {file}')
    
    # Get the 'boxinstall'
    url = f'{REPOSERVER}/boxinstall'
    r = requests.get(url, allow_redirects=True)
    if not r.status_code == 200:
        print('\n⚠️ boxinstall not found, skipping')
    else:
        print('\n✅ boxinstall found!')
        print('🪛 Running boxinstall ...')
        for line in r.text.splitlines():
            if line.startswith("#") or line.isspace() or not line.strip():
                continue
            print(f'\n⚡ boxinstall: {line}')
            p = subprocess.Popen(line, cwd="boxes/"+box, shell=True)
            p.wait()
    
    print('\n🎉 Box installed!')
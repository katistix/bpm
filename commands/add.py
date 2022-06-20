import requests
import subprocess
import os

# REPOSERVER = 'https://raw.githubusercontent.com/katistix/bpm_boxes/master/'
REPOSERVER = 'http://localhost:3000/boxes_repo/'

def add(box):

    # Check if box is already installed
    boxFolder = 'boxes/' + box
    if os.path.exists(boxFolder):
        print('📦 Box already installed')
        return

    # Check if box is available in repo
    print(f'🔍 Checking if box is available at {REPOSERVER}{box}/files')
    r = requests.get(f'{REPOSERVER}{box}/files')
    if r.status_code == 200:
        print('✅ Box found!\n\n🪛 Installing...\n')
        # Create box folder
        os.mkdir(boxFolder)

    else:
        print('❌ Box not found')
        return


    # Get the 'files'
    url = f'{REPOSERVER}{box}/files'
    r = requests.get(url, allow_redirects=True)
    files = r.text.splitlines()
    for file in files:
        if file.startswith("#") or file.isspace() or not file.strip():
            continue
        # Download file
        url = f'{REPOSERVER}{box}/{file}'
        r = requests.get(url, allow_redirects=True)
        open('boxes/'+box+'/'+file, 'wb').write(r.content)
        print(f'Added: {file}')
    
    # Get the 'boxinstall'
    url = f'{REPOSERVER}{box}/boxinstall'
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
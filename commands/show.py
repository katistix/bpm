import subprocess
import os

def show(box):
    # Check if box is installed
    boxFolder = 'boxes/' + box
    if not os.path.exists(boxFolder):
        print('❌ Box not installed')
        return
    # Open explorer to box folder
    print('📦 Opening box folder...')
    subprocess.Popen(f'explorer boxes\\{box}')
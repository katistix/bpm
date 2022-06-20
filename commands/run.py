import subprocess
import os
import commands.getConfig as GET
import sys


def run(box):
    # Check if box exists
    if not os.path.exists('boxes/' + box):
        print('📦 Box is not installed')
        return
    cmd = GET.read(sys.argv[2])['run']
    p = subprocess.Popen(cmd, cwd="boxes/"+box, shell=True)
    p.wait()
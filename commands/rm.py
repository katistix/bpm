import shutil
import os

def rm(boxToRemove):
    # Check if box exists
    if not os.path.exists('boxes/' + boxToRemove):
        print('📦 Box does not exist')
        return

    # Ask for confirmation
    confirmation = input("Are you sure you want to remove " + boxToRemove + "? (y/N) ")
    if confirmation.lower() == 'y':
        shutil.rmtree('boxes/'+boxToRemove, ignore_errors=True)
        print("✅ Removed " + boxToRemove)
    else:
        print("❌ Aborted")
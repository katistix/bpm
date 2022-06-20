import sys
import os


# Commands
import commands.add as ADD
import commands.list as LIST
import commands.rm as RM
import commands.run as RUN
import commands.getConfig as GET

COMMAND = sys.argv[1]
helpText = """🔜 Soon to be implemented"""

if __name__ == '__main__':
    
    
    if COMMAND == 'h' or COMMAND == 'help':
        print(helpText)

    elif COMMAND == 'install' or COMMAND == 'add':
        ADD.add(sys.argv[2])
    
    elif COMMAND == 'rm' or COMMAND == 'remove':
        RM.rm(sys.argv[2])
    
    elif COMMAND == 'list' or COMMAND == 'ls':
        LIST.list()
    
    elif COMMAND == 'update':
        print('🔜 Soon to be implemented')
    
    
    elif COMMAND == 'r' or COMMAND == 'run':
        RUN.run(sys.argv[2])

    
    
    else:
        print('❌ Unknown command')

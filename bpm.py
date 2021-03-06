import sys
import os


# Commands
import commands.add as ADD
import commands.list as LIST
import commands.rm as RM
import commands.run as RUN
import commands.getConfig as GET
import commands.show as SHOW
import commands.init as INIT

COMMAND = sys.argv[1]
helpText = """🔜 Soon to be implemented"""

if __name__ == '__main__':
    
    
    if COMMAND == 'h' or COMMAND == 'help':
        print(helpText)
    elif COMMAND == 'init':
        INIT.init()

    elif COMMAND == 'install':
        ADD.add(sys.argv[2])
    

    elif COMMAND == 'rm' or COMMAND == 'remove':
        RM.rm(sys.argv[2])
    
    elif COMMAND == 'list' or COMMAND == 'ls':
        LIST.list()
    
    elif COMMAND == 'update' or COMMAND == 'u':
        print('🔜 Soon to be implemented')
    
    elif COMMAND == 'show':
        SHOW.show(sys.argv[2])
    
    elif COMMAND == 'r' or COMMAND == 'run':
        RUN.run(sys.argv[2])

    
    
    else:
        print('❌ Unknown command')

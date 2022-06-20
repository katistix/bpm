import os

boxfiles = """# Add more files here
box_config.json
"""

boxinstall = '# Commands to run at installation'


def init():
    if os.path.exists('box_config.json'):
        print('✅ box_config.json already exists')
    else:
        version = input('Version: ')
        description = input('Description: ')
        run = input('Run Command: ')
        boxconfig_json = '{\n\t'+ f'"version": "{version}",\n\t' + f'"description": "{description}",\n\t' + f'"run": "{run}"\n' + '}'

        with open('box_config.json', 'w') as f:
            f.write(boxconfig_json)
        print('✅ box_config.json created')
    
    if os.path.exists('boxfiles'):
        print('✅ boxfiles already exists')
    else:
        with open('boxfiles', 'w') as f:
            f.write(boxfiles)
        print('✅ boxfiles created')
    
    if os.path.exists('boxinstall'):
        print('✅ boxinstall already exists')
    else:
        with open('boxinstall', 'w') as f:
            f.write(boxinstall)
        print('✅ boxinstall created')

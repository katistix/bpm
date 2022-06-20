import os

boxconfig_json = """
{
    "version": "0.0.1",
    "description": "",
    "run": ""
}
"""

boxfiles = """
# Add more files here
box_config.json
"""

boxinstall = """
# Command to run at installation
"""

def init():
    if os.path.exists('box_config.json'):
        print('✅ box_config.json already exists')
    else:
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

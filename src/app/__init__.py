# V1.0.0

from rich.console import Console
import json
import sys

def json_data(JSON_FILE):
    with open(JSON_FILE, 'r') as file:
        data_content = json.load(file)

    name = data_content['productName']
    version = data_content['version']
    license = data_content['license']

    return name, version, license

class ProgramConsole:
    def __init__(self, console, name, version, license):
        super().__init__()

        self.name = name
        self.version = version
        self.license = license

        console.print(f"""{name} - {version}

{name} is a free and open-source project assistant that makes it easy for you to create your projects.
It was developed entirely in python and is reserved especially for projects containing python code.
Compatibility issues may occur if your project is not primarily developed in python.

If you are new we recommend you to enter the command "help".

""")
        
        while True:
            prompt = console.input('> ')
            ProgramConsole.commands_management(console, prompt, license)

    def commands_management(console, prompt, license):
        if prompt == 'help':
            console.print(f"\n======================COMMANDS======================\nhelp / license / credits /\ncreate (project/backup) / load backup / shutdown /\ndelete (data/project/backup)")
        elif prompt == 'license':
            console.print(f"\n{license}\n")
        elif prompt == 'credits':
            console.print(f"\nCredits : KDUser12\n")
        elif prompt.startswith('create'):
            if 'project' in prompt:
                exec(open('app/packages/create_project.py').read())
            elif 'backup' in prompt:
                exec(open('app/packages/create_backup.py').read())
        elif prompt.startswith('load'):
            if 'backup' in prompt:
                exec(open('app/packages/load_backup.py').read())
        elif prompt.startswith('delete'):
            if 'data' in prompt:
                exec(open('app/packages/delete_data.py').read())
            elif 'project' in prompt:
                exec(open('app/packages/delete_project.py').read())
            elif 'backup' in prompt:
                exec(open('app/packages/delete_backup.py').read())
        elif prompt == 'shutdown':
            sys.exit(1)
        else:
            console.print("Error", "Please enter a valid command.")

        
if __name__ == '__main__':
    sys.dont_write_bytecode = True
    JSON_FILE = 'app/cache/app_config.json'
    name, version, license = json_data(JSON_FILE)

    console = Console()
    ProgramConsole(console, name, version, license)
import sys
import json

def json_data(JSON_FILE_PATH):
    with open(JSON_FILE_PATH, 'r') as json_file:
        data = json.load(json_file)

    name = data['productName']
    version = data['version']

    return name, version

class Console:
    def __init__(self, name, version):
        super().__init__()
        
        self.name = name
        self.version = version

        print(f"{name} - {version}\n")
        print(f"{name} is a free open-source python project assistant.")
        print("If you are new we advise you to type the command \"help\".\n\n")
        
        while True:
            prompt = input('> ')
            Console.commands_management(prompt)
        
    def commands_management(prompt):
        if prompt == 'help':
            commands = [
                {
                    "command": "help",
                },
                {
                    "command": "license",
                },
                {
                    "command": "startproject",
                },
                {
                    "command": "shutdown"
                }
            ]

            print("==========Commands==========")
            for command in commands:
                print(f"{command['command']}")

        elif prompt == 'license':
            print("MIT License")

        elif prompt == "startproject":
            exec(open('app/packages/startproject.py').read())

        elif prompt == 'shutdown':
            sys.exit()
        
    
if __name__ == "__main__":
    sys.dont_write_bytecode = True
    JSON_FILE_PATH = 'app/cache/config.json'

    name, version = json_data(JSON_FILE_PATH)
    Console(name, version)
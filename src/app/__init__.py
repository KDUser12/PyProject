import cmd
import json
import sys

def JSON_data():
    JSON_FILE_PATH = "app/cache/config.json"
    with open(JSON_FILE_PATH, "r") as json_file:
        data = json.load(json_file)

    name = data['productName']
    version = data['version']

    return name, version

class Console(cmd.Cmd):
    prompt = "> "

    def __init__(self, name, version):
        super().__init__()
        self.name = name
        self.version = version

        print(f"{name} - {version}\n")
        print(f"{name} is a free open-source python project assistant.")
        print("If you are new we advise you to type the command \"help\".")

    def do_help(self, arg: str) -> bool | None:
        return super().do_help(arg)
    
    def do_license(self, arg):
        print("MIT License\n")

    def do_startproject(self, arg):
        exec(open("app/packages/startproject.py").read())
    
    def do_shutdown(self, arg):
        return True

if __name__ == "__main__":
    sys.dont_write_bytecode = True
    name, version = JSON_data()
    app = Console(name, version)
    app.cmdloop()
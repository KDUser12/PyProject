__versions__ = "2.0.0-beta"
__file__ = "PyProject.py"


import json
import os
import sys


basic_commands = ["help", "license", "shutdown"]


def collect_json_data():
    if os.path.exists("cache/configuration.json"):
        with open("cache/configuration.json", "r") as config_json:
            data = json.load(config_json)
        return data
    else:
        print("An error has occurred: Error Code 001")
        sys.exit("001")


class CommandExecutor:
    def __init__(self):
        self.data = collect_json_data()
        self.license = self.data["license"]
        self.prompt = None

        print("PyProject - {}\n".format(__versions__))
        print("PyProject is a program to facilitate the initial creation of a project generating the fundamental\n"
              "structure including folders, files and required configurations.")
        print('To learn more enter the "help" command.')

        CommandExecutor.command_input(self)

    def command_input(self):
        while True:
            try:
                while True:
                    self.prompt = input("\n> ")
                    CommandExecutor.basic_command_manage(self)
            except KeyboardInterrupt:
                print("An error has occurred: Error Code 002")
                sys.exit(2)

    def basic_command_manage(self):
        if self.prompt in basic_commands:
            if self.prompt == "help":
                print("\nHere is the list of available commands: ")
                for cmd in basic_commands:
                    print("- {}".format(cmd))
            elif self.prompt == "license":
                print(self.license)
            elif self.prompt == "shutdown":
                sys.exit(0)


if __name__ == "__main__":
    CommandExecutor()

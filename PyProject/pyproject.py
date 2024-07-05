import os

from utils.version import get_version
from utils.github import get_latest_version


class Commands:
    def __init__(self):
        self.prompt = None
        self.directory = None

    def call_command(self):
        while True:
            self.prompt = input("[~{}] >")

def main():
    version = get_version((2, 0, 0, "beta", 0))
    latest_version = get_latest_version("PyProject", "v{}".format(version))
    os.system("cls" if os.name == "nt" else "clear")
    
    print("PyProject - {}\n".format(version))
    print("PyProject is a program to facilitate the initial creation of a project by generating the structure basic"
          "including folders, files and required configurations. \nTo learn more, enter the \"help\" command.")

    if version != latest_version:
        print("\nThe new version {} is available. You can now update your program.".format(latest_version))


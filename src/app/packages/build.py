import configparser
import os

from app.packages.builds.setup_content import setup_content

class BuildProject:
    def build_project(_directory):
        print("Creating folders and files in progress...")

        try:
            setup_file = open(f"{_directory}/setup.py", 'w')
            setup_file.write(setup_content)
            setup_file.close()

            requirements_file = open(f"{_directory}/requirements.txt", 'w')

            os.mkdir(f"{_directory}/src")
            os.mkdir(f"{_directory}/src/app")
            os.mkdir(f"{_directory}/src/app/cache")
            os.mkdir(f"{_directory}/src/app/packages")

            main_content = open("app/packages/builds/main_content.txt").read()
            main_file = open(f"{_directory}/src/main.py", 'w')
            main_file.write(main_content)
            main_file.close()
            
            __init___content = open("app/packages/builds/__init___content.txt").read()
            __init___file = open(f"{_directory}/src/app/__init__.py", 'w')
            __init___file.write(__init___content)
            __init___file.close()

            
            os.mkdir(f"{_directory}/docs")
            os.mkdir(f"{_directory}/docs/user_manual")
            os.mkdir(f"{_directory}/docs/documentation")

            os.mkdir(f"{_directory}/.github")

            print("Creating folders and files completed!")
            return True
        except OSError as error:
            print("An error occurred when creating the file :", error)
            return False

    def check_data(_directory):
        if not os.path.exists(_directory):
            print("The directory you have chosen does not exist, do you want to create it?")
            if input("[Y] [N]\n> ") == "y":
                try:
                    os.makedirs(_directory)
                    return True
                except OSError as error:
                    print("An error occurred when creating the file :", error)
                    return False
            return False
        return True

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("app/cache/temps/config.config")
    _directory = config.get("Configuration", "directory")
    
    if BuildProject.check_data(_directory):
        BuildProject.build_project(_directory)
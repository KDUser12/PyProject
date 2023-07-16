import json
import os

def json_data(JSON_FILE_PATH):
    with open(JSON_FILE_PATH, 'r') as json_file:
        data = json.load(json_file)

    name = data['name']
    version = data['version']
    authors = data['authors']
    description = data['description']
    directory = data['directory']

    return name, version, authors, description, directory

class BuildProject:
    def build_project(name, version, authors, description, directory):
        print("Creating folders and files in progress...")

        try:
            setup_content = f"""

from setuptools import setup, find_packages

setup(
    name='{name}',
    version='{version}',
    author='{authors}',
    description='{description}',
    packages=find_packages(),
)

"""
            
            setup_file = open(f"{directory}/setup.py", 'w')
            setup_file.write(setup_content)
            setup_file.close()

            requirements_file = open(f"{directory}/requirements.txt", 'w')

            os.mkdir(f"{directory}/src")
            os.mkdir(f"{directory}/src/app")
            os.mkdir(f"{directory}/src/app/cache")
            os.mkdir(f"{directory}/src/app/packages")

            main_content = open("app/packages/builds/main_content.txt").read()
            main_file = open(f"{directory}/src/main.py", 'w')
            main_file.write(main_content)
            main_file.close()
            
            __init___content = open("app/packages/builds/__init___content.txt").read()
            __init___file = open(f"{directory}/src/app/__init__.py", 'w')
            __init___file.write(__init___content)
            __init___file.close()

            
            os.mkdir(f"{directory}/docs")
            os.mkdir(f"{directory}/docs/user_manual")
            os.mkdir(f"{directory}/docs/documentation")

            os.mkdir(f"{directory}/.github")

            print("Creating folders and files completed!")
            return True
        except OSError as error:
            print("An error occurred when creating the file :", error)
            return False

    def check_data(directory):
        if not os.path.exists(directory):
            print("The directory you have chosen does not exist, do you want to create it?")
            if input("[Y] [N]\n> ") == "y":
                try:
                    os.makedirs(directory)
                    return True
                except OSError as error:
                    print("An error occurred when creating the file :", error)
                    return False
            return False
        return True

if __name__ == "__main__":
    JSON_FILE_PATH = 'app/cache/project-config.json'
    name, version, authors, description, directory = json_data(JSON_FILE_PATH)
    
    if BuildProject.check_data(directory):
        BuildProject.build_project(name, version, authors, description, directory)
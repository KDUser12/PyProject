import json
import os
from datetime import datetime

def json_data(JSON_FILE):
    with open(JSON_FILE, 'r') as file:
        data_content = json.load(file)

    name = data_content['name']
    version = data_content['version']
    authors = data_content['authors']
    description = data_content['description']
    project_directory = data_content['project_directory']

    return name, version, authors, description, project_directory

class BuildProject:
    def create_project(name, version, authors, description, project_directory):
        try:
            print(f"[{datetime.now()}] : Creation of the contents of the setup.py file")
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
            
            print(f"[{datetime.now()}] : Creation of the setup.py file")
            with open(f'{project_directory}/setup.py', 'w') as file:
                file.write(setup_content)

            print(f"[{datetime.now()}] : Creation of the requirements.txt file")
            with open(f'{project_directory}/requirements.txt', 'w') as file:
                file.write('')

            print(f"[{datetime.now()}] : Creating src, app and cache folders")
            os.makedirs(f'{project_directory}/src/app/cache')
            
            print(f"[{datetime.now()}] : Creation of packages folders")
            os.mkdir(f'{project_directory}/src/app/packages')

            print(f"[{datetime.now()}] : Creating the contents of the main.py file")
            with open('app/packages/builds/main_content.txt', 'r') as file:
                main_content = file.read()

            print(f"[{datetime.now()}] : Creating the main.py file")
            with open(f'{project_directory}/src/main.py', 'w') as file:
                file.write(main_content)

            print(f"[{datetime.now()}] : Creating the contents of the __init__.py file")
            with open('app/packages/builds/__init___content.txt', 'r') as file:
                __init___content = file.read()

            print(f"[{datetime.now()}] : Creating the __init__.py file")
            with open(f'{project_directory}/src/app/__init__.py', 'w') as file:
                file.write(__init___content)

            print(f"[{datetime.now()}] : Creating docs and user_manual folders")
            os.makedirs(f"{project_directory}/docs/user_manual")
            
            print(f"[{datetime.now()}] : Creation of documentation folder")
            os.mkdir(f'{project_directory}/docs/documentation')

            print(f"[{datetime.now()}] : Creating the .github folder")
            os.mkdir(f'{project_directory}/.github')

            print(f"[{datetime.now()}] : Project creation completed!")

        except OSError as error:
            print(f"[{datetime.now()}] : An error occurred when creating the project:", error)

    def check_project_directory(project_directory):
        try:
            if not os.path.exists(project_directory):
                print("The project directory you entered does not exist, do you want to create it?")
                if input('[Y] [N]\n> ') == 'y':
                    os.makedirs(project_directory)
                    return True
                return False
            return True
        except OSError as error:
            print(f"[{datetime.now()}] : An error occurred when creating the folder:", error)

if __name__ == '__main__':
    JSON_FILE = 'app/cache/project_data/project_config.json'
    name, version, authors, description, project_directory = json_data(JSON_FILE)

    if BuildProject.check_project_directory(project_directory):
        BuildProject.create_project(name, version, authors, description, project_directory)
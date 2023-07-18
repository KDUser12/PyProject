from datetime import datetime
import os

class CreateProject:
    def config_project():
        name = input('Project Name: ')
        product_name = input('Product Name: ')
        version = input('Version: ')
        description = input('Description : ')
        authors = input('Authors: ')
        project_directory = input('Project Directory: ')
        backup_directory = input('Backup Directory: ')

        return name, product_name, version, description, authors, project_directory, backup_directory

    def create_json_file(name, product_name, version, description, authors, project_directory, backup_directory, FILE_PATH):
        print(f"[{datetime.now()}] : JSON file creation in progress...")

        os.makedirs('app/cache/project_data')

        json_file_content = f"""

{{
    "name": "{name}",
    "productName": "{product_name}",
    "version": "{version}",
    "description": "{description}",
    "authors" : "{authors}",
    "project_directory": "{project_directory}",
    "backup_directory": "{backup_directory}"
}}

"""     
        
        with open(FILE_PATH, 'w') as file:
            file.write(json_file_content)

        print(f"[{datetime.now()}] : JSON file creation completed !")
        exec(open("app/packages/build_project.py").read())

if __name__ == '__main__':
    FILE_PATH = 'app/cache/project_data/project_config.json'

    name, product_name, version, description, authors, project_directory, backup_directory = CreateProject.config_project()
    CreateProject.create_json_file(name, product_name, version, description, authors, project_directory, backup_directory, FILE_PATH)
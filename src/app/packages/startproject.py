
class StartProject:
    def configuration():
        name = input("Name : ")
        product_name = input("Product Name : ")
        version = input("Version : ")
        description = input("Description : ")
        authors = input("Authors : ")
        directory = input("Directory : ")

        return name, product_name, version, description, authors, directory
    
    def create_configuration_file(name, product_name, version, description, authors, directory, FILE_PATH):
        print("Configuration file creation in progress...")

        json_content_data = f"""

{{
    "name": "{name}",
    "productName": "{product_name}",
    "version": "{version}",
    "description": "{description}",
    "authors" : "{authors}",
    "directory": "{directory}"
}}

"""     
        with open(FILE_PATH, 'w') as config_file:
            config_file.write(json_content_data)
        
        print("Création du fichier terminé !")
        exec(open("app/packages/build.py").read())

if __name__ == "__main__":
    FILE_PATH = "app/cache/project-config.json"
    name, product_name, version, description, authors, directory = StartProject.configuration()
    StartProject.create_configuration_file(name, product_name, version, description, authors, directory, FILE_PATH)
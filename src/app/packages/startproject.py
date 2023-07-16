import configparser
import subprocess

class StartProject:
    def configuration():
        _name = input("Name : ")
        _product_name = input("Product Name : ")
        _version = input("Version : ")
        _description = input("Description : ")
        _authors = input("Authors : ")
        _directory = input("Directory : ")

        return _name, _product_name, _version, _description, _authors, _directory

    def create_configuration_file(_name, _product_name, _version, _description, _authors, _directory, FILE_PATH):
        print("Configuration file creation in progress...")
        config = configparser.ConfigParser()

        config.add_section("Configuration")
        config.set("Configuration", "name", _name)
        config.set("Configuration", "product_name", _product_name)
        config.set("Configuration", "version", _version)
        config.set("Configuration", "description", _description)
        config.set("Configuration", "authors", _authors)
        config.set("Configuration", "directory", _directory)

        with open(FILE_PATH, 'w') as config_file:
            config.write(config_file)

        exec(open("app/packages/build.py").read())


if __name__ == "__main__":
    FILE_PATH = "app/cache/temps/config.config"
    _name, _product_name, _version, _description, _authors, _directory = StartProject.configuration()
    StartProject.create_configuration_file(_name, _product_name, _version, _description, _authors, _directory, FILE_PATH)
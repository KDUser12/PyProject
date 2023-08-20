import json
import sys

# Liste des commandes de base
basic_cmds = ["help", "license", "shutdown"]


# Fonction pour charger les données depuis le fichier JSON
def load_json_data():
    try:
        with open("cache/configuration.json", "r") as config_file:
            data = json.load(config_file)
        return data
    except FileNotFoundError:
        print("An error has occurred: Code Error 001")
        sys.exit(1)
    except json.JSONDecodeError:
        print("An error has occurred: Code Error 005")


# Classe pour exécuter les commandes
class CommandExecutor:
    def __init__(self):
        self.data = load_json_data()
        self.license = self.data["license"]
        self.prompt = None
        self.versions = "2.0.0-Beta"

        # Affichage des informations de base du programme
        print("PyProject - {}\n".format(self.versions))
        print("PyProject is a program to facilitate the initial creation of a project by generating the structure\n"
              "basic including folders, files and required configurations.")
        print('To learn more, enter the "help" command.')

        self.handle_command_input()

    # Méthode pour gérer les entrées de commande
    def handle_command_input(self):
        while True:
            try:
                while True:
                    self.prompt = input("\n> ")
                    self.manage_basic_commands()
            except KeyboardInterrupt:
                print("An error has occurred: Code Error 002")
                sys.exit(2)

    # Méthode pour gérer les commandes de base
    def manage_basic_commands(self):
        if self.prompt in basic_cmds:
            if self.prompt == "help":
                print("\nHere is the list of available commands: ")
                for cmd in basic_cmds:
                    print("- {}".format(cmd))
            elif self.prompt == "license":
                print(self.license)
            elif self.prompt == "shutdown":
                sys.exit(0)
            else:
                print("An error has occurred: Code Error 004")
        else:
            print("An error has occurred: Code Error 003")


# Point d'entrée du programme
if __name__ == "__main__":
    CommandExecutor()

# LISTE DES BIBLIOTHEQUES #######################
import sys
import json
import os
import pickle
import shutil
from rich.console import Console
from datetime import datetime

# LISTE DES CLASSES #############################
from app.__init__ import ProgramConsole
from app.packages.create_project import CreateProject
from app.packages.build_project import BuildProject
from app.packages.create_backup import CreateBackup

if __name__ == "__main__":
    # DESACTIVATION DE LA CREATION DE FICHIER ###
    sys.dont_write_bytecode = True

    # LANCEMENT DU PROGRAMME ####################
    exec(open('app/__init__.py').read())
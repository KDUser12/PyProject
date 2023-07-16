# LISTE DES BIBLIOTHEQUES ###################
import cmd
import json
import sys
import configparser
import subprocess
import os

# DESACTIVATION DE LA CREATION DE FICHIER ###
sys.dont_write_bytecode = True

# LISTE DES CLASSES #########################
from app.__init__ import Console
from app.packages.startproject import StartProject
from app.packages.build import BuildProject

# LISTE DES VARIABLES #######################
from app.packages.builds.setup_content import setup_content

# LANCEMENT DU PROGRAMME ####################
exec(open("app/__init__.py").read())
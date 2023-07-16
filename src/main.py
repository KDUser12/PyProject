# LISTE DES BIBLIOTHEQUES ###################
import json
import sys
import os

# DESACTIVATION DE LA CREATION DE FICHIER ###
sys.dont_write_bytecode = True

# LISTE DES CLASSES #########################
from app.__init__ import Console
from app.packages.startproject import StartProject
from app.packages.build import BuildProject

# LANCEMENT DU PROGRAMME ####################
exec(open("app/__init__.py").read())
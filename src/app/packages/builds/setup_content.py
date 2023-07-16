import configparser

config = configparser.ConfigParser()
config.read("app/cache/temps/config.config")

name = config.get("Configuration", "name")
version = config.get("Configuration", "version")
authors = config.get("Configuration", "authors")
description = config.get("Configuration", "description")

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
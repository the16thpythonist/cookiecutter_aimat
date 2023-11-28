"""
This module is used to collect common utility functions that thematically don't fit elsewhere.
"""
import os
import pathlib

# GLOBAL VARIABLES
# ================

# This is the absolute string path to the folder that contains all the code modules. Use this whenever 
# you need to access files from within the project folder.
PATH: str = pathlib.Path(__file__).parent.absolute()

# Based on the package path we can now define the more specific sub paths
VERSION_PATH: str = os.path.join(PATH, 'VERSION')


# MISC FUNCTIONS
# ==============

def get_version(path: str = os.path.join(PATH, 'VERSION')) -> str:
    """
    This function returns the string representation of the package version.
    """
    with open(path, mode='r') as file:
        content = file.read()
        version = content.replace(' ', '').replace('\n', '')
        
    return version

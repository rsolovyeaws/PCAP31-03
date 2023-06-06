from helpers.strings import extract_lower
from helpers import *
from helpers import variables
import helpers 

name = "Robert Solovev"
print(f"Uppercase letters: f{extract_upper(name)}")
print(f"Lowercase letters: f{extract_lower(name)}")

import sys 
print(f"Directories in sys.path: \n{[d for d in sys.path]}")
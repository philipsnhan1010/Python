# Ways to import a built-in modules
# 1
# import math
# print(math.sqrt(2))

# 2 : faster than 1
# from math import sqrt
# print(sqrt(2))

# 3: Also fast with alias
# from math import sqrt as square_root
# print(square_root(2))
##-----------------------------------------------------------------------------------
# Some popular built-in modules
import cmath        # Maths for complex numbers
import csv          # Read to and Write from Excel files
import datetime     # Work with dates and times
print(datetime.datetime.today())

import email        # Sending email messages
import enum         # Allow to use coding enumerations 
import fractions    # Work with Rational numbers
import gzip         # Compress and decompress files
import json         # Work with JSON files
import math         # Use mathematical functions
import os           # Get information of Operating system
print(os.name)

import random       # Work with random numbers
import re           # Work with regular expressions
import statistics   # Statistic functions
import sys          # Get at system-specific information
print(sys.version)

import time         # Work with times
import tkinter      # Create a graphics interface system
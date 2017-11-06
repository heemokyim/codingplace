# 1. import b_documenting
# 2. b_documenting.__doc__
# 3. below comment will be displayed
"""
This script creates empty file1234
"""

import doctest

filename='sample1.txt'

def create_file():
    # b_documenting.create_file.__doc__
    # below comment will be displayed
    """
    create empty file
    """
    with open(filename,'w') as file:
        file.write('') # emptry file string


# How to reflect modification and reload?
# import imp
# imp.reload(b_documenting)
#           no quotes !

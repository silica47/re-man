import os
import argparse

# function to take command line arguments
def arguments():
    parser = argparse.ArgumentParser()
    # arguments
    parser.add_argument('-f', dest="file", help="file name")
    parser.add_argument('-i', dest="input",help="optional argument with file")

    # parse the arguments in args variable 
    args = parser.parse_args()

    return args

# all the arguments comes in options variable
options = arguments()
file = options.file
optional_input = options.input

print(file)
print(optional_input)
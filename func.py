import os
import argparse

# function to take command line arguments
def arguments():
    parser = argparse.ArgumentParser()
    # arguments
    parser.add_argument('-f', dest="file", type=str, help="file name")
    parser.add_argument('-i', dest="input", help="optional argument with file")

    # parse the arguments in args variable 
    args = parser.parse_args()

    #checks if user has specified the file or not
    if not args.file:
        print("[+] Please specify a file name")
    return args

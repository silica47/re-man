import os
import argparse
import subprocess
import shutil

# function to take command line arguments
def arguments():
    parser = argparse.ArgumentParser()
    # arguments
    parser.add_argument('-f', dest="binary", type=str, help="name of the binary")
    parser.add_argument('-i', dest="input", help="optional arguments with the binary")

    # parse the arguments in args variable 
    args = parser.parse_args()

    #checks if user has specified the file or not
    if not args.binary:
        print("[+] Please specify a file name")
    return args

#make the folder for storing data
def makedir(binary):
    os.chdir("./output")
    os.mkdir(f'./{binary}')
    os.chdir("../")


def cat(binary):
    # write to the file
    with open("cat", "w") as f:
        subprocess.run(['cat', binary], stdout=f, text=True)
    
    # moving the file in output directory
    src_path = "cat"
    dst_path = f'./output/{binary}'
    shutil.move(src_path, dst_path)
   

# a = subprocess.run(['cat', 're-man.py'], capture_output=True, text=True)
# print(a.stdout)

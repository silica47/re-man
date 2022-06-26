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
   
def strings(binary):
    with open("strings", "w") as f:
        subprocess.run(['strings', binary], stdout=f, text=True)

    src_path = "strings"
    dst_path = f'./output/{binary}'
    shutil.move(src_path, dst_path)

def files(binary):
    with open("file", "w") as f:
        subprocess.run(['file', binary], stdout=f, text=True)

    src_path = "file"
    dst_path = f'./output/{binary}'
    shutil.move(src_path, dst_path)

def ldd(binary):
    with open("ldd", "w") as f:
        subprocess.run(['ldd', binary], stdout=f, text=True)

    src_path = "ldd"
    dst_path = f'./output/{binary}'
    shutil.move(src_path, dst_path)

def nm(binary):
    with open("nm", "w") as f:
        subprocess.run(['nm', binary], stdout=f, text=True)

    src_path = "nm"
    dst_path = f'./output/{binary}'
    shutil.move(src_path, dst_path)

def readelf(binary):
    with open("readelf", "w") as f:
        subprocess.run(['readelf', '-h', binary], stdout=f, text=True)

    src_path = "readelf"
    dst_path = f'./output/{binary}'
    shutil.move(src_path, dst_path)

def ltrace(binary, options):

    if not options:
        with open("ltrace", "w") as f:
            subprocess.run(['ltrace', f'./{binary}'], stderr=f, stdout=subprocess.DEVNULL, text=True)
    else:
        with open("ltrace", "w") as f:
            subprocess.run(['ltrace', f'./{binary}', options], stderr=f, stdout=subprocess.DEVNULL, text=True)

    src_path = "ltrace"
    dst_path = f'./output/{binary}'
    shutil.move(src_path, dst_path)

def strace(binary, options):

    if not options:
        with open("strace", "w") as f:
            subprocess.run(['strace', f'./{binary}'], stdout=subprocess.DEVNULL, stderr=f)

    else:
        with open("strace", "w") as f:
            subprocess.run(['strace', f'./{binary}', options], stdout=subprocess.DEVNULL, stderr=f)

    src_path = "strace"
    dst_path = f'./output/{binary}'
    shutil.move(src_path, dst_path)

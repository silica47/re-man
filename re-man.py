import func
# import pyfiglet

def main():
    # all the arguments comes in options variable
    options = func.arguments()
    binary = options.binary
    optional_input = options.input

    # making directory
    func.makedir(binary)

    #cat command
    func.cat(binary)
    print("Something Went Wrong")

if __name__ == "__main__":
    # print(pyfiglet.figlet_format("RE Man", font = "slant"))
    try:
        main()
    except Exception as e:
        print(f'Error: {e}')

import func

def main():
    # all the arguments comes in options variable
    options = func.arguments()
    file = options.file
    optional_input = options.input

    print(file)
    # print(optional_input)

if __name__ == "__main__":
    main()
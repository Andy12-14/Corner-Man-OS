from functions.write_file import write_file


def main():

    #print(write_file("calculator", "lorem.txt", "overwrite for lorem.txt using write_file function."))
    #print(write_file("calculator", "pkg/moredir.txt", "Created moredir.txt in pkg directory."))
    print(write_file("calculator", "../outside.txt", "This should be denied."))









main()
import sys
def cat():
    """
    concatenate files and print on the standard output
    
    USAGE :
    >>> python cat.py f1 f2 ... fn
    content of file f1
    content of file f2
    ...
    content of file fn
    """
    file_names = sys.argv[1:]
    for name in file_names:
        try:
            with open(name, 'r') as f:
                lines = f.readlines()
                for l in lines:
                    print(l, end="")
        except IOError as error:
            print("cat: {}: No such file or directory".format(name))
cat()
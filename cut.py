import sys, re
def cut():
    """
    remove sections from each line of files
    
    USAGE :
    $ cat foo.txt
    A,B,C,D,E
    a,b,c,d,e
    $ python cut.py -d , -f 3-5,3-4,1-1 foo.txt
    A,C,D,E
    a,c,d,e
    """
    arguments = sys.argv[1:]
    if len(arguments) != 5 or arguments[0] != '-d' or arguments[2] != '-f':
        raise ValueError("cut: invalid usage\nUSAGE:\n>>> python cut.py -d c -f d file")
    if len(arguments[1]) != 1:
        raise ValueError("cut: the delimiter must be a single character")
    if "0" in arguments[3]:
        raise ValueError("cut: fields are numbered from 1")
    # the regex I wrote for the real cut command : "^([1-9]+-?|-?[1-9]+|[1-9]+-[1-9]+)(,([1-9]+-?|-?[1-9]+|[1-9]+-[1-9]+))*$"
    if re.match(r'^([1-9]+-[1-9]+)(,[1-9]+-[1-9]+)*$', arguments[3]) == None:
        raise ValueError("cut: invalid field range")
    file_path = arguments[4]
    delim = arguments[1]
    fields = arguments[3]
    fields_list = fields.split(',')
    columns = []
    for field in fields_list:
        bornes = field.split('-')
        inf = int(bornes[0])
        sup = int(bornes[1])
        if sup < inf:
            raise ValueError("cut: invalid decreasing range")
        elif sup == inf:
            columns.append(sup-1)
        else :
            columns.extend(list(range(inf-1, sup)))
    columns = sorted(list(set(columns)))
    try:
        with open(file_path, 'r') as infile:
            for line in infile:
                i = 0
                tokens = line.split(delim)
                while i < len(columns) and columns[i] < len(tokens):
                    if i+1 == len(columns) or columns[i+1] == len(tokens):
                        print(tokens[columns[i]])
                    else :
                        print(tokens[columns[i]], end=delim)
                    i += 1
    except IOError as error:
            print("cut: {}: No such file or directory".format(file_path))
try:     
    cut()
except ValueError as error:
    print(error)
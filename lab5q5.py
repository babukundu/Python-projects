def make_dictionary(filename):
    text = open(filename, "r")
    dct = dict()
    for line in text:
        line = line.strip()
        if len(line)!=0:
            if line in dct:
                dct[line]=dct[line]+1
            else:
                dct[line]=1
    
    return dct
    



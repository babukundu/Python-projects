def isbn_dictionary(filename):
    import csv
    dict_from_csv = {}
    with open(filename, mode='r') as inp:
        reader = csv.reader(inp)
        for rows in reader:
            lst=[]
            lst.append(rows[:-1])
        dict_from_csv = {rows[-1]:lst for rows in reader}
    
    return dict_from_csv
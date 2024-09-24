def isbn_dictionary(filename):
    import csv
    dict_from_csv = {}
    try:
        with open(filename, mode='r') as inp:
            for rows in inp:
                lst1=rows.strip().split(',')
                lst2=(lst1[0],lst1[1])
                dict_from_csv[lst1[-1]]=lst2
        return dict_from_csv
    except FileNotFoundError:
        print("The file",filename,"was not found.")

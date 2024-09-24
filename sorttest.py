def list_sorting(lst1,lst2):
    zipped_lists = zip(lst1, lst2)
    sorted_pairs = sorted(sorted(zipped_lists),reverse=True,key=lambda x:x[1])

    tuples = zip(*sorted_pairs)
    list_name,list_age = [ list(tuple) for tuple in  tuples]
    return list_name,list_age

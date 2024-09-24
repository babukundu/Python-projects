def get_name(name_dict, id_num):
    key_list = list(name_dict.keys())
    val_list = list(name_dict.values())

    if (id_num in name_dict.keys()):
        position = key_list.index(id_num)
        return val_list[position]
     
    else:
        return "None"

def word_counter(input_str):
    counts = dict()
    words = input_str.split()

    for word in words:
        w=word.lower()
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1

    res_dict = dict((k.lower(), v) for k, v in counts.items())

    return res_dict

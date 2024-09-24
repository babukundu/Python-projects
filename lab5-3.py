def find_key(input_dict, value):
    key_list = list(input_dict.keys())
    val_list = list(input_dict.values())

    if (value in input_dict.values()):
        position = val_list.index(value)
        return key_list[position]
     
    else:
        return None
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
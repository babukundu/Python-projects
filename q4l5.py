def make_index(words_on_page):
    counts = dict()
    for key, values in words_on_page.items():
        for v in values:
            if v in counts:
                counts[v] += [key]
            else:
                counts[v] = [key]
    return counts
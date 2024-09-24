def is_a_number(string):

    x=string.isdigit()
    return x
def replace_character(sentence):
    str=sentence.replace('s','$')
    str1=str.replace('S','$')
    return str1
def word_swapper(sentence, word):
    str=sentence.replace(word,"ABC")
    return str
def top_and_tail(string):
    res_str = string[1:-1]
    return res_str
def half_string(string):
    x=len(string)
    y=int(x/2)
    res_str = string[0:y]
    return res_str
def second_half_string(string):
    x=len(string)
    y=int(x/2)
    res_str = string[y:]
    return res_str
def first_nth_string(string, n):
    res_str = string[0:int(n)]
    return res_str
def full_name(first_name, last_name):
    str=first_name+" "+last_name
    return str
def count_item(data, item):
    x=data.count(item)
    return x
def append_item(data,item):
    data.append(item)
    
    return data
def second(data):
    item = data[1]
    return item
def insert_item_end(data, item):
    data.insert(len(data),item)
    return data
def append_list_new(data1, data2):
    new_list = data1+data2
    return new_list
def append_lists(data1, data2):
    return data1+data2
def last(data):
    item=data[-1]
    return item
def remove(data):
    lst=data[:2]+data[3:]
    return lst
def nth_member(data, n):
    item = data[n]
    return item
def duplicate_last(data):
    new_list = data.copy()
    item=data[-1]
    new_list.append(item)
    return new_list
def cubed_tuple(number):
    tup = (number,number**3)
    return tup
def list_swap(lst):
    n=len(lst)
    if n % 2 == 0:
        m=n
    else:
        m=n-1
    for i in range(0, m, 2):
        temp=lst[i]
        lst[i]=lst[i+1]
        lst[i+1]=temp
        
    return lst
def num_words(string):
    words=string.split()
    return len(words)
def list_sorting(lst1,lst2):
    zipped_lists = zip(lst1, lst2)
    sorted_pairs = sorted(sorted(zipped_lists),reverse=True,key=lambda x:x[1])

    tuples = zip(*sorted_pairs)
    list_name,list_age = [ list(tuple) for tuple in  tuples]
    return list_name,list_age
from introsort_multithreaded import sorting

def sort(lst): 
    if type(lst[0]) is int: 
        return sorting.sort_int(lst)
    elif type(lst[0]) is float: 
        return sorting.sort_fraction(lst)
    elif type(lst[0]) is str: 
        return sorting.sort_str(lst) 
    else: 
        print("Unknown type")
        return 
        

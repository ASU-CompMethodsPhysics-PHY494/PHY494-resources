def mean(num_list):
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError:
        return 0
    except TypeError:
        raise TypeError("Cannot get mean for non-number elements")

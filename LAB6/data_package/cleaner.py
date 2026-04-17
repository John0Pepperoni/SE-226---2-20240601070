def remove_duplicates(data_list):
    unique_set = set(data_list)
    return list(unique_set)

def strip_whitespaces(string_list):
    return [s.strip() for s in string_list]

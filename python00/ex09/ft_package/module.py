def count_in_list(lst, item) -> int:
    count = len([x for x in lst if x == item])
    return count

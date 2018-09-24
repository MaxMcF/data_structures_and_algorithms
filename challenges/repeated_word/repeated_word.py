from ..data_structures.hash_table import hash_table


def repeated_word(string):
    dup_bool = True
    while dup_bool:
        word = string.split(' ', 1)
        success = hash_table.insert(word[0])
        if success is False:
            return word[0]
        string = word[1]
    return 'No Duplicate'


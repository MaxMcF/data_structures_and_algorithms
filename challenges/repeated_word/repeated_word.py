from hash_table import HashTable

def repeated_word(string):
    """This function will detect the first repeated word in a string.
    Currently, there is no handling for punctuation, meaning that if the word
    is capitalized, or at the end of a senctence, it will be stored as a different word.

    ARGS:
        A string of words
    RETURN:
        The first duplicated word in the input string.
    """
    ht = HashTable()
    dup_bool = True
    while dup_bool:
        word = string.split(' ', 1)
        try:
            success = ht.set(word[0], None)
        except:
            return word[0]
        if success is False:
            return word[0]
        try:
            string = word[1]
        except:
            return 'No Duplicate'



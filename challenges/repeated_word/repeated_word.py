from hash_table import HashTable

def repeated_word(string):
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



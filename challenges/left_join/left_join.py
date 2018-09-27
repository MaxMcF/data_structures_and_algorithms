from hash_table import HashTable

def left_join(table_one, table_two):
    return_list = []
    for i in table_one.hashtable:
        if i:
            while i.head:
                try:
                    val_two = table_two.get(i.head.key)
                except:
                    val_two = None
                return_list.append([i.head.key, i.head.val, val_two])
                i.head = i.head.next
    return return_list


# ht2 = HashTable()
# ht2.set('Max', 'Max Gunnar McFarland')
# # ht2.set('Mike', 'Michael Jordan')
# # ht2.set('John', 'John Hamm')


# ht1 = HashTable()
# ht1.set('Sonya', 'Sonya Sotomayor')
# # ht1.set('Mike', 'Michael Jackson')
# # ht1.set('John', 'John Wayne')


# result = left_join(ht1, ht2)
# import pdb; pdb.set_trace()

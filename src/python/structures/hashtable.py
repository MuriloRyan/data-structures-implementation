from hashtable.separate_chaining import SeparateChainingHashTable
from hashtable.open_adressing import OpenAdressingHashTable

hashtable_class = {
    "scht": SeparateChainingHashTable,
    "oaht": LinearProbingSeparateChainingHashTable
}

def hashtable(str: protocol,int: length, dict: hashtable_class=hashtable_class):
    protocol = protocol.lower()

    try:
        hashtable = hashtable_class[protocol]
        return hashtable
    except:

        return None

ht = hashtable('scht', 16)
print(ht)
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * self.capacity
        self.length = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return float('{:.2f}'.format(self.length / self.capacity))

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hashKey = 5381

        for char in key:
            hashKey = (hashKey * 33) + ord(char)
        return hashKey & 0xfffffff




    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        if self.storage[self.hash_index(key)] == None:
            self.storage[self.hash_index(key)] = HashTableEntry(key, value)
            self.length +=1
        else:
            # oldHead = self.storage[self.hash_index(key)]
            # newHead = HashTableEntry(key, value)
            # self.storage[self.hash_index(key)] = newHead
            # newHead.next = oldHead
            # self.length +=1
            cur = self.storage[self.hash_index(key)]

            while cur != None:
                if cur.key == key:
                    cur.value = value
                    break
                elif cur.next == None:
                    cur.next = HashTableEntry(key, value)
                    break
                cur = cur.next

        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity*2)


            
        

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        cur = self.storage[self.hash_index(key)]
        prev = None
        while cur != None:
            if cur.key == key:
                if cur.next == None and prev == None:
                    self.storage[self.hash_index(key)] = None
                    self.length -=1
                    return
                elif cur.next == None and prev != None:
                     prev.next = None
                     return
                elif prev == None and cur.next != None:
                    self.storage[self.hash_index(key)] = cur.next
                    cur = None
                    return
                else:
                    prev.next = cur.next
                    cur = None
                    return
            prev = cur
            cur = cur.next

        if self.get_load_factor() <= 0.2:
            new_capacity = self.capacity //2
            if new_capacity < 8:
                new_capacity = 8
            self.resize(new_capacity)



    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        cur = self.storage[self.hash_index(key)]

        while cur != None:
            if cur.key == key:
               return cur.value
            cur = cur.next


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        old_capacity = self.capacity
        self.capacity = new_capacity
        oldStorage = self.storage
        self.storage = [None] * self.capacity

        for i in range(old_capacity):
            cur = oldStorage[i]

            while cur != None:
                self.storage[self.hash_index(cur.key)] = HashTableEntry(cur.key, cur.value)
                cur = cur.next
        



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

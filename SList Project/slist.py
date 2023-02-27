class SList:
    class SListNode:
        def __init__ (self, value = None):
            self.value = value
            self.next = None

    def __init__ (self):
        self._head = None
        self._size = 0

    '''Insert a new value in the list. Maintain nondecreasing ordering of elements'''
    def insert(self, value):
        new_node = SList.SListNode(value)
        check = self._head
        prev = None
        if self._size == 0:
            self._head = new_node
            self._size += 1
        else:
            while check is not None and check.value <= value:
                prev = check
                check = check.next
            new_node.next = check
            if prev is not None:
                prev.next = new_node
            else:
                self._head = new_node
            self._size += 1
        
    '''Search for a value in the list, return it if found, None otherwise'''
    def find(self, value):
        current = self._head
        while current is not None:
            if current.value == value:
                return value
            current = current.next
        return None

    '''Remove the first occurance of value.'''
    def remove(self, value):
        check = self._head
        prev = None
        while check is not None and check.value is not value:
            prev = check
            check = check.next
        if check is None:
            return
        else:
            prev.next = check.next
            check.next = None

    '''Remove all instances of value'''
    def remove_all(self, value):
        check = self._head
        prev = None
        #runs through the list until it hits the end, or hits the desired value
        while check is not None and check.value is not value:
            prev = check
            check = check.next
        #if it hits the desired value, run through it until it hits the next value
        if check.next is None:
            prev.next = None
            return
        if check.value is value:
            while check.next.value is value:
                check = check.next
        if check is None:
            return
        else:
            prev.next = check.next
            check.next = None



    '''Convert the list to a string and return it'''
    def __str__(self):
        values = []
        check = self._head
        while check is not None:
            values.append(str(check.value))
            check = check.next
        return ' -> '.join(values)

    '''Return an iterator for the list'''
    def __iter__(self):
        self._current = self._head
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            result = self._current.value
            self._current = self._current.next
            return result

    '''Return the item at the given index, or throw an exception if invalid index'''
    def __getitem__(self, index):
        check = self._head
        for x in range(index):
            check = check.next
        return check.value

    def __len__(self):
        check = self._head
        len_counter = 0
        while check is not None:
            check = check.next
            len_counter += 1
        return len_counter


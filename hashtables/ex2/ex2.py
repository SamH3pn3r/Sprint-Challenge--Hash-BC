#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length)

    """
    YOUR CODE HERE
    """

    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        # print(tickets[i].source, tickets[i].destination)
    # Start with None
    # Look at start value
    # Use to retrieve next stop
    # Continue until value is None
    current_val = hash_table_retrieve(hashtable, "NONE")
    print(current_val)
    route[0] = current_val
    for i in range(1, length):
        next_val = hash_table_retrieve(hashtable, current_val)
        print(next_val)
        route[i] = next_val
        current_val = next_val
    print(route)
    return route
  
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
    route = [None] * length

    # Insert a source key and destination in the hashtable
    for i in tickets:
        hash_table_insert(hashtable, i.source, i.destination)

    # find the first ticket with source as None. will become next destination
    destination = hash_table_retrieve(hashtable, "NONE")

    for i in range(length):
        # build the route
        route[i] = destination
        # next destination
        destination = hash_table_retrieve(hashtable, destination)
    return route

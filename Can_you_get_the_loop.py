"""
You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

Your objective is to determine the length of the loop.

For example in the following picture the tail's size is 3 and the loop size is 11.
# Use the `next' attribute to get the following node

node.next
Note: do NOT mutate the nodes!
"""

def loop_size(node):
    dict_node = {}
    count = 0
    if node == node.next: return 1
    while(node.next not in dict_node):
        dict_node[node] = count
        count += 1
        node = node.next
    return count+1-dict_node[node.next]

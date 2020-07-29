#Find all list items
# wrtie a python function to index all items in a list

#Input list to search, value to search for
#output: list of indices
# example:
"""
example = [[[1,2,3],2,[1,3]],[1,2,3]]
find 2
[[0,0,1],[0,1],[1,1]]
"""

def index_all(search_list, item):
    indices = []
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):#if it's a type of list, search the sub-list
            for index in index_all(search_list[i], item):
                indices.append([i]+index)
    return indices

print(index_all([[[1,2,3],2,[1,3]],[1,2,3]], 2))
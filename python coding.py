#Write a python programe to merge two shorted lists into a single sorted list.

def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0
    
    # Traverse both lists and append smaller element from the lists
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    # Append remaining elements from list1, if any
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    # Append remaining elements from list2, if any
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
    return merged_list

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

merged_list = merge_sorted_lists(list1, list2)
print(merged_list)

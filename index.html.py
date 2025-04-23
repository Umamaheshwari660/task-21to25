
# task: Given a string, return a dictionary where keys are characters and values are their occurrence.
# Given two dictionaries, merge them into one. If a key exists in both, sum their values 

# Part 1: Count character occurrences in a string

def count_characters(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

#  Part 2: Merge two dictionaries, summing values for common keys

def merge_dicts(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged

#  Example Usage:

s1 = "banana"
s2 = "bandana"

d1 = count_characters(s1)  
d2 = count_characters(s2)   

merged_result = merge_dicts(d1, d2)

print("Count 1:", d1)
print("Count 2:", d2)
print("Merged:", merged_result)

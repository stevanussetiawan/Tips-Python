dict1 = {'apple': 1, 'banana': 2}
dict2 = {'banana': 3, 'orange': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)

# Or in Python 3.9+
merged_dict = dict1 | dict2

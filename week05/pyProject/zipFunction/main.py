keys = ["a","b","c"]
values = [1,2,3]
dictionary = {k:v for k,v in zip(keys,values)}

print(dictionary)
# {'a': 1, 'b': 2, 'c': 3}

keys.append("d")
values.append(4);
dictionary = {k:v for k,v in zip(keys,values)}
print(dictionary)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
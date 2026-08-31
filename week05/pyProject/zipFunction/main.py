
# Week 5 - Activity 1: Zip function - Dictionary data type - Tips and tricks
def tips_and_tricks():
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


# Week 5 - Activity 2: Merging Dictionaries with Conditions
def mergeDics():
    Key1 = ["a", "b", "c", "d", "f", "g", "h", "e", "a"]
    Value1= [20, 3, 1, 88, 55, 92, 6, 90, 910]
    Key2=["u", "b", 'o', 'x',  "e", 'a']
    Value2=[200, 30, 10, 88, 55, 920]

    # Transforming Lists into a Dictionary
    dic1 = {k:v for k,v in zip(Key1,Value1)}
    dic2 = {k:v for k,v in zip(Key2,Value2)}

    # Merging Dictionaries with the Double Asterisk (**)
    merged_dict = {**dic1, **dic2}
    print(merged_dict);

if __name__ == "__main__":
    # tips_and_tricks()
    mergeDics();




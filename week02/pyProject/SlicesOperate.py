my_list = [1, 3, 5, 7, 9, 11]
print(my_list); # [1, 3, 5, 7, 9, 11]
# splice (拼接) an new list into mu_list, not include the index 4 (my_list[4])
my_list[2:4] = [-3, -9, -11, -13] 
#list  [1, 3, -3, -9, -11, -13, 9, 11]
#index  0  1                    4   5   # origin index
print(my_list);  #
# Insert 6 values at index 3 (middle of the list)
my_list[4:6] = ["a", "b", "c", "d", "e", "f"]
print(my_list);
# [1, 3, -3, -9, 'a', 'b', 'c', 'd', 'e', 'f', 9, 11]
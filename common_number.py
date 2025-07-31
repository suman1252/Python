# Python program to find the common elements 
# in two lists
def common_member(list1,list2):
    list1_set = set(list1)
    list2_set = set(list2)
 
    if (list1_set & list2_set):
        print(list1_set & list2_set)
    else:
        print("No common elements") 
          
  
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [5, 7, 9, 11, 13, 15, 17, 19, 21, 23]
common_member(list1,list2)
  

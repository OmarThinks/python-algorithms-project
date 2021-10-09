"""
Let's talk about lists
"""


my_list = [7,6,9,5,3,8,4,2,1]


my_list.sort(reverse=True)

assert(my_list == [9, 8, 7, 6, 5, 4, 3, 2, 1])


my_list.sort()

assert(my_list == [1, 2, 3, 4, 5, 6, 7, 8, 9])








my_list.pop()
assert(my_list == [1, 2, 3, 4, 5, 6, 7, 8])



my_list.pop(0)
assert(my_list == [2, 3, 4, 5, 6, 7, 8])


my_list.insert(0,1)





assert(my_list[0:2]==[1,2])


my_list.append(9)



assert(my_list==[1, 2, 3, 4, 5, 6, 7, 8, 9])




assert(my_list.count(1)==1)
assert(my_list.count(300)==0)
assert(my_list.index(3)==2)
# print(my_list.index(700)) # Raises error




print(my_list)



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



my_list.extend([10,11,12])

assert(my_list == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


my_list_copy= my_list.copy()

my_list_copy[0]=5


assert(my_list[0] 		== 1)
assert(my_list_copy[0] 	== 5)



my_list_equals = my_list


my_list_equals[0]=700



assert(my_list[0] 		== 700)
assert(my_list_equals[0] 	== 700)






assert([x**2 for x in range(3)]==[0,1,4])


print("hi".split(" "))
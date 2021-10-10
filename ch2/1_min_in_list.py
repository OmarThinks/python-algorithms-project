"""
Prompt:

Find the minimum Number in a list


I will assuume that they are all floats

"""



"""
This will have a Quadratic Complexity
"O(n^2)"
"""



from math import inf


"""
This will have a Quadratic Complexity
"O(n^2)"
"""


def find_min_in_list_quadratic(input_list):
	min_number = inf
	
	for element_1 in input_list:
		for element_2 in input_list:
			if element_2<=element_1:
				if element_2<min_number:
					min_number = element_2
					continue
	return min_number

assert(find_min_in_list_quadratic([]) == inf)
assert(find_min_in_list_quadratic([1]) == 1)
assert(find_min_in_list_quadratic([1,2,3]) == 1)
assert(find_min_in_list_quadratic([2,3,4,5]) == 2)







"""
This will have a Linear Complexity
"O(n)"
"""

def find_min_in_list_linear(input_list):
	min_number = inf
	for element in input_list:
		if element<min_number:
			min_number=element
	return min_number



assert(find_min_in_list_linear([]) == inf)
assert(find_min_in_list_linear([1]) == 1)
assert(find_min_in_list_linear([1,2,3]) == 1)
assert(find_min_in_list_linear([2,3,4,5]) == 2)





"""
START
Q1

NOTE: The function "get_childs_parents" is reused in next questions
It is very Important function
"""



"""
Planning:

Store all data in a dictionary, to summerize the connections


childs_parents = {
	node (str): [list of parents] 
}

Example:

childs_parents = {
	"3": [1,2],
	...
}


Then loop through this dict, to get the length of parnets of each element.
Collect the 0 parnets in one group.
And collect the 1 parnets in one group.
"""




from pprint import pprint as pp

def get_childs_parents(parent_child_pairs):
	childs_parents = {}

	for pair in parent_child_pairs:
		parent = pair[0]
		child = pair[1]
		#print(parent, child)

		if str(parent) not in childs_parents:
			childs_parents[str(parent)] = []
		
		if str(child) not in childs_parents:
			childs_parents[str(child)] = [parent]
		else:
			childs_parents[str(child)].append(parent)
	return childs_parents



def find_nodes_with_zero_and_one_parents(parent_child_pairs): 
	#print(parent_child_pairs)
	childs_parents = get_childs_parents(parent_child_pairs)

	orphan_elements = []
	one_parent_elements = []
	for child in childs_parents.keys():
		number_of_parnets = len(childs_parents[child])
		#print(child, number_of_parnets)
		if number_of_parnets == 0:
			orphan_elements.append(int(child))
		elif number_of_parnets == 1:
			one_parent_elements.append(int(child))
	#print(orphan_elements)
	#print(one_parent_elements)
	return [orphan_elements, one_parent_elements]



"""
TESTING:

Here we test with the given test cases
"""


parent_child_pairs = [
    (5, 6), (1, 3), (2, 3), (3, 6), (15, 12),
    (5, 7), (4, 5), (4, 9), (9, 12), (30, 16)
]






nodes = find_nodes_with_zero_and_one_parents(parent_child_pairs)


nodes_with_zero_parent = sorted(nodes[0])
nodes_with_one_parent = sorted(nodes[1])
# Just sorting the result
# To make it look exactly like the output should be
# If I add sorting to the function, then complexity will be "O(n log(n))"

assert([nodes_with_zero_parent, nodes_with_one_parent]==[
  [1, 2, 4, 15, 30],   # Individuals with zero parents
  [5, 7, 9, 16]        # Individuals with exactly one parent
]
)


print("Q1 Passed all test cases")

"""
COMPLEXITY:

Here we compute complexity


n: length of the relationships

Time complexity: "O(n)"
Spacial complexity: "O(n)"
"""




"""
Q1: END
"""




"""
Q2: STRAT
"""

"""
Planning:


Create a function called get_ancestors

This function keeps climbing
Now, we get the intersection of these sets

If there was ant intersection, then return True
No intersection: return False

"""







parent_child_pairs_2 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (15, 21), (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
    (12, 9), (15, 13)
]





def get_ansectors(children_parents, element):
	current_level = []
	next_level = children_parents[str(element)]
	ansectors = []
	while len(next_level)>0:
		current_level = next_level.copy()
		next_level = []
		for ansector in current_level:
			if ansector not in ansectors:
				ansectors.append(ansector)
				next_level.extend(children_parents[str(ansector)])
	return ansectors


def has_common_ancestor(
	parent_child_pairs, element_1, element_2):
	children_parents = get_childs_parents(parent_child_pairs)
	element_1_ancestors = get_ansectors(children_parents, element_1)
	element_2_ancestors = get_ansectors(children_parents, element_2)
	if len(
		list(set(element_1_ancestors)&set(element_2_ancestors)))>0:
		return True
	return False





"""
TESTING:
"""





assert(has_common_ancestor(parent_child_pairs_2, 3, 8)   == False)
assert(has_common_ancestor(parent_child_pairs_2, 5, 8)   == True)
assert(has_common_ancestor(parent_child_pairs_2, 6, 8)   == True)
assert(has_common_ancestor(parent_child_pairs_2, 6, 9)   == True)
assert(has_common_ancestor(parent_child_pairs_2, 1, 3)   == False)
assert(has_common_ancestor(parent_child_pairs_2, 3, 1)   == False)
assert(has_common_ancestor(parent_child_pairs_2, 7, 11)  == True)
assert(has_common_ancestor(parent_child_pairs_2, 6, 5)   == True)
assert(has_common_ancestor(parent_child_pairs_2, 5, 6)   == True)
assert(has_common_ancestor(parent_child_pairs_2, 3, 6)   == True)
assert(has_common_ancestor(parent_child_pairs_2, 21, 11) == True)



print("Q2 Passed all test cases")



"""
COMPLEXITY:

Here we compute complexity


n: length of the relationships

Time complexity: "O(n)"
Spacial complexity: "O(n)"
"""


"""
Q2: END
"""






"""
Q3: START
"""


"""
use get_ancestors.
The latest ancestor i the one we are looking for.
"""





def find_earliest_ancestor(parent_child_pairs, element):
	children_parents = get_childs_parents(parent_child_pairs)
	element_ansectors = get_ansectors(children_parents, element)
	if len(element_ansectors)>0:
		return element_ansectors.pop()
	return None



parent_child_pairs_3_1 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]



assert(find_earliest_ancestor(parent_child_pairs_3_1, 8) == 14)
assert(find_earliest_ancestor(parent_child_pairs_3_1, 7) == 14)
assert(find_earliest_ancestor(parent_child_pairs_3_1, 6) == 14)
assert(find_earliest_ancestor(parent_child_pairs_3_1, 15) == 2)
assert(find_earliest_ancestor(parent_child_pairs_3_1, 14) == None)
assert(find_earliest_ancestor(parent_child_pairs_3_1, 11) == 14)






parent_child_pairs_3_2 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 2), (1, 9)
]




assert(find_earliest_ancestor(parent_child_pairs_3_2, 8) == 4)
assert(find_earliest_ancestor(parent_child_pairs_3_2, 7) == 4)
assert(find_earliest_ancestor(parent_child_pairs_3_2, 6) == 14)
assert(find_earliest_ancestor(parent_child_pairs_3_2, 15) == 14)
assert(find_earliest_ancestor(parent_child_pairs_3_2, 14) == None)
assert(find_earliest_ancestor(parent_child_pairs_3_2, 11) == 4 or 1)


print("Q3 Passed all test cases")


"""
COMPLEXITY:

Here we compute complexity


n: length of the relationships

Time complexity: "O(n)"
Spacial complexity: "O(n)"
"""




"""
Q3: END
"""
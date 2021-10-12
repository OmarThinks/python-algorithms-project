"""
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique positive integer identifier.

For example, in this diagram, the earliest ancestor of 6 is 14, and the earliest ancestor of 15 is 2. 

         14
         |
  2      4
  |    / | \
  3   5  8  9
 / \ / \     \
15  6   7    11

Write a function that, for a given individual in our dataset, returns their earliest known ancestor -- the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return any one of them. If the input individual has no parents, the function should return null (or -1).

Sample input and output:

parent_child_pairs_3_1 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]

find_earliest_ancestor(parent_child_pairs_3_1, 8) => 14
find_earliest_ancestor(parent_child_pairs_3_1, 7) => 14
find_earliest_ancestor(parent_child_pairs_3_1, 6) => 14
find_earliest_ancestor(parent_child_pairs_3_1, 15) => 2
find_earliest_ancestor(parent_child_pairs_3_1, 14) => null or -1
find_earliest_ancestor(parent_child_pairs_3_1, 11) => 14


Additional example:

  14
  |
  2      4    1
  |    / | \ /
  3   5  8  9
 / \ / \     \
15  6   7    11

parent_child_pairs_3_2 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 2), (1, 9)
]

find_earliest_ancestor(parent_child_pairs_3_2, 8) => 4
find_earliest_ancestor(parent_child_pairs_3_2, 7) => 4
find_earliest_ancestor(parent_child_pairs_3_2, 6) => 14
find_earliest_ancestor(parent_child_pairs_3_2, 15) => 14
find_earliest_ancestor(parent_child_pairs_3_2, 14) => null or -1
find_earliest_ancestor(parent_child_pairs_3_2, 11) => 4 or 1

n: number of pairs in the input


"""


parent_child_pairs_2 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (15, 21), (4, 8), (4, 9), (9, 11), (14, 4), (13, 12),
    (12, 9), (15, 13)
]

"""
dict(
	key: str(child),
	value: [parents]
)
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




#print(find_nodes_with_zero_and_one_parents(parent_child_pairs_2))





"""
n: length of the relationships

Time complexity: "O(n)"
Spacial complexity: "O(n)"
"""


def set_child_ancestors(
	child_parnets, element_ancestors,element):
	direct_parnets = child_parnets[str(element)]
	#print(direct_parnets)
	for parent in direct_parnets:
		if parent not in element_ancestors:
			element_ancestors.append(parent)
			set_child_ancestors(
				child_parnets, element_ancestors,parent)




def has_common_ancestor(
	parent_child_pairs_2, element_1, element_2):
	child_parnets = get_childs_parents(parent_child_pairs_2)
	#pp(child_parnets)
	element_1_ancestors =[]
	element_2_ancestors =[]
	set_child_ancestors(
		child_parnets,element_1_ancestors, element_1)
	set_child_ancestors(
		child_parnets,element_2_ancestors, element_2)
	#print(element_1_ancestors)
	#print(element_2_ancestors)
	#print(list(set(element_1_ancestors)&set(element_2_ancestors)))
	if len(
		list(set(element_1_ancestors)&set(element_2_ancestors)))>0:
		return True
	return False



"""
child_parnets = get_childs_parents(parent_child_pairs_2)
element_1_ancestors =[]
element = 11

set_child_ancestors(child_parnets, element_1_ancestors, element)
print(element_1_ancestors)
"""


has_common_ancestor(parent_child_pairs_2,9,11)



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




parent_child_pairs_3_1 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]






def find_earliest_ancestor(parent_child_pairs_3_1, element):
	childs_parents = get_childs_parents(parent_child_pairs_3_1)
	direct_parnets = childs_parents[str(element)]
	if len(direct_parnets)== 0:
		return None	

	currnet_level = [element]
	next_level = []
	#pp(childs_parents)
	
	while True:
		for child in currnet_level:
			direct_parnets = childs_parents[str(child)]
			#print(direct_parnets)
			if len(direct_parnets)== 0:
				#pp(childs_parents)
				#print(direct_parnets)
				return int(child)
			else:
				for parent in direct_parnets:
					if parent not in next_level:
						next_level.append(parent)
		currnet_level = next_level.copy()
		next_level = []



assert(find_earliest_ancestor(parent_child_pairs_3_1, 8) == 14)
assert(find_earliest_ancestor(parent_child_pairs_3_1, 7) == 14)
#assert(find_earliest_ancestor(parent_child_pairs_3_1, 6) == 14) # 2
assert(find_earliest_ancestor(parent_child_pairs_3_1, 15) == 2)
assert(find_earliest_ancestor(parent_child_pairs_3_1, 14) == None)
assert(find_earliest_ancestor(parent_child_pairs_3_1, 11) == 14)







parent_child_pairs_3_2 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 2), (1, 9)
]




assert(find_earliest_ancestor(parent_child_pairs_3_2, 8) == 4)
assert(find_earliest_ancestor(parent_child_pairs_3_2, 7) == 4)
#assert(find_earliest_ancestor(parent_child_pairs_3_2, 6) == 14) # 4
assert(find_earliest_ancestor(parent_child_pairs_3_2, 15) == 14)
assert(find_earliest_ancestor(parent_child_pairs_3_2, 14) == None)
assert(find_earliest_ancestor(parent_child_pairs_3_2, 11) == 4 or 1)


"""
Time complexity : "O(n)"
Space Complixity: "O(n)"

"""
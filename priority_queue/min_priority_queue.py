from pprint import pprint as pp
from random import randint

import unittest
from math import log
import json

assertEqual = unittest.TestCase().assertEqual


class MinPriorityQueue():
	"""docstring for MinPriorityQueue"""
	priority_queue = []
	length = 0
	
	def __init__(self, priority_queue:list):
		self.priority_queue = sorted(priority_queue)
		self.length = len(self.priority_queue)
	
	def get_parent_index(self, node_index, do_assertions = True):
		if node_index == 0 or None: return None
		
		if node_index == None:
			return None

		parent_index = int((node_index+1)/2)-1

		if do_assertions:
			#print(parent_index, node_index)
			#print(self.get_children_indices(parent_index, do_assertions=False))
			assertEqual(True, node_index in 
				self.get_children_indices(parent_index, do_assertions=False))
		return int((node_index+1)/2)-1

	def get_children_indices(self, node_index, do_assertions= True):
		left_child_index = node_index*2+1
		right_child_index = node_index*2+2

		if do_assertions:
			assertEqual(node_index, 
				self.get_parent_index(left_child_index, do_assertions=False))
			assertEqual(node_index, 
				self.get_parent_index(right_child_index, do_assertions=False))
		return [left_child_index, right_child_index]

	def get_node_depth(self, node_index):
		return int(log(node_index+1, 2))

	def get_node(self, node_index):
		if node_index>= self.length:
			return None
		return self.priority_queue[node_index]

	def get_structure(self, node_index = 0):
		node_value = self.get_node(node_index)
		if node_value == None: # Base Case
			return None
		left_child_index, right_child_index = self.get_children_indices(node_index)
		left_child_value, right_child_value = (self.get_node(left_child_index),
			self.get_node(right_child_index))
		if left_child_value == right_child_value == None:
			return node_value


		return {str(node_value):[
		self.get_structure(left_child_index),
		self.get_structure(right_child_index)]
		}

	def print(self):
		print(json.dumps(self.get_structure(), indent=4))


	def find_node(self, node_value, root_index = 0):
		current_value = self.get_node(root_index)
		if current_value==node_value: # Base Case
			return root_index
		if current_value == None: # Base Case
			return False
		
		left_child_index, right_child_index = self.get_children_indices(root_index)

		#print(root_index, self.get_children_indices(root_index))
		#print(root_index, left_child_index)
		return (self.find_node(node_value, left_child_index) or 
			self.find_node(node_value, right_child_index))

	def insert(self, value):
		empty_index = self.find_node(None)
		if empty_index >= len(self.priority_queue):
			self.priority_queue.append(value)
		else:
			self.priority_queue[empty_index] = value
		self.length +=1

	"""def delete_node(self, node_value):
		node_index = self.find_node(node_value)
		if node_index == False: return # Node does not exist
		left_child_index, right_child_index = self.get_children_indices(node_index)
		left_child_value, right_child_value = (self.get_node(left_child_index),
			self.get_node(right_child_index))
		if left_child_value == left_child_value == None: # This can be deleted Easily
			self.priority_queue[node_index] = None
			self.length -=1
		if left_child_value == None:
			self.priority_queue[node_index] = 0# Edit later"""





my_mpq = MinPriorityQueue([7654,1324,12,1,0,75,7,6,8,3])

print(my_mpq.priority_queue)

my_mpq.print()

#pp([my_mpq.get_parent_index(node) for node in range(my_mpq.length)])
#pp([my_mpq.get_children_indices(node) for node in range(my_mpq.length)])



assertEqual(my_mpq.get_node_depth(0),0)
assertEqual(my_mpq.get_node_depth(1),1)
assertEqual(my_mpq.get_node_depth(2),1)
assertEqual(my_mpq.get_node_depth(3),2)
assertEqual(my_mpq.get_node_depth(4),2)
assertEqual(my_mpq.get_node_depth(5),2)
assertEqual(my_mpq.get_node_depth(6),2)
assertEqual(my_mpq.get_node_depth(7),3)

assertEqual(my_mpq.get_node(9), my_mpq.priority_queue[my_mpq.length-1])
assertEqual(my_mpq.get_node(10), None)
assertEqual(my_mpq.find_node(3), 2)
assertEqual(my_mpq.find_node(70000), False)




my_mpq.insert(900)
my_mpq.insert(1900)

my_mpq.print()



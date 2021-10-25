from pprint import pprint as pp
from random import randint

import unittest
from math import log

assertEqual = unittest.TestCase().assertEqual


class MinPriorityQueue():
	"""docstring for MinPriorityQueue"""
	priority_queue = []
	length = 0
	def __init__(self, priority_queue:list):
		self.priority_queue = sorted(priority_queue, reverse=True)
		self.length = len(self.priority_queue)
	
	def get_parent_index(self, node_index, do_assertions = True):
		if node_index == 0 or None: return None
		
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

	def print(self):
		pp(self.priority_queue)




my_mpq = MinPriorityQueue([randint(0,1000) for _ in range(10)])

my_mpq.print()

pp([my_mpq.get_parent_index(node) for node in range(my_mpq.length)])
pp([my_mpq.get_children_indices(node) for node in range(my_mpq.length)])



assertEqual(my_mpq.get_node_depth(0),0)
assertEqual(my_mpq.get_node_depth(1),1)
assertEqual(my_mpq.get_node_depth(2),1)
assertEqual(my_mpq.get_node_depth(3),2)
assertEqual(my_mpq.get_node_depth(4),2)
assertEqual(my_mpq.get_node_depth(5),2)
assertEqual(my_mpq.get_node_depth(6),2)
assertEqual(my_mpq.get_node_depth(7),3)

assertEqual(my_mpq.get_node(9), my_mpq.priority_queue[my_mpq.length-1])


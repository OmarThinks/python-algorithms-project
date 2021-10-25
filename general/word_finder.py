"""
After catching your classroom students cheating before, you realize your students are getting craftier and hiding words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

grid1 = [
    ['c', 'c', 'x', 't', 'i', 'b'],
    ['c', 'c', 'a', 't', 'n', 'i'],
    ['a', 'c', 'n', 'n', 't', 't'],
    ['t', 'c', 's', 'i', 'p', 't'],
    ['a', 'o', 'o', 'o', 'a', 'a'],
    ['o', 'a', 'a', 'a', 'o', 'o'],
    ['k', 'a', 'i', 'c', 'k', 'i'],
]
word1 = "catnip"
word2 = "cccc"
word3 = "s"
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"

find_word_location(grid1, word1) => [ (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
find_word_location(grid1, word2) =>
       [(0, 1), (1, 1), (2, 1), (3, 1)]
    OR [(0, 0), (1, 0), (1, 1), (2, 1)]
    OR [(0, 0), (0, 1), (1, 1), (2, 1)]
    OR [(1, 0), (1, 1), (2, 1), (3, 1)]
find_word_location(grid1, word3) => [(3, 2)]
find_word_location(grid1, word4) => [(0, 5), (1, 5), (2, 5)]
find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
find_word_location(grid1, word6) => [(6, 4), (6, 5)]
find_word_location(grid1, word7) => [(5, 1), (5, 2), (5, 3)]
find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
find_word_location(grid2, word9) => [(0, 0)]

Complexity analysis variables:

r = number of rows
c = number of columns
w = length of the word




"""




def is_word_in_scrambled(word: str, scrabmbled: str):
	word_list = list(word)
	scrabmbled_list = list(scrabmbled)
	#print(word_list)
	#print(scrabmbled_list)
	for letter in word_list:
		if letter in scrabmbled_list:
			scrabmbled_list.remove(letter)
			#print(scrabmbled_list)
		else:
			return False
	return True
		








#assert(is_word_in_scrambled("cat", "tcabnihjs")== True)


words = ["cat", "baby", "dog", "bird", "car", "ax"]
string1 = "tcabnihjs"
string2 = "tbcanihjs"
string3 = "baykkjl"
string4 = "bbabylkkj"
string5 = "ccc"
string6 = "breadmaking"

def find_embedded_word(words, string):
	for word in words:
		if is_word_in_scrambled(word,string) :
			return word
	return None

"""
Time Complexity: O(WS)
Space Complexity: O(W+S)
"""

"""

assert(find_embedded_word(words, string1)== "cat")
assert(find_embedded_word(words, string2)== "cat")
assert(find_embedded_word(words, string3)== None)
assert(find_embedded_word(words, string4)== "baby")
assert(find_embedded_word(words, string5)== None)
assert(find_embedded_word(words, string6)== "bird")

"""






























grid1 = [
    ['c', 'c', 'x', 't', 'i', 'b'],
    ['c', 'c', 'a', 't', 'n', 'i'],
    ['a', 'c', 'n', 'n', 't', 't'],
    ['t', 'c', 's', 'i', 'p', 't'],
    ['a', 'o', 'o', 'o', 'a', 'a'],
    ['o', 'a', 'a', 'a', 'o', 'o'],
    ['k', 'a', 'i', 'c', 'k', 'i'],
]
word1 = "catnip"
word2 = "cccc"
word3 = "s"
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"






"""
(1,1)

[(0,1),(0,1),(1,2),(2,1)]
"""

def add_to_queue(grid,new_point, path, word, queue):

	if new_point in path:
		return
	if len(path)>=len(word):
		return
	try:
		grid[new_point[0]][new_point[1]]
	except Exception as e:
		return
	new_path = path.copy()
	new_path.append(new_point)
	queue.append(new_path)



def look_around(grid,path,word,queue):
	point = path[-1]
	x = point[0]
	y = point[1]

	add_to_queue(grid,(x+1,y), path, word, queue)
	add_to_queue(grid,(x-1,y), path, word, queue)
	add_to_queue(grid,(x,y+1), path, word, queue)
	add_to_queue(grid,(x,y-1), path, word, queue)





def path_to_word(grid, path):
	letters_list = []
	for point in path:
		#print(point)
		#print(path)
		letters_list.append(grid[point[0]][point[1]])
	return "".join(letters_list)



def find_word_from_point(grid, point, word):
	max_length = len(word)
	queue = [[point]]
	path = []
	while len(queue)>0:
		path = queue.pop()
		current_word = path_to_word(grid,path)
		if current_word == word:
			return path
		look_around(grid,path,word,queue)
	return None

def find_word_location(grid, word):
	x_max = len(grid)
	y_max = len(grid[0])
	word_path = []
	for x in range(x_max):
		for y in range(y_max):
			word_path = find_word_from_point(grid, (x,y), word)
			if word_path != None:
				return word_path
	return None






print(find_word_location(grid1, word1))



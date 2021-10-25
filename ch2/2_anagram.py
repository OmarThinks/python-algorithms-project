"""
A string will be an anagram to another, 
if it is a rearrangement for it
"""




"""
Complexity of "O(n log(n))"
"""


def is_anagram_n_log_n(string_1,string_2):
	string_list_1 = list(string_1) # n
	string_list_2 = list(string_2) # n

	string_list_1.sort() # n log(n)
	string_list_2.sort() # n log(n)

	return (string_list_1 == string_list_2)



"""
T(n) = 2n + 2 n log(n)

"O(n log(n))"
"""

















"""
Complexity of "O(n))"
"""
"abccfbyrtbbc"
{
	"a":1,
	"b":2,
	"c":3
}

def is_anagram_linear(string_1,string_2):
	dict_1 = {}
	dict_2 = {}

	for char in string_1:
		if dict_1.get(char, None)==None:
			dict_1[char] = 1
		else:
			dict_1[char] +=1
	
	for char in string_2:
		if dict_2.get(char, None)==None:
			dict_2[char] = 1
		else:
			dict_2[char] +=1
	

	return (dict_1 == dict_2)



"""
T(n) = 1+1 +n*(1+1)*2 = 2 + 4n

"O(n)"

"O(n^2)"
"""










print({"a":1,"b":2}=={"b":2,"a":1})





new_list = []

new_list[6] = 400

print(new_list)








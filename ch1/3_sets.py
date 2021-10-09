
set_1 = {1,1,2,2,3,4,5,4,5,5,5,5,}

assert(set_1 == {1,2,3,4,5}) # ordered
assert(set_1 == {1,5,4,2,3}) # unordered





set_2 = {4,5,6,7,8,9}


assert(set_1 | set_2 == {1, 2, 3, 4, 5, 6, 7, 8, 9})
assert(set_1 & set_2 == {4, 5})

assert(set_1-set_2 == {1,2,3})
assert((set_1>=set_2) == False)



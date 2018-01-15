from functools import reduce

even_list = []
for x in range(100,500,2):
	even_list.append(x)

print(reduce(lambda x,y : x+y, even_list))

from functools import reduce

even_list = []
for x in range(0,5,2):
        even_list.append(x**2)

print(reduce(lambda x,y : (x+y), even_list))

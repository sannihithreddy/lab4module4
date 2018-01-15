def nested_sum(nested_list):
  sum=0
  for i in nested_list:
    if type(i)==list:
         sum+=nested_sum(i)
    else:
         sum+=i
  return sum
list1=[3,6,9,[1,2,3]]
print(nested_sum(list1))


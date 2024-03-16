#program to remove all even numbers from the beginning of a list
#eg: [2, 4, 6, 17, 10] -> [17, 10] 

def delete_starting_evens(list):
  for item in range(len(list),-1,-1): # changing to range 
    if list[item]%2==0:              # eheck element at index is even
      list.pop(item)
  return list

list = [2, 8, 10, 11
       #changes visible
print(delete_starting_evens(list))

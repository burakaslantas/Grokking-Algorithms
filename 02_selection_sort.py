def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if(array[i] < smallest):
            smallest = array[i]
            smallest_index = i
    return smallest_index

res = []
my_array = [32,2,25,3,11,78,-2,32]
print("my_array:", my_array)
for i in range(len(my_array)):
    smallest_index = find_smallest(my_array)
    res.append(my_array.pop(smallest_index))
print("res:", res)

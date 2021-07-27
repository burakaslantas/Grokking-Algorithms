def binary_search(array, searched_value):
    start = 0
    end = len(array) - 1

    while(start <= end):
        mid = (start + end) // 2
        guess = array[mid]
        if(searched_value == guess):
            return mid
        elif(searched_value < guess):
            end = mid - 1
        elif(searched_value > guess):
            start = mid + 1

    return -1

my_array = [32,2,25,3,11,78,-2,32]
my_array.sort()
print(my_array)
print(binary_search(my_array, 78))

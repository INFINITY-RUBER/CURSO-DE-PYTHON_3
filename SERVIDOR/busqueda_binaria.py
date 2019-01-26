import random

def binary_search(data, target, low, high):
    number_found=False;
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            number_found = True
            return number_found
        elif target < data[mid]:
            high = mid-1
        else:
            low = mid + 1

    return number_found        



if __name__=='__main__':
    data = [random.randint(0,100) for i in range(10)]
    data.sort()
    print(data)
    target = int(input('what number would you like to found?'))
    found = binary_search(data, target , 0, len(data)-1)
    print(found)
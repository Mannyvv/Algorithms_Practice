
def sum(array : list):
    
    if len(array) == 1:
        return array.pop()
    return array.pop() + sum(array)

print(sum([4,5,6,4,3,2,3,4,5]))
    





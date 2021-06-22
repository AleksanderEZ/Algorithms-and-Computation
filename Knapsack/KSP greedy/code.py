def ksp_greedy(items, capacity, taken):

    maxValue = 0
    maxValueAux = 0
    takenAux = taken.copy()
    capacityAux = capacity

    def forMethod():
        
        nonlocal capacity
        nonlocal capacityAux
        nonlocal maxValue
        nonlocal maxValueAux
        nonlocal taken
        nonlocal takenAux
        nonlocal items
        
        for item in items:
            if (capacity - item.weight >= 0):
                maxValueAux += item.value
                capacity -= item.weight
                takenAux[item.index] = 1
                
        if (maxValueAux > maxValue):
            maxValue = maxValueAux
            taken = takenAux
            
        capacity = capacityAux
        maxValueAux = 0
        takenAux = [0] * len(items)

    items.sort(reverse = True, key=lambda x: x.value)
    forMethod()
    
    items.sort(key=lambda x: x.weight)
    forMethod()
    
    items.sort(reverse = True, key=lambda x: x.value/x.weight)
    forMethod()
    
    return maxValue, taken
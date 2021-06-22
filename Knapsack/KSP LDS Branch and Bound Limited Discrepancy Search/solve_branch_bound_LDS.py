from node import *

# Modify this code to fix its errors and implement the Limited Discrepancy Search strategy

def solve_branch_bound_LDS(items: list, capacity: int) -> (int, list, list):
    
    root_node = Node(0, [], 0, capacity)
    best = root_node
    best_value = 0
    
    alive = [root_node]

    order_visiting = []

    while (len(alive) > 0):
        current = alive.pop()
        
        order_visiting.append(current.index)
        current_estimate = current.estimate(items)

        if current_estimate <= best_value:
            continue

        if current.value > best_value:
            best_value = current.value
            best = current

        if current.index >= len(items) or current.room == 0:
            continue

        right_node = Node(current.index + 1, 
                        current.path.copy(), 
                        current.value, 
                        current.room)
        alive.append(right_node)
        
        enough_room = current.room - items[current.index].weight
        if enough_room < 0:
            continue

        left_path = current.path.copy()
        left_path.append(current.index)
        
        left_node = Node(current.index + 1,
                         left_path,
                         current.value + items[current.index].value,
                         enough_room)
        
        alive.append(left_node)

    taken = [0] * len(items)

    for i in best.path:
        taken[items[i].index] = 1

    return best_value, taken, order_visiting
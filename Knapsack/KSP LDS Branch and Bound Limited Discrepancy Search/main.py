from solve_branch_bound_LDS import *

first_line = input().split() # N items, Capacity
item_count = int(first_line[0])
capacity = int(first_line[1])

items = []
for i in range(1, item_count+1):
    parts = input().split() # CSV
    items.append(Item(i-1, int(parts[0]), int(parts[1])))


value, taken, visiting_order = solve_branch_bound_LDS(items, capacity)

print(visiting_order)
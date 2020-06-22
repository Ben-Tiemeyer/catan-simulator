import random
def number_pull(robber):
    outer_start_index = random.randint(0, 11)
    outer_count = 0
    selection_order = []
    outer_circle = [8,9,10,17,24,30,36,35,34,27,20,14,8,9,10,17,24,30,36,35,34,27,20,14]
    inner_circle = [15,16,23,29,28,21,15,16,23,29,28,21]
    child_dict = {}
    for num in range(24):
        child_dict[outer_circle[num]] = inner_circle[int(num/2)]
    for num in range(12):
        selection = outer_circle[outer_start_index + outer_count]
        selection_order.append(selection)
        outer_count += 1
    inner_start_index = inner_circle.index(child_dict[selection])
    inner_count = 0
    for num in range(6):
        selection = inner_circle[inner_start_index + inner_count]
        selection_order.append(selection)
        inner_count += 1
    selection_order.append(22)
    number_mapper = {}
    number_order = [5,2,6,3,8,10,9,12,11,4,8,10,9,4,5,6,3,11]
    tile_count = 0
    for tile in selection_order:
        if tile != robber:
            number_mapper[tile] = str(number_order[tile_count])
            tile_count += 1
        else:
            number_mapper[tile] = ''
    return number_mapper

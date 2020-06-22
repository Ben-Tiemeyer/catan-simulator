import networkx as nx
def BuildingSpotSelection(spots, nobuild_spots):
    max_value = 0
    for spot in spots.keys():
        if spot not in nobuild_spots:
            spot_value = spots[spot].return_value()
            if spot_value > max_value:
                max_value = spot_value
                max_value_spot = spot
    return max_value_spot

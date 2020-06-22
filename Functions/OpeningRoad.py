import networkx as nx
def OpeningRoad(start, spots, buildable_spots, spot_network):
    max_value = 0
    road_target = 0
    max_search = 2
    while road_target == 0:
        for end in buildable_spots:
            distance = len(nx.shortest_path(spot_network, str(start), end))-1
            if distance == max_search:
                spot_value = spots[int(end)].return_value()
                if spot_value > max_value:
                    max_value = spot_value
                    road_target = int(nx.shortest_path(spot_network, str(start), end)[1])
        max_search = max_search + 1
    return road_target

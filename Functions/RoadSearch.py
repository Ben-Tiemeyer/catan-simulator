import networkx as nx
def RoadSearch(starts, spots, buildable_spots, spot_network, owned):
    max_value = 0
    road_target = 0
    max_search = 1
    while (road_target == 0) and (max_search < 7):
        for start in starts:
            for end in buildable_spots:
                try:
                    distance = len(nx.shortest_path(spot_network, str(start), end))-1
                except:
                    continue
                if distance == max_search:
                    duplicate = False
                    for owned_road in owned:
                        if (start in set(owned_road)) & (int(nx.shortest_path(spot_network, str(start), end)[1]) in set(owned_road)):
                            duplicate = True
                    if duplicate == False:
                        spot_value = spots[int(end)].return_value()
                        if (spot_value > max_value):
                            max_value = spot_value
                            road_target = int(nx.shortest_path(spot_network, str(start), end)[1])
                            road_start = start
        max_search = max_search + 1
    if road_target == 0:
        road_start = 0
    return road_start, road_target

from Functions.BuildNetwork import BuildNetwork
from Functions.BuildingSpotSelection import BuildingSpotSelection
from Functions.HexCoords import HexCoords
from Functions.number_pull import number_pull
from Functions.OpeningRoad import OpeningRoad
from Functions.pull_land import pull_land
from Functions.RoadSearch import RoadSearch
from Functions.Roll import Roll
from Functions.show_city import show_city
from Functions.show_road import show_road
from Functions.show_settlement import show_settlement
from Functions.StoreLines import StoreLines
from Functions.StorePoints import StorePoints

from Mappings.mappings import probability_dict
from Mappings.mappings import spot_road_dict
from Mappings.mappings import spot_tile_dict

import networkx as nx
import random

class Player():
    def __init__(self, color, id, hand = {}, points = 0, spots = [], settlements = [], cities = [], roads = [], network = BuildNetwork(), dev_card = None, army = 0):
        hand = {}
        points = 0
        spots = []
        settlements = []
        cities = []
        roads = []
        hand['BRICK'] = 0
        hand['WHEAT'] = 0
        hand['WOOD'] = 0
        hand['ORE'] = 0
        hand['SHEEP'] = 0
        dev_card = None
        army = 0
        self.__color = color
        self.__hand = hand
        self.__points = points
        self.__spots = spots
        self.__settlements = settlements
        self.__cities = cities
        self.__roads = roads
        self.__network = BuildNetwork()
        self.__id = id
        self.__dev_card = dev_card
        self.__army = army

    def print_attributes(self):
        return self.__hand, self.__points, self.__spots, self.__settlements, self.__cities, self.__roads, self.__id, self.__dev_card, self.__army

    def return_points(self):
        return self.__points

    def return_network(self):
        return self.__network

    def return_color(self):
        return self.__color

    def lose_points(self, amount):
        self.__points -= amount

    def get_monopolized(self, resource):
        self.__hand[resource] = 0

    def return_hand(self):
        return self.__hand

    def edit_network(self, opp_settlements, opp_roads):
        for settlement in opp_settlements:
            try:
                self.__network.remove_node(str(settlement))
            except:
                continue
        if len(opp_roads) >= 1:
            for road in opp_roads:
                start = road[0]
                end = road[1]
                try:
                    self.__network.remove_edge(str(start), str(end))
                except:
                    continue

    def reap(self, roll, spots):
        for settlement in self.__settlements:
            count = 0
            settlement = spots[settlement]
            for number in settlement.return_numbers():
                if number == roll:
                    resource = settlement.return_tile_ids()[count].return_resource()
                    self.__hand[resource] += 1
                count += 1
        for city in self.__cities:
            count = 0
            city = spots[city]
            for number in city.return_numbers():
                if number == roll:
                    resource = city.return_tile_ids()[count].return_resource()
                    self.__hand[resource] += 1
                count += 1

    def build_settlement(self, spot, DISPLAY, point_list):
        self.__spots.append(spot)
        self.__settlements.append(spot)
        self.__points += 1
        show_settlement(DISPLAY, point_list, spot, self.__color)

    def build_city(self, spot, DISPLAY, point_list):
        self.__spots.append(spot)
        self.__cities.append(spot)
        self.__points += 1
        show_city(DISPLAY, point_list, spot, self.__color)

    def build_road(self, start, end, DISPLAY, line_list):
        if end not in self.__spots:
            self.__spots.append(end)
        elif start not in self.__spots:
            self.__spots.append(start)
        self.__roads.append([start, end])
        show_road(DISPLAY, line_list, start, end, self.__color)

    def draw_card(self, resource):
        if resource != 'NADA':
            self.__hand[resource] += 1

    def use_cards(self, spots, DISPLAY, point_list, line_list, nobuild_spots, dev_cards, players):
        output = [[], []]
        id = self.__id
        if self.__dev_card != None:
            if self.__dev_card == 'RB':
                for i in [1,2]:
                    start, road = RoadSearch(self.__spots, spots, [str(x) for x in spots.keys() if x not in nobuild_spots], self.__network, self.__roads)
                    if (start, road) != (0,0):
                        self.build_road(start, road, DISPLAY, line_list)
                        output[1].append([start, road])
                self.__dev_card = None
            elif self.__dev_card == 'YOP':
                resources = ['WHEAT', 'ORE', 'BRICK', 'WOOD', 'SHEEP']
                pull1 = resources[random.randint(0,4)]
                self.draw_card(pull1)
                pull2 = resources[random.randint(0,4)]
                self.draw_card(pull2)
                self.__dev_card = None
            elif self.__dev_card == 'M':
                opponent_cards = {}
                count = 0
                for p in [1,2,3,4]:
                    if p != id:
                        hand = players[p].return_hand()
                        for resource in hand.keys():
                            if count == 0:
                                opponent_cards[resource] = hand[resource]
                            else:
                                opponent_cards[resource] = opponent_cards[resource] + hand[resource]
                        count += 1
                max_resource_quantity = 0
                for resource in opponent_cards.keys():
                    if opponent_cards[resource] > max_resource_quantity:
                        max_resource = resource
                        max_resource_quantity = opponent_cards[resource]
                for p in [1,2,3,4]:
                    if p != id:
                        players[p].get_monopolized(max_resource)
                self.__hand[max_resource] += max_resource_quantity
                self.__dev_card = None
            elif self.__dev_card == 'K':
                resources = ['WHEAT', 'ORE', 'BRICK', 'WOOD', 'SHEEP']
                pull1 = resources[random.randint(0,4)]
                self.draw_card(pull1)
                self.__army += 1
                self.__dev_card = None
        if (len(self.__settlements) > 0) & (len(self.__cities) < 4) & (self.__hand['WHEAT'] >= 3) & (self.__hand['ORE'] >= 2):
            max_value_spot = 0
            for spot in self.__settlements:
                if spot not in self.__cities:
                    spot_value = spots[spot].return_value()
                    if spot_value > max_value_spot:
                        max_value_spot = spot_value
                        build_spot = spot
            if max_value_spot != 0:
                self.build_city(build_spot, DISPLAY, point_list)
                self.__hand['WHEAT'] -= 3
                self.__hand['ORE'] -= 2
        if ((len(self.__settlements)-len(self.__cities)) < 5) & (self.__hand['WHEAT'] >= 1) & (self.__hand['BRICK'] >= 1)  & (self.__hand['WOOD'] >= 1)  & (self.__hand['SHEEP'] >= 1):
            max_value_spot = 0
            for spot in self.__spots:
                if (spot not in nobuild_spots) and (spot not in self.__settlements) and (spot not in self.__cities):
                    spot_value = spots[spot].return_value()
                    if spot_value > max_value_spot:
                        max_value_spot = spot_value
                        build_spot = spot
            if max_value_spot != 0:
                self.build_settlement(build_spot, DISPLAY, point_list)
                output[0].append(build_spot)
                self.__hand['WHEAT'] -= 1
                self.__hand['SHEEP'] -= 1
                self.__hand['BRICK'] -= 1
                self.__hand['WOOD'] -= 1
        if (len(dev_cards) > 0) & (self.__hand['WHEAT'] >= 1) & (self.__hand['SHEEP'] >= 1) & (self.__hand['ORE'] >= 1):
            self.__hand['WHEAT'] -= 1
            self.__hand['SHEEP'] -= 1
            self.__hand['ORE'] -= 1
            choice = dev_cards[random.randint(0,len(dev_cards)-1)]
            dev_cards.remove(choice)
            if choice == 'VP':
                #print('Player', id, 'Pulled a victory point!')
                self.__points += 1
            else:
                self.__dev_card = choice
        if (len(self.__roads) < 15) & (self.__hand['BRICK'] >= 1) & (self.__hand['WOOD'] >= 1):
            start, road = RoadSearch(self.__spots, spots, [str(x) for x in spots.keys() if x not in nobuild_spots], self.__network, self.__roads)
            if (start, road) != (0,0):
                self.build_road(start, road, DISPLAY, line_list)
                output[1].append([start, road])
                self.__hand['WOOD'] -= 1
                self.__hand['BRICK'] -= 1
        loaded = []
        low = {}
        for resource in sorted(self.__hand.keys()):
            if self.__hand[resource] >= 4:
                loaded.append(resource)
            else:
                low[self.__hand[resource]] = resource
        if (len(low.keys()) > 0) & (len(loaded) >= 1):
            for loaded_resource in loaded:
                self.__hand[loaded_resource] -= 4
                self.__hand[low[sorted(low.keys())[0]]] += 1

        return output

    def EvaluateLargestArmy(self, current_largest_army, current_army_champion, players):
        army = self.__army
        if army > current_largest_army:
            self.__points += 2
            try:
                players[current_army_champion].lose_points(2)
            except:
                first_time = True
            return army, self.__id
        else:
            return current_largest_army, current_army_champion

    def CalculateLongestRoad(self, current_longest_road, current_road_champion, players):
        roads = self.__roads
        spot_network = nx.Graph()
        for road in roads:
            node1 = road[0]
            node2 = road[1]
            spot_network.add_edge(str(node1), str(node2))
        all_nodes = []
        for road in roads:
            for node in road:
                if node not in all_nodes:
                    all_nodes.append(node)
        longest_road = 0
        for start_node in all_nodes:
            for end_node in [x for x in all_nodes if x != start_node]:
                try:
                    path_nodes = max((path for path in nx.all_simple_paths(spot_network, str(start_node), str(end_node))))
                    longest_path = len(path_nodes)
                    if longest_path > longest_road:
                        add_one = 0
                        count = 0
                        for spot in spot_network.neighbors(str(path_nodes[-1])):
                            count += 1
                        if count > 1:
                            add_one = 1
                        longest_road = longest_path + add_one
                        nodes = [start_node, end_node]
                        longest_path_nodes = path_nodes
                except:
                    continue
        longest_road = longest_road - 1
        if longest_road > current_longest_road:
            self.__points += 2
            try:
                players[current_road_champion].lose_points(2)
            except:
                first_time = True
            return longest_road, self.__id
        else:
            return current_longest_road, current_road_champion

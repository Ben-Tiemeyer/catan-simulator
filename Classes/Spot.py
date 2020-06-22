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

class Spot():
    def __init__(self, uid, tiles, numbers, value, classification='Empty'):
        self.__uid = uid
        self.__tiles = tiles
        self.__numbers = numbers
        self.__value = value
        self.__classification = classification

    def print_attributes(self):
        return print(self.__uid, self.__tiles, self.__numbers, self.__value, self.__classification)

    def return_numbers(self):
        return self.__numbers

    #Actually returns tile objects rather than tile ids
    def return_tile_ids(self):
        return self.__tiles

    def return_value(self):
        return self.__value

    def build_settlement(self, owner):
        self.__classification = 'settlement'

    def build_city(self, owner):
        self.__classification = 'city'

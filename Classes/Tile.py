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

class Tile():
    def __init__(self, uid, resource, number_tile):
        self.__uid = uid
        self.__resource = resource
        self.__number_tile = number_tile

    def print_attributes(self):
        return print(self.__uid, self.__resource, self.__number_tile)

    def return_resource(self):
        return self.__resource

    def return_number_tile(self):
        return self.__number_tile

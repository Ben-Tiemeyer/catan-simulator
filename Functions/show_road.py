import pygame
from pygame.locals import *

from Mappings.mappings import probability_dict
from Mappings.mappings import spot_road_dict
from Mappings.mappings import spot_tile_dict

def show_road(DISPLAY, line_list, start, end, color):
    if start < end:
            road_key = int(str(start)+str(end))
    else:
        road_key = int(str(end)+str(start))
    font = pygame.font.Font('freesansbold.ttf', 12)
    pygame.draw.line(DISPLAY, color, line_list[spot_road_dict[road_key]-1][0], line_list[spot_road_dict[road_key]-1][1], 5)
    pygame.display.update()

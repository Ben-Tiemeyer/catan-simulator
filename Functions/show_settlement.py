import pygame
from pygame.locals import *

from Mappings.mappings import probability_dict
from Mappings.mappings import spot_road_dict
from Mappings.mappings import spot_tile_dict

def show_settlement(DISPLAY, point_list, start, color):
    font = pygame.font.Font('freesansbold.ttf', 116)
    text = font.render('.', True, color)
    DISPLAY.blit(text, (point_list[start-1][0]-15, point_list[start-1][1]-85))
    pygame.display.update()

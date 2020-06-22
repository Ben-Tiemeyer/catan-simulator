import networkx as nx
import random
import pygame
from pygame.locals import *
import sys
import time
import pandas as pd

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

from Classes.Player import Player
from Classes.Spot import Spot
from Classes.Tile import Tile

from Mappings.mappings import probability_dict
from Mappings.mappings import spot_road_dict
from Mappings.mappings import spot_tile_dict

def main(spectate):

    #Initialize pygame
    pygame.init()
    pygame.font.init()
    DISPLAY=pygame.display.set_mode((625,600))
    pygame.display.set_caption('Settlers of Catan')
    WHITE=(255,255,255)
    DISPLAY.fill(WHITE)


    #Randomly Assign Land Tiles
    WHITE=(255,255,255)
    BLUE=(0,0,255)
    colors = [BLUE]*46
    land, resource = pull_land()
    tile_resources = {}
    land_count = 1
    for number in [8,9,10,14,15,16,17,20,21,22,23,24,27,28,29,30,34,35,36]:
        colors[number] = land[land_count]
        tile_resources[number] = resource[land_count]
        land_count += 1

    ############Create Hexagonal Board Pieces#################

    size = 100
    start = 50
    running_counter = 0
    center_list = []
    point_list = []
    line_list = []

    ############ First Row of Tiles
    hex_center = (start+((size/4)*(3**(1/2))),start)
    center_list.append(hex_center)
    if colors[running_counter] == (255, 255, 255):
            robber = running_counter
    points = HexCoords(size, hex_center)
    point_list = StorePoints(points[0], point_list, running_counter)
    line_list = StoreLines(points[0], line_list, running_counter)
    pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
    running_counter += 1

    count = 0
    while count < 5:
        hex_center = (points[2][0]+(2*points[1]),start)
        center_list.append(hex_center)
        if colors[running_counter] == (255, 255, 255):
            robber = running_counter
        points = HexCoords(size, hex_center)
        point_list = StorePoints(points[0], point_list, running_counter)
        line_list = StoreLines(points[0], line_list, running_counter)
        pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
        count = count + 1
        running_counter += 1


    ############ Second Row of Tiles
    hex_center = (start,start+(size*3/4))
    center_list.append(hex_center)
    if colors[running_counter] == (255, 255, 255):
        robber = running_counter
    points = HexCoords(size, hex_center)
    point_list = StorePoints(points[0], point_list, running_counter)
    line_list = StoreLines(points[0], line_list, running_counter)
    pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
    running_counter += 1

    count = 0
    while count < 6:
        hex_center = (points[2][0]+(2*points[1]),start+(size*3/4))
        center_list.append(hex_center)
        if colors[running_counter] == (255, 255, 255):
            robber = running_counter
        points = HexCoords(size, hex_center)
        point_list = StorePoints(points[0], point_list, running_counter)
        line_list = StoreLines(points[0], line_list, running_counter)
        pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
        count = count + 1
        running_counter += 1

    ############ Third Row of Tiles
    hex_center = (start+((size/4)*(3**(1/2))),start+(size*6/4))
    center_list.append(hex_center)
    if colors[running_counter] == (255, 255, 255):
        robber = running_counter
    points = HexCoords(size, hex_center)
    point_list = StorePoints(points[0], point_list, running_counter)
    line_list = StoreLines(points[0], line_list, running_counter)
    pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
    running_counter += 1

    count = 0
    while count < 5:
        hex_center = (points[2][0]+(2*points[1]),start+(size*6/4))
        center_list.append(hex_center)
        if colors[running_counter] == (255, 255, 255):
            robber = running_counter
        points = HexCoords(size, hex_center)
        point_list = StorePoints(points[0], point_list, running_counter)
        line_list = StoreLines(points[0], line_list, running_counter)
        pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
        count = count + 1
        running_counter += 1

    ############ Fourth Row of Tiles
    hex_center = (start,start+(size*9/4))
    center_list.append(hex_center)
    if colors[running_counter] == (255, 255, 255):
            robber = running_counter
    points = HexCoords(size, hex_center)
    point_list = StorePoints(points[0], point_list, running_counter)
    line_list = StoreLines(points[0], line_list, running_counter)
    pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
    running_counter += 1

    count = 0
    while count < 6:
        hex_center = (points[2][0]+(2*points[1]),start+(size*9/4))
        center_list.append(hex_center)
        if colors[running_counter] == (255, 255, 255):
            robber = running_counter
        points = HexCoords(size, hex_center)
        point_list = StorePoints(points[0], point_list, running_counter)
        line_list = StoreLines(points[0], line_list, running_counter)
        pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
        count = count + 1
        running_counter += 1

    ############ Fifth Row of Tiles
    hex_center = (start+((size/4)*(3**(1/2))),start+(size*12/4))
    center_list.append(hex_center)
    if colors[running_counter] == (255, 255, 255):
        robber = running_counter
    points = HexCoords(size, hex_center)
    point_list = StorePoints(points[0], point_list, running_counter)
    line_list = StoreLines(points[0], line_list, running_counter)
    pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
    running_counter += 1

    count = 0
    while count < 5:
        hex_center = (points[2][0]+(2*points[1]),start+(size*12/4))
        center_list.append(hex_center)
        if colors[running_counter] == (255, 255, 255):
            robber = running_counter
        points = HexCoords(size, hex_center)
        point_list = StorePoints(points[0], point_list, running_counter)
        line_list = StoreLines(points[0], line_list, running_counter)
        pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
        count = count + 1
        running_counter += 1

    ############ Sixth Row of Tiles
    hex_center = (start,start+(size*15/4))
    center_list.append(hex_center)
    if colors[running_counter] == (255, 255, 255):
        robber = running_counter
    points = HexCoords(size, hex_center)
    point_list = StorePoints(points[0], point_list, running_counter)
    line_list = StoreLines(points[0], line_list, running_counter)
    pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
    running_counter += 1

    count = 0
    while count < 6:
        hex_center = (points[2][0]+(2*points[1]),start+(size*15/4))
        center_list.append(hex_center)
        if colors[running_counter] == (255, 255, 255):
            robber = running_counter
        points = HexCoords(size, hex_center)
        point_list = StorePoints(points[0], point_list, running_counter)
        line_list = StoreLines(points[0], line_list, running_counter)
        pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
        count = count + 1
        running_counter += 1

    ############ Seventh Row of Tiles
    hex_center = (start+((size/4)*(3**(1/2))),start+(size*18/4))
    center_list.append(hex_center)
    if colors[running_counter] == (255, 255, 255):
        robber = running_counter
    points = HexCoords(size, hex_center)
    point_list = StorePoints(points[0], point_list, running_counter)
    line_list = StoreLines(points[0], line_list, running_counter)
    pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
    running_counter += 1

    count = 0
    while count < 5:
        hex_center = (points[2][0]+(2*points[1]),start+(size*18/4))
        center_list.append(hex_center)
        if colors[running_counter] == (255, 255, 255):
            robber = running_counter
        points = HexCoords(size, hex_center)
        point_list = StorePoints(points[0], point_list, running_counter)
        line_list = StoreLines(points[0], line_list, running_counter)
        pygame.draw.polygon(DISPLAY,colors[running_counter],points[0])
        count = count + 1
        running_counter += 1

    ############Done Creating Hexagonal Game Board Pieces#################

    #Add Ports
    font = pygame.font.Font('freesansbold.ttf', 24)
    text = font.render('2:1', True, (255,255,0))
    text = pygame.transform.rotate(text, 330)
    DISPLAY.blit(text, (260,455))
    text = font.render('3:1', True, (0,0,0))
    text = pygame.transform.rotate(text, 30)
    DISPLAY.blit(text, (405,455))
    text = font.render('2:1', True, (0,100,0))
    text = pygame.transform.rotate(text, 90)
    DISPLAY.blit(text, (485,335))
    text = font.render('2:1', True, (204,85,0))
    text = pygame.transform.rotate(text, 90)
    DISPLAY.blit(text, (485,185))
    text = font.render('3:1', True, (0,0,0))
    text = pygame.transform.rotate(text, -30)
    DISPLAY.blit(text, (405,60))
    text = font.render('3:1', True, (0,0,0))
    text = pygame.transform.rotate(text, 30)
    DISPLAY.blit(text, (265,57))
    text = font.render('2:1', True, (124,252,0))
    text = pygame.transform.rotate(text, 30)
    DISPLAY.blit(text, (132,132))
    text = font.render('3:1', True, (0,0,0))
    text = pygame.transform.rotate(text, 90)
    DISPLAY.blit(text, (68,258))
    text = font.render('2:1', True, (68,60,84))
    text = pygame.transform.rotate(text, -30)
    DISPLAY.blit(text, (130,380))

    #Assign Numbers to Tiles and Create 19 Tile Objects
    numbers = number_pull(robber)
    center_list = [(item[0]-8, item[1]-15) for item in center_list]
    font = pygame.font.Font('freesansbold.ttf', 32)
    tiles = {}
    for number in [8,9,10,14,15,16,17,20,21,22,23,24,27,28,29,30,34,35,36]:
        tiles[number] = Tile(number, tile_resources[number], numbers[number])
        text = font.render(str(numbers[number]), True, (0,0,0))
        if len(numbers[number]) > 1:
            center_list[number] = (center_list[number][0]-8, center_list[number][1])
        DISPLAY.blit(text, center_list[number])


    #Mark corner spots on board and Create 54 Spot Obejcts
    spots = {}
    #font = pygame.font.Font('freesansbold.ttf', 48)
    #font = pygame.font.Font('freesansbold.ttf', 12)
    count = 1
    for point in point_list:
        tile_ids = spot_tile_dict[count]
        values = [numbers[x] for x in tile_ids]
        values = ['0' if x == '' else x for x in values]
        values = list(map(int, values))
        value = sum([probability_dict[x] for x in values])
        spots[count] = Spot(count, [tiles[x] for x in tile_ids], values, value)
        #text = font.render('.', True, (0,0,0))
        #DISPLAY.blit(text, (point[0]-6, point[1]-35))
        #text = font.render(str(count), True, (0,0,0))
        #DISPLAY.blit(text, (point[0]-8, point[1]-8))
        count += 1

    #Mark lines that connect spots
    #font = pygame.font.Font('freesansbold.ttf', 12)
    count = 1
    for line in line_list:
        pygame.draw.line(DISPLAY, (0,0,0), line[0], line[1], 1)
        #text = font.render(str(count), True, (100,0,0))
        #DISPLAY.blit(text, (((line[0][0]+line[1][0])/2)-8, ((line[0][1]+line[1][1])/2)-8))
        count += 1

    pygame.display.update()

    players = {}
    players[1] = Player(color=(0,0,139), id = 1)
    players[2] = Player(color=(254,127,156), id = 2)
    players[3] = Player(color=(106, 13, 173), id = 3)
    players[4] = Player(color=(215,215,215), id = 4)

    nobuild_spots = []

    print('                                 ')

    starting_spots = {}
    for p in [1,2,3,4]:
        starting_spots[p] = {}
        for resource in ['WHEAT', 'ORE', 'WOOD', 'BRICK', 'SHEEP']:
            starting_spots[p][resource] = 0

    time.sleep(0.5)

    count = 0
    for p in [1,2,3,4,4,3,2,1]:
        count += 1
        start = BuildingSpotSelection(spots, nobuild_spots)
        road = OpeningRoad(start, spots, [str(x) for x in spots.keys() if x not in nobuild_spots], players[1].return_network())
        players[p].build_settlement(start, DISPLAY, point_list)
        players[p].build_road(start, road, DISPLAY, line_list)
        for spot in players[p].return_network().neighbors(str(start)):
            nobuild_spots.append(int(spot))
        nobuild_spots.append(start)
        for tile in spots[start].return_tile_ids():
            number = tile.return_number_tile()
            resource = tile.return_resource()
            try:
                starting_spots[p][resource] += probability_dict[int(number)]
            #For when starting spot is on desert tile
            except:
                continue
        for opp_player in [x for x in [1,2,3,4] if x != p]:
            players[opp_player].edit_network([start], [[start, road]])
        if count > 4:
            for tile in spots[start].return_tile_ids():
                players[p].draw_card(str(tile.return_resource()))
        if spectate is True:
            time.sleep(0.5)

    points = 0
    turn_count = 0
    current_longest_road = 4
    current_road_champion = 0
    current_largest_army = 2
    current_army_champion = 0

    v = ['VP']*5
    p = ['YOP']*2
    m = ['M']*2
    k = ['K']*14
    r = ['RB']*2
    dev_cards = []
    for card_type in [v,p,m,k,r]:
        for card in card_type:
            dev_cards.append(card)

    while points < 10:
        p = turn_count%4 + 1
        roll_result = Roll()
        for each in [1,2,3,4]:
            players[each].reap(roll_result, spots)
        turn_output = players[p].use_cards(spots, DISPLAY, point_list, line_list, nobuild_spots, dev_cards, players)
        for opp_player in [x for x in [1,2,3,4] if x != p]:
            players[opp_player].edit_network(turn_output[0], turn_output[1])
        for build in turn_output[0]:
            for spot in BuildNetwork().neighbors(str(build)):
                nobuild_spots.append(int(spot))
            nobuild_spots.append(build)
        current_longest_road, current_road_champion = players[p].CalculateLongestRoad(current_longest_road, current_road_champion, players)
        current_largest_army, current_army_champion = players[p].EvaluateLargestArmy(current_largest_army, current_army_champion, players)
        points = players[p].return_points()
        if spectate is True:
            time.sleep(0.1)
        #print(p, turn_count, points)
        turn_count += 1

    print('                                 ')
    print('Player #'+str(p)+' Wins The Game in', turn_count, 'turns!')
    print('                                 ')
    print('Largest Army:', current_largest_army, 'Player:',current_army_champion)
    print('Longest Road:', current_longest_road, 'Player:', current_road_champion)
    print('                                 ')
    print('FINAL SCOREBOARD:')
    print('-------------------')
    print('Player 1 (Blue):', players[1].return_points())
    print('Player 2 (Pink):', players[2].return_points())
    print('Player 3 (Purple):', players[3].return_points())
    print('Player 4 (Gray):', players[4].return_points())

    results_df = pd.DataFrame()

    for p in [1,2,3,4]:
        total_starting_prob = 0
        for resource in ['BRICK', 'ORE', 'SHEEP', 'WHEAT', 'WOOD']:
            total_starting_prob += starting_spots[p][resource]
            starting_spots[p][resource] = [starting_spots[p][resource]]
        starting_spots[p]['TOTAL'] = [total_starting_prob]
        starting_spots[p]['POINTS PER TURN'] = [players[p].return_points() / turn_count]
        new_row = pd.DataFrame.from_dict(starting_spots[p])
        results_df = pd.concat([results_df, new_row], sort=False)


    pygame.quit()

    #while True:
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            pygame.quit()
    #            sys.exit()

    return results_df

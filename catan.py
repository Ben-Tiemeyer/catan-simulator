import networkx as nx
import random
import pygame
from pygame.locals import *
import sys
import time
import pandas as pd

from Functions.main import main

results_df = pd.DataFrame()

spectate_input = input('Spectate? (Y/N): ')
if spectate_input == 'Y':
    spectate = True
else:
    spectate = False

try:
    i_input = int(input('How many games do you want to simulate? '))
except:
    print('input error, running 1 simulation')
    i_input = 1

save_input = input('Do you want to save the results of the simulations? (Y/N): ')
if save_input == 'Y':
    save = True
else:
    save = False

i = 0
while i < i_input:
    new_row = main(spectate)
    i += 1
    results_df = pd.concat([results_df, new_row], sort=False)
    print(i)

#print(results_df.reset_index(drop=True))
random_integer = str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
if save is True:
    results_df.to_csv('catan_simulation_results_'+random_integer+'.csv', index=None)

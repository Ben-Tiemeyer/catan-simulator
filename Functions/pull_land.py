import random
def pull_land():
    color_dict = {}
    resource_dict = {}
    dark_green = (0,100,0)
    red = (204,85,0)
    yellow = (255,255,0)
    gray = (68,60,84)
    light_green = (124,252,0)
    white = (255,255,255)
    already_chosen = []
    counter = 0
    for i in range(19):
        choice = random.randint(1, 19)
        while choice in already_chosen:
            choice = random.randint(1, 19)
        if choice <= 4:
            counter += 1
            color_dict[counter] = dark_green
            resource_dict[counter] = 'WOOD'
            already_chosen.append(choice)
        elif choice <= 7:
            counter += 1
            color_dict[counter] = red
            resource_dict[counter] = 'BRICK'
            already_chosen.append(choice)
        elif choice <= 11:
            counter += 1
            color_dict[counter] = yellow
            resource_dict[counter] = 'WHEAT'
            already_chosen.append(choice)
        elif choice <= 14:
            counter += 1
            color_dict[counter] = gray
            resource_dict[counter] = 'ORE'
            already_chosen.append(choice)
        elif choice <= 18:
            counter += 1
            color_dict[counter] = light_green
            resource_dict[counter] = 'SHEEP'
            already_chosen.append(choice)
        else:
            counter += 1
            color_dict[counter] = white
            resource_dict[counter] = 'NADA'
            already_chosen.append(choice)
    return (color_dict, resource_dict)

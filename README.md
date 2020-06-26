# catan-simulator

### This project simulates and records the results of a game of Settlers of Catan with 4 computer players.
See Video: https://github.com/Ben-Tiemeyer/catan-simulator/blob/master/catan_simulation.mp4

![Board](https://github.com/Ben-Tiemeyer/catan-simulator/blob/master/Images/Board.PNG?raw=true)

For each simulation run, the following data is stored:
- The amount of probability pips that each player started adajcent to for each resource
- Each player's points per turn for that game
      
This data is saved to a csv in the following format, with each row representing a player's results:
| WHEAT      | ORE   | WOOD     | BRICK | SHEEP | TOTAL | POINTS PER TURN |
| :---:      |:----: |    :---: | :---: | :---: | :---: | :----:       |
| 4     | 3 | 8  | 4 | 2 | 21 | 0.1786 | 
| 3     | 0 | 9  | 4 | 6 | 22 | 0.0555 |
| 7     | 5 | 4  | 4 | 2 | 22 | 0.1882 | 
| 4     | 2 | 7  | 2 | 5 | 20 | 0.0852 |
      
      
### With enough simulations, this data can be used to calculate each resource's relative value.
Using Linear Regression on a data set comprised of 1,000 Game Simulations

![Resource Values](https://github.com/Ben-Tiemeyer/catan-simulator/blob/master/Images/Starting_Resource_Values.png?raw=true)

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

![Resource Values](https://github.com/Ben-Tiemeyer/catan-simulator/blob/master/Images/Starting_Resource_Values.png?raw=true)<br/><br/>

## Methodology
The four computer (AI) players simulate a game of Catan by all playing according to the following policies:<br/>
- Settlements and Cities are built upon the available spot with the highest cumulative probability pips (regardless of resource)<br/>
- Roads are built towards the avialable spot with the highest cumulative probability pips that is only 1 spot away (regardless of resource)<br/>
    - If no spots are avaialble to build 1 spot away, then searches 2 spots away, and so on until it can find an available spot to build towards<br/>
- Cards are used by the AI players each turn in the following sequence:<br/>
    1) Any avaiable development cards are used<br/>
    2) A city is built if the player: <br/>
    - has a city remaining, <br/>
    - has the needed resources, <br/>
    - has an available settlement on which to build<br/>
            - 3) A settlement is if the player:<br/>
                  has a settlement remaining<br/>
                  has the resources<br/>
                  has an available spot to build that is not adjacent to another settlement/city<br/>
            - 4) A development card is purchased if the player has the available resources to purchase a development card<br/>
            - 5) A road is built if the player <br/>
                  has a road remaining<br/>
                  has the resources to build a road<br/>
                  has an available spot to build<br/>
            - 6) If the player has 4 remaining cards of any resource, they will trade in those 4 cards for 1 card of the resource that they have the least of<br/>
      

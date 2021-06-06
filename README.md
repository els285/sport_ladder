# Sports Ladder

Python scripts for maintaing a sports ladder competition. Designed with tennis in mind, but applicable to a general class of set-based racquet sports. 

Generates a random ladder based on an input set of players. Subsequent matches between those players alters the ladder positions.
Player statistics are also stored, including number of games, sets and matches won.


## Example

Initialise a set of players:
```python
Ethan     = Player("Ethan")
Caroline  = Player("Caz")
Chris     = Player("Chris")
Flora     = Player("Flora")
```

Generate a competition ladder with a defined name and set of pre-defined players:

```python
Spring_Ladder = Ladder("Spring League Competition",[Ethan,Flora,Chris,Caroline])
```
The ordering of players here is defined randonmly.

Add matches:
```python
Spring_Ladder.AddMatch(flora,chris,"1st June 2021",((6,4),(7,6)))
Spring_Ladder.AddMatch(ethan,caz,"3rd June 2021",((6,3),(6,2)))
```

Print the ladder order:
```python
Spring_Ladder.ShowLadder()
```


## To Do
* Implement visualisation in the form of discrete time series
* Derive child classes based on different rules or different sports
* Convert to Python app



## API

### Player Class
Stores information about player, their current and past positions, and their statistics

### Match Class
A Match is an object representing a match between two individuals, with a defined winner, loser and score.

### Ladder Class
The Ladder class represents the competition. Matches are added to the Ladder, which then updates the players' positions.

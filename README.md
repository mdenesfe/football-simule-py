# Football Simulator

This code snippet reads the players of two teams entered by the user, calculates the player scores of the teams and simulates a football match.

## Getting Started

1. First, the user enters the names of two teams.
2. Reads the players to create the teams.
3. Calculates the attack, defense and midfield scores of each team.
4. Takes the average score of the teams.
5. Applies a random average with normal distribution and determines the score of the match.
6. During the match, the scorer is determined for each goal and the fatigue levels of the players are updated.
7. At the end of the match, the score is printed on the screen.

## Requirements

The only requirement for this code snippet is python 3.x.

## Running

To run this code snippet, you only need to run `python main.py` command in your console or terminal.

## Contributors
- [mdenesfe](https://github.com/mdenesfe)

## Notes

- The player information is read from the players.csv file based on the team names entered by the user, sufficient player information must be present in this file.
- The fatigue levels of the players are increased after each goal, but there is no possibility of substituting players like in a real football game.
- The score is determined randomly and factors such as tactics, player performances do not affect it as they would in a real football game.

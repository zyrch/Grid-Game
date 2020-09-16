
GridWorld Game

You have to create a game in python where the player has to reach the goal position from the
start position, collecting all the randomly spawned rewards and avoiding obstacles.

● The grid is of size n X n. You have to take n as an input from the user. The start and goal
positions should be randomly placed on the boundary.

● There are obstacles in some of the cells of the grid and their positions should also be
random.

● The player can make moves like up, down, left and right and 2 special moves - rotate
clockwise and rotate anticlockwise. You have to implement functions for each of the
moves to achieve their functionality. The moves are case insensitive.

● A move is to be taken as input from the player. For instance, R4D3L2U1 means move 4
units to the right, then 3 units down, then 2 units to the left and finally 1 unit upwards.
(The input need not necessarily contain all R, L, U and D. For example, R4D3 is also a
valid input). You have to take these inputs from the player until it loses all its energy or
reaches the goal position.

● The special moves (rotate anti/clockwise) must also be taken as input from the player. If
the input is A3, it means that you have to rotate the grid anti-clockwise 3 times. Similarly,
C3 means 3 times clockwise rotation. All rotations are by 90 o. Note that when you rotate
the grid, the coordinates of the player and goal do not change; only the grid cells get
rotated. Every rotation command reduces the player’s energy by n//3 units.

● The score at the start is basically the energy of the player. The initial value of the energy
is 2n units. Every time, the player consumes food, the player’s energy increases by
value times n units where each food has its own value and every time it hits an obstacle
it loses 4n units.

● Also, for every move, it loses 1 unit of energy(Energy lost for R4D3L2U1 is 4+3+2+1 =
10 units).

● If the player is at the boundary and it makes a move which can take it out of the
boundary, then the player should appear at the opposite side of the grid. For instance, if
it is at the left boundary and it moves left, so it should appear at the right side of the grid
on the same row.

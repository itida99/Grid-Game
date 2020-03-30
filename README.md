# Grid-Game
A game in python where the player has to reach the goal position, collecting all the rewards and avoiding obstacles.

The grid is of size n X n. The player gives an input n. The start and goal positions would be randomly placed on the boundary.

There are obstacles in some of the cells of the grid, and their positions would also be random.

The player can make moves like up, down, left and right and two special moves - rotate clockwise and rotate anti-clockwise. The moves are case insensitive.

A move is taken as input from the player. For instance, R4D3L2U1 means move 4 units to the right, then 3 units down, then 2 units to the left and finally 1 unit upwards. (The input need not necessarily contain all R, L, U and D. For example, R4D3 is also a valid input). The player can keep giving such inputs until it loses all its energy or reaches the goal position.

The special moves (rotate anti/clockwise) can also be given as an input. If
the input is A3, it means that the grid is rotated anti-clockwise 3 times. Similarly, C3 means 3 times clockwise rotation. All rotations are by 90 degrees. On rotation of the grid, the coordinates of the player and goal do not change; only the grid cells get rotated. Every rotation command reduces the player’s energy by n//3 units.

The score at the start is the energy of the player. The initial value of the energy is 2n units. Every time, the player consumes food, the player’s energy increases by value times n units where each food has its own value and every time it hits an obstacle it loses 4n units.

Also, for every move, it loses 1 unit of energy(Energy lost for R4D3L2U1 is 4+3+2+1 = 10 units).

If the player is at the boundary and it makes a move which can take it out of the boundary, then the player would appear at the opposite side of the grid. For instance, if it is at the left boundary and it moves left, so it would appear at the right side of the grid on the same row.

import os
import time
import random

class Grid:
    """
    Contains information about the grid
    Attributes:
        N: size of the grid
        start: original position of the player
        goal: final position of the player
        myObstacles: an array of obstacles
        myRewards: an array of rewards
    Methods:
        rotateClockwise(n): rotates the grid clockwise n times by 90°
        rotateAnticlockwise(n): rotates the grid anti-clockwise n times by 90°
        showGrid(): prints the grid on the console.
    """

    def __init__(self, N):
        self.N = N

        # sample returns distinct random numbers
        X = random.randrange(1, N + 1)
        Y = random.randrange(1, N + 1)

        # defines on which edge goal and start are placed
        key1, key2 = random.sample(range(1, 5), 2)

        if key1 == 1:
            self.start = (X, 1)
        elif key1 == 2:
            self.start = (1, X)
        elif key1 == 3:
            self.start = (X, N)
        elif key1 == 4:
            self.start = (N, X)

        # starting coordinates of the player
        p1.x, p1.y = self.start

        if key2 == 1:
            self.goal = (Y, 1)
        elif key2 == 2:
            self.goal = (1, Y)
        elif key2 == 3:
            self.goal = (Y, N)
        elif key2 == 4:
            self.goal = (N, Y)

    def intializeGame(self):
        """
        Intializing the game, assinging obstacle and rewards random coordinates
        There are a Total of approx(N) rewards and approx(2N) obstacles
        """

        # An array of Obstacles
        self.myObstacles = []
        # An array of Rewards
        self.myRewards = []

        # loop the initializes obstacles
        for i in range(self.N):

            # Generate four different random numbers in range 1 to N
            X1, Y1, X2, Y2, X3, Y3 = random.sample(range(1, self.N + 1), 6)

            # Energy of the Reward
            energy = random.randrange(1, 10)

            # Create a reward with position X1, Y1
            if (self.start != (X1, Y1) and self.goal != (X1, Y1)):
                rw = Reward(X1, Y1, energy)
                self.myRewards.append(rw)

            # create obstacle with coordinates X2, Y2
            if (self.start != (X2, Y2) and self.goal != (X2, Y2)):
                ob = Obstacle(X2, Y2)
                self.myObstacles.append(ob)

            # create obstacle with coordinates X3, Y3
            if (self.start != (X3, Y3) and self.goal != (X3, Y3)):
                ob = Obstacle(X3, Y3)
                self.myObstacles.append(ob)

    def rotateClockwise(self, n):

         # (i, j) changes to (j, N - i + 1)

        # dictionary to help revert back changes
        O = {}
        R = {}

        for i in self.Obs:
            O[i] = True

        for i in self.Rew:
            R[i] = self.Rew[i]

        t = self.goal

        for i in range(n):

            self.goal = (self.goal[1], self.N - self.goal[0] + 1)

            # contains list of iteams to delete and add
            l = []
            l2 = []
            for ob in self.Obs:
                temp = ob
                l2.append(ob)
                self.Obs[ob] = False
                temp2 = (temp[1], self.N - temp[0] + 1)
                l.append(temp2)

            for i in l:
                self.Obs[i] = True

            for i in l2:
                del self.Obs[i]

            l = []
            l2 = []
            for re in self.Rew:
                temp = re
                l.append(re)
                temp2 = (temp[1], self.N - temp[0] + 1)
                l2.append(temp2)

            for i in range(len(l2)):
                self.Rew[l2[i]] = self.Rew[l[i]]

            for i in l:
                del self.Rew[i]

        if (p1.x, p1.y) in self.Obs:
            self.Obs = O
            self.Rew = R
            self.goal = t
            return False

        p1.energy -= self.N // 3

    def rotateAnticlockwise(self, n):
        # (i, j) changes to (N - j + 1, i)

        # dictionary to help revert back changes
        O = {}
        R = {}

        for i in self.Obs:
            O[i] = True

        for i in self.Rew:
            R[i] = self.Rew[i]

        t = self.goal

        for i in range(n):

            self.goal = (self.N - self.goal[1] + 1, self.goal[0])

            # contains list of iteams to delete and add
            l = []
            la = []
            for ob in self.Obs:
                temp = ob
                l.append(ob)
                temp2 = (self.N - temp[1] + 1, temp[0])
                la.append(temp2)

            for i in la:
                self.Obs[i] = True

            for i in l:
                del self.Obs[i]

            l = []
            la = []
            for re in self.Rew:
                temp = re
                l.append(re)
                temp2 = (self.N - temp[1] + 1, temp[0])
                la.append(temp2)

            for i in range(len(la)):
                self.Rew[la[i]] = self.Rew[l[i]]

            for i in l:
                del self.Rew[i]

        if (p1.x, p1.y) in self.Obs:
            self.Obs = O
            self.Rew = R
            self.goal = t
            return False

        # Decrease energy of player
        p1.energy -= self.N // 3

    def showGrid(self):
        """
        Prints the Grid on the screen
        Obstacle is represented by '#'
        Reward is represented by a number denoting the value of the reward
        Player is represented by 'O'
        Empty cell is represented by '.'
        """

        _ = os.system('clear')

        print("\033[1;30;43mENERGY", p1.energy)
        for i in range(self.N):
            for j in range(self.N):

                key = (i + 1, j + 1)

                # if position of various variable coincide then they are printed accorfing to priority (start == goal), rewards, Obstacles
                # \033[1;30;43m is escape sequence for font color and background color
                if key == (p1.x, p1.y):
                    # Current Position of player
                    print("\033[1;30;43mO ", end='')
                elif key == self.goal:
                    # Position of Goal
                    print("\033[1;30;43m$ ", end='')
                elif key in self.Rew:
                    # Position of Reward
                    print("\033[1;33;40m" + str(self.Rew[key]), '', end='')
                elif key in self.Obs:
                    # Position of Obstacle
                    print("\033[1;33;40m# ", end='')
                else:
                    # Empty space
                    print("\033[1;33;40m. ", end='')
            # Change line
            print("\033[1;33;40m")


class Player:
    """
    Contain all the attributes and methods specific to each player
    Attributes:
        x: The x coordinate of the player
        y: The y coordinate of the player
        energy: The energy of the player
    Methods:
        makeMove(s):
            Invoked when a player makes a move, passed a argument of type string
    """

    def __init__(self, energy):
        self.energy = energy

    def printMovingGrid(self, grid, dire, values):
        """
        Displays the grid with the player moving, called by the makeMove function
        Args:
            self: A pointer to the instance of class by which printMovingGrid is invoked
            grid: An object of class Grid containing the main grid of the game
            dire: A string containing the direction of move, eg: "DULRD"
            values: Contains a integer value for every change in direction of motion
        Returns:
            1: Player Won
            0: Player Lost
        """

        # Stores the move that have been made to print 'X' in their place
        moves = {}
        moves[(self.x, self.y)] = True

        # Loops every letter in dire
        for p in range(len(dire)):

            # Contains number of moves in one direction
            num = values[p]

            if dire[p] == 'C':
                v = grid.rotateClockwise(values[p])

                if (v == False):
                    # unsuccesfull rotation
                    grid.showGrid()
                    print("Cannot Rotate Clockwise")
                    time.sleep(1)
                    continue

                if self.energy < 1:
                    return False

                grid.showGrid()
                time.sleep(0.5)

                continue

            elif dire[p] == 'A':
                v = grid.rotateAnticlockwise(values[p])

                if (v == False):
                    # unsuccesfull rotation
                    grid.showGrid()
                    print("Cannot Rotate Anti-Clockwise")
                    time.sleep(1)
                    continue

                if self.energy < 1:
                    return False

                grid.showGrid()
                time.sleep(0.5)

                continue

            while (num):

                # Clear screen and print a new grid
                _ = os.system('clear')

                # Current position of the player
                cur = self.moveplayer(dire[p])

                if (self.x, self.y) in grid.Rew:
                    self.energy += grid.Rew[(self.x, self.y)] * grid.N
                    del grid.Rew[(self.x, self.y)]
                elif (self.x, self.y) in grid.Obs:
                    self.energy -= 4 * grid.N
                if self.energy < 1:
                    return False

                print("\033[1;30;43mENERGY", self.energy)

                for i in range(grid.N):
                    for j in range(grid.N):

                        # Coordinate which has to be printed
                        key = (i + 1, j + 1)

                        # Prints X for showing the player's path
                        if key in moves and key not in grid.Obs:
                            print("\033[1;30;43mX ", end='')
                            continue

                        # if position of various variable coincide then they are printed accorfing to priority (start == goal), rewards, Obstacles
                        # \033[1;30;43m is escape sequence for font color and background color
                        if key == cur:
                            # Current postion of player
                            print("\033[1;30;43mO ", end='')
                        elif key == grid.goal:
                            # Position of Goal
                            print("\033[1;30;43m$ ", end='')
                        elif key in grid.Rew:
                            # Position of Rewards
                            print("\033[1;33;40m" +
                                  str(grid.Rew[key]), '', end='')
                        elif key in grid.Obs:
                            # Position of Obstacle
                            print("\033[1;33;40m# ", end='')
                        else:
                            # Empty space
                            print("\033[1;33;40m. ", end='')
                    # Change line
                    print("\033[1;33;40m")

                # Add the cur position to the dictionary to print it as X in the next loop
                moves[cur] = True
                # Loop Counter
                num -= 1
                # A Delay of 0.5 seconds
                time.sleep(0.5)

        # Clear Screen
        _ = os.system('clear')

        print("\033[1;33;40mENERGY", self.energy)

        # Prints the grid after the moves have been made
        for i in range(grid.N):
            for j in range(grid.N):

                key = (i + 1, j + 1)

                # if position of various variable coincide then they are printed accorfing to priority (start == goal), rewards, Obstacles
                # \033[1;30;43m is escape sequence for font color and background color
                if key == (self.x, self.y):
                    # Position of Player
                    print("\033[1;30;43mO ", end='')
                elif key == grid.goal:
                    # Position of Goal
                    print("\033[1;30;43m$ ", end='')
                elif key in grid.Rew:
                    # Position of Rewards
                    print("\033[1;33;40m" + str(grid.Rew[key]), '', end='')
                elif key in grid.Obs:
                    # Position of Obstacle
                    print("\033[1;33;40m# ", end='')
                else:
                    # Empty space
                    print("\033[1;33;40m. ", end='')
            print("\033[1;33;40m")

        time.sleep(0.5)

        if (not grid.Rew and grid.goal == (self.x, self.y)):
            return 1

    def moveplayer(self, move):
        """
        Move the player according to the input
        Args:
            self: A pointer to the instance of class by which printMovingGrid is invoked
            move: A character defining the move
        Returns:
            The position of the player after the move has been made
        """
        if move == 'R':
            self.y += 1                           # Moves player to the right by 1 Unit
            if self.y > grid.N:                   # If player passes the boundary
                self.y = 1                        # Appear on the other side

        elif move == 'L':
            self.y -= 1                           # Moves player to the left by 1 Unit
            if self.y < 1:                        # If player passes the boundary
                self.y = grid.N                   # Appear on the other side
        elif move == 'U':
            self.x -= 1                           # Moves player to the up by 1 Unit
            if self.x < 1:                        # If player passes the boundary
                self.x = grid.N                   # Appear on the other side
        else:
            self.x += 1                           # Moves player to the down by 1 Unit
            if self.x > grid.N:                   # If player passes the boundary
                self.x = 1                        # Appear on the other side

        self.energy -= 1
        return (self.x, self.y)

    def makeMove(self, s):
        """
        Moves the player according to the given move
        Args:
            self: A pointer to the instance of class by which printMovingGrid is invoked
            s: A string containing sequence of move to be performed
        Returns:
            1: Player Won
            0: Player Lost
            5: Everything went fine
        """

        # create a list with value of moves after every change in direction
        values = []

        # buffer behaves as a stack which pops when the value is letter
        buff = ''
        key = s[0]                     # store the first value as key
        dire = '' + s[0]
        s = s[1:]                      # delete the first value of the string s

        for i in s:

            if (i.isalpha()):
                # if the current value if a alphabhet flush the previous integer in the buff
                # convert buffer to int and then flush it
                values.append(int(buff))
                buff = ''

                # assign a new key
                key = i

                # enter the key in direction
                dire += i
            else:
                # else add to buffer
                buff += i

        # to store the value of the last move
        values.append(int(buff))

        v = self.printMovingGrid(grid, dire, values)
        # call print grid to display the player move
        if (v == False):
            return 0

        if (v == 1):
            return 1

        return 5


class Obstacle:
    """
    An Obstacle in the Grid
    Attributes:
        x: x coordinate of the obstacle
        y: y coordinate of the obstacle
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Reward:
    """
    A Reward in the Grid
    Attributes:
        x: x coordinate of the obstacle
        y: y coordinate of the obstacle
        value: value of energy of reward
    """

    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value


if __name__ == "__main__":

    print("\033[1;33;40mENTER SIZE OF GRID")
    N = int(input())

    p1 = Player(2 * N)
    grid = Grid(N)

    PlayerWon = False
    PlayerLost = False
    GameRunning = True

    grid.intializeGame()
    p1.x, p1.y = grid.start

    grid.Obs = {}

    # As dictionary are faster for searching
    for i in grid.myObstacles:
        t = (i.x, i.y)
        grid.Obs[t] = True

    grid.Rew = {}
    for i in grid.myRewards:
        t = (i.x, i.y)
        grid.Rew[t] = i.value

    l = []
    for i in grid.Obs:
        if i in grid.Rew:
            l.append(i)

    # Remove duplicates if any present
    for i in l:
        del grid.Obs[i]

    grid.showGrid()

    v = 0
    while(GameRunning):
        s = str(input())
        v = p1.makeMove(s.upper())
        if (v != 5):
            break

    if v == 1:
        grid.showGrid()
        print("GAME OVER", "YOU WON THE GAME")

    if v == 0:
        grid.showGrid()
        print("GAME OVER", "YOU LOST THE GAME")

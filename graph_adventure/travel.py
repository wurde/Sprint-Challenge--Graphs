#
# Dependencies
#

import random
from player import Player
from world import World
from stack import Stack
from queue import Queue
from graphs.graph1 import graph1
from graphs.graph2 import graph2
from graphs.graph3 import graph3
from graphs.graph4 import graph4
from graphs.graph5 import graph5

#
# Define a traversal algorithm
#

class Travel:
    def __init__(self, world, player):
        self.world = world
        self.player = player
        self.traversalGraph = {}
        self.path = []

    """
    Traverse the world.
    """
    def start(self):
        visitedRooms = set()
        stack = Stack()

        currentRoom = self.player.currentRoom
        visitedRooms.add(currentRoom)
        currentExits = currentRoom.getExits()
        adjacentRooms = dict([(d,'?') for d in currentExits])
        self.traversalGraph[currentRoom.id] = [(currentRoom.x, currentRoom.y), adjacentRooms]

        while len(visitedRooms) < len(self.world.rooms):
            for direction in dict.keys(self.traversalGraph[currentRoom.id][1]):
                if self.traversalGraph[currentRoom.id][1][direction] == '?':
                    nextDirection = direction
            if nextDirection is None:
                nextDirection = currentExits[random.randint(0, len(currentExits) - 1)]

            prevRoom = currentRoom
            self.player.travel(nextDirection)
            self.path.append(nextDirection)

            currentRoom = self.player.currentRoom
            currentExits = currentRoom.getExits()
            adjacentRooms = dict([(d,'?') for d in currentExits])

            if currentRoom not in visitedRooms:
                self.traversalGraph[prevRoom.id][1][nextDirection] = currentRoom.id
                adjacentRooms[self.reverseDirection(nextDirection)] = prevRoom.id
                self.traversalGraph[currentRoom.id] = [(currentRoom.x, currentRoom.y), adjacentRooms]
                visitedRooms.add(currentRoom)
            
            nextDirection = None

    """
    Return the reverse direction.
    """
    def reverseDirection(self, direction):
        if direction == "n":
            return "s"
        elif direction == "s":
            return "n"
        elif direction == "e":
            return "w"
        elif direction == "w":
            return "e"

#
# Execute commands
#

if __name__ == '__main__':
    #
    # Load world
    #

    world = World()

    #
    # Load room graph
    #

    world.loadGraph(graph1)
    world.printRooms()

    #
    # Define player
    #

    player = Player("Name", world.startingRoom)

    #
    # Travel the world using the player
    #

    travel = Travel(world, player)
    travel.start()

    # count = 0
    # while len(travel.traversalGraph) <= len(world.rooms) and len(travel.path) > 2000:
    #     count += 1
    #     travel = Travel(world, player)
    #     travel.start()
    #     print(f"Attempt: {count}, Move Count: {len(travel.path)} {len(travel.traversalGraph)} {len(world.rooms)}")

    # print(f"traversalGraph: {travel.traversalGraph}")
    print(f"Path: {travel.path}")

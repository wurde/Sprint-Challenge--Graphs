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
        visited_rooms = set()
        stack = Stack()

        currentRoom = self.player.currentRoom
        currentExits = currentRoom.getExits()
        adjacentRooms = dict([(d,'?') for d in currentExits])
        self.traversalGraph[currentRoom.id] = [(currentRoom.x, currentRoom.y), adjacentRooms]

        while len(visited_rooms) < len(self.world.rooms):
            nextDirection = currentExits[random.randint(0, len(currentExits) - 1)]
            self.player.travel(nextDirection)
            self.path.append(nextDirection)

            currentRoom = self.player.currentRoom
            currentExits = currentRoom.getExits()
            adjacentRooms = dict([(d,'?') for d in currentExits])

            if currentRoom.id not in visited_rooms:
                visited_rooms.add(currentRoom.id)
                self.traversalGraph[currentRoom.id] = [(currentRoom.x, currentRoom.y), adjacentRooms]

        print(f"self.traversalGraph {self.traversalGraph}")

        # while stack.size() > 0:
        #     nextDirection = stack.pop()
        #     self.player.travel(nextDirection)
        #     self.path.append(nextDirection)
        #     visited_rooms.append(player.currentRoom)

        #     if player.currentRoom.id not in self.traversalGraph:
        #         self.traversalGraph[self.player.currentRoom.id] = [
        #             set(player.currentRoom.getCoords()),
        #             player.currentRoom.getExits()
        #         ]

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

    world.loadGraph(graph2)
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
    print(f"Path: {travel.path}")

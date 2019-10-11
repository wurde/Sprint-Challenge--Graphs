#
# Dependencies
#

import random
from player import Player
from world import World
from stack import Stack
from queue import Queue
from graphs.graph1 import graph1

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
        self.traversalGraph[self.player.currentRoom.id] = [(currentRoom.x, currentRoom.y), adjacentRooms]

        print(f"self.world.rooms {self.world.rooms}")
        # print(f"len(self.world.rooms)")

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
    print(f"Path: {travel.path}")

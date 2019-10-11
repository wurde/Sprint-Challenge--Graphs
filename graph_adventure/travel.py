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

    # HINT player.currentRoom.id  #=> 0
    # HINT player.currentRoom.getExits() #=> ['n']
    # HINT player.currentRoom.getRoomInDirection('n') #=> <Room id=1 />
    # HINT player.travel(direction)
    def start(self):
        # TODO Traverse the world.
        visited = set()
        stack = Stack()

        for direction in self.player.currentRoom.getExits():
            stack.push(direction)

        while stack.size() > 0:
            nextDirection = stack.pop()
            self.player.travel(nextDirection)
            self.path.append(nextDirection)

            if player.currentRoom.id not in self.traversalGraph:
                self.traversalGraph[self.player.currentRoom.id] = [
                    set(player.currentRoom.getCoords()),
                    player.currentRoom.getExits()
                ]

        print(f"Path: {self.path}")

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

    # travel = Travel(world, player)
    # travel.start()
    # print(travel.path)

    for roomID in graph1:
        print(f"roomID={roomID}")

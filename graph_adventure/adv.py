#
# Dependencies
#

from player import Player
from world import World
from graphs.graph1 import graph1
from graphs.graph2 import graph2
from graphs.graph3 import graph3
from graphs.graph4 import graph4
from graphs.graph5 import graph5
from traversals.traversal1 import traversal1
from traversals.traversal2 import traversal2
from traversals.traversal3 import traversal3
from traversals.traversal4 import traversal4
from traversals.traversal5 import traversal5

#
# Load world
#

world = World()

#
# Define room graph
#

roomGraph = graph1
# roomGraph = graph2
# roomGraph = graph3
# roomGraph = graph4
# roomGraph = graph5

#
# Load room graph
#

world.loadGraph(roomGraph)

#
# Print rooms to terminal
#

world.printRooms()

#
# Define player
#

player = Player("Name", world.startingRoom)

#
# Define traversal path
#

traversalPath = traversal1
# traversalPath = traversal2
# traversalPath = traversal3
# traversalPath = traversal4
# traversalPath = traversal5

#
# Test traversal path
#

visited_rooms = set()
visited_rooms.add(player.currentRoom)
for move in traversalPath:
    player.travel(move)
    visited_rooms.add(player.currentRoom)

if len(visited_rooms) == len(roomGraph):
    print(f"TESTS PASSED: {len(traversalPath)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(roomGraph) - len(visited_rooms)} unvisited rooms")

#
# Manually walk player around
#

# player.currentRoom.printRoomDescription(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     else:
#         print("I did not understand that command.")

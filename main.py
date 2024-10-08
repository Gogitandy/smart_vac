room = Room(9)
rx = SmartVac(room)
rx.map_room()
print("map from vac")
for row in rx.perimeter_map:
    print(row)
print("----map of room----")
for row in room.layout:
    print(row)

array_map = rx.explore_room()
for row in room.layout:
    print(row)
print("vac map")
for row in array_map:
    print(row)

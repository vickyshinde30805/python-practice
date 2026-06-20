restrictions = [[1,0], [5,10]]

id1, h1 = restrictions[0]
id2, h2 = restrictions[1]

print("id1 =", id1)
print("h1 =", h1)
print("id2 =", id2)
print("h2 =", h2)

distance = id2 - id1
print("distance =", distance)

reachable_height = h1 + distance
print("reachable_height =", reachable_height)

new_height = min(h2, reachable_height)
print("new_height =", new_height)
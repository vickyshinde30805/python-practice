v=5
edge = [(0, 1), (0, 2), (1, 3), (1, 4)]
def buildgraph(v,edge):
    adjlist=[[] for i in range(v)]
    for u,v in edge:
        adjlist[u].append(v)
        adjlist[v].append(u)
    return adjlist
adjlist=buildgraph(v,edge)
for i in range (v):
    print(i,"->",adjlist[i])
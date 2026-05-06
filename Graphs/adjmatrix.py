v=5
edge = [(0, 1), (0, 2), (1, 3), (1, 4)]
def adjmatrixbuild(v,edge):
    adjmatrix=[[0 for j in range(v)] for i in range(v)]
    for u,v in edge:
        adjmatrix[u][v]=1
        adjmatrix[v][u]=1
    return adjmatrix
adjmatrix=adjmatrixbuild(v,edge)
for i in adjmatrix:
    for j in i:
        print(j,end="  ")
    print()
    
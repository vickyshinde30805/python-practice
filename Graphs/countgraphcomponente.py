
def adjlistbuild(v,edge):
    adjlist=[[]for i in range(v)]
    for u,w in edge:
        adjlist[u].append(w)
        adjlist[w].append(u)
    return adjlist


class Queue:
    def __init__(self):
        self.val=[]
    def push(self,x):
        self.val.append(x)
    def pop(self):
        if len(self.val)==0:
            return
        return self.val.pop(0)
    def front(self):
        if len(self.val)==0:
            return -1
        return self.val[0]
    def size(self):
        return len(self.val)
    
def bfs(adjlist,start,visited):
        ans=[]
        q=Queue()
        ans.append(start)
        visited[start]=True
        q.push(start)
        while q.size()>0:
            front=q.front()
            q.pop()
            for i in adjlist[front]:
                if not visited[i]:
                    ans.append(i)
                    visited[i]=True
                    q.push(i)
        return ans

v=9
edge = [(0, 1), (0, 2), (1, 2), (2, 3),(4,5),(6,7),(6,8),(7,8)]
adjlist=adjlistbuild(v,edge)
visited=[False]*v
ans=0
for i in range(v):
    if not visited[i]:
        bfs(adjlist,i,visited)
        ans+=1
print(ans)
v=5
edge = [(0, 1), (0, 2), (1, 3), (1, 4)]
def adjlistbuild(v,edge):
    adjlist=[[]for i in range(v)]
    for u,v in edge:
        adjlist[u].append(v)
        adjlist[v].append(u)
    return adjlist
adjlist=adjlistbuild(v,edge)





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
    
def bfs(adjlist):
        n=len(adjlist)
        ans=[]
        visited=[False]*n
        q=Queue()
        ans.append(0)
        visited[0]=True
        q.push(0)
        while q.size()>0:
            front=q.front()
            q.pop()
            for i in adjlist[front]:
                if not visited[i]:
                    ans.append(i)
                    visited[i]=True
                    q.push(i)
        return ans
print(bfs(adjlist))


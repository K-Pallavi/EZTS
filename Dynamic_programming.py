#Dynamic Programming using memoization
import sys
def cost(curr,visited,g,dp):
    n=len(g)
    if len(visited)==n:
        return g[curr][0]
    visit=tuple(visited)
    if (curr,visit) in dp:
        return dp[(curr,visit)]
    min_cost=sys.maxsize
    for i in range(n):
        if i not in visited:
            new_visited=visited+[i]
            new_cost=g[curr][i]+cost(i,new_visited,g,dp)
            min_cost=min(min_cost,new_cost)
    dp[(curr,visit)]=min_cost
    return min_cost
        

g=[
    [0,4,7,5,5],
    [4,0,2,3,8],
    [7,2,0,3,4],
    [5,3,3,0,6],
    [5,8,4,6,0]
]
n=len(g)
dp={}
print("minimum cost= ",cost(0,[0],g,dp))
for i in dp:
    print(i)

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

grid = []

# input grid
for i in range(rows):
    row = list(input())
    grid.append(row)

# directions (8 sides)
dir = [(-1,-1), (-1,0), (-1,1),
       (0,-1),        (0,1),
       (1,-1), (1,0), (1,1)]

# result grid
result = [[0]*cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == '*':
            result[i][j] = '*'
        else:
            count = 0
            for d in dir:
                ni = i + d[0]
                nj = j + d[1]
                
                if 0 <= ni < rows and 0 <= nj < cols:
                    if grid[ni][nj] == '*':
                        count += 1
                        
            result[i][j] = count

# print result
for row in result:
    print(*row)
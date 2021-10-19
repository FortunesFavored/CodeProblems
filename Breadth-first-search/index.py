from pprint import pprint
import time

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

path = [[0 for j in range(len(maze[i]))] for i in range(len(maze))]

def make_step(step):
    for i in range(len(path)):
        for j in range(len(path[i])):
            if path[i][j] == step:
                if i > 0 and path[i-1][j] == 0 and maze[i-1][j] == 0:
                    path[i-1][j] = step+1
                if j > 0 and path[i][j-1] == 0 and maze[i][j-1] == 0:
                    path[i][j-1] = step+1
                if i < len(path)-1 and path[i+1][j] == 0 and maze[i+1][j] == 0:
                    path[i+1][j] = step + 1
                if i < len(path[i])-1 and path[i][j+1] == 0 and maze[i][j+1] == 0:
                    path[i][j+1] = step+1
    # time.sleep(0.25)
    # pprint(path)

a,b = 1,1
c,d = 2,5
path[a][b] = 1

path_traveled = [(c,d)]

k = 1
while path[c][d] == 0:
    make_step(k)
    k += 1

print('k value', k)
print(path[c][d])
while k > 1:
    if c > 0 and path[c-1][d] == k-1:
        c,d = c-1,d
        path_traveled.append((c,d))
    if d > 0 and path[c][d-1] == k-1:
        c,d = c,d-1
        path_traveled.append((c,d))
    if c < len(path) -1 and path[c+1][d] == k-1:
        c,d = c+1,d
        path_traveled.append((c,d))
    if d < len(path[d]) -1 and path[c][d+1] == k-1:
        c,d = c,d+1
        path_traveled.append((c,d))
    k -= 1






# print('Maze')
# pprint(a)
print('Maze Break')
pprint(path)

print(path_traveled[::-1])
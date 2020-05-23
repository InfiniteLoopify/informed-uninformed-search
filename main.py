
# Umair Shahab
# 17K-3726
# Section A

import queue
from operator import itemgetter


graph = [
    ["Arad", 366, [(15, 140), (16, 118),  (19, 75), ]],
    ["Bucharest", 0, [(5, 211), (6, 90), (13, 101),  (17, 85), ]],
    ["Craiova", 160, [(3, 120), (13, 138),  (14, 146), ]],
    ["Drobeta", 242, [(2, 120), (10, 75), ]],
    ["Eforie", 161, [(7, 86), ]],
    ["Fagaras", 176, [(1, 211), (15, 99), ]],
    ["Giurgiu", 77, [(1, 90), ]],
    ["Hirsova", 151, [(4, 86), (17, 98), ]],
    ["Iasi", 226, [(11, 87), (18, 92), ]],
    ["Lugoj", 244, [(10, 70), (16, 111), ]],
    ["Mehadia", 241, [(3, 75), (9, 70), ]],
    ["Neamt", 234, [(8, 87), ]],
    ["Oradea", 380, [(15, 151), (19, 71), ]],
    ["Pitesti", 100, [(1, 101), (2, 138), (14, 97), ]],
    ["Rimnicu Vilcea", 193, [(2, 146), (13, 97), (15, 80), ]],
    ["Sibiu", 253, [(0, 140), (5, 99), (12, 151),  (14, 80), ]],
    ["Timisoara", 329, [(0, 118), (9, 111), ]],
    ["Urziceni", 80, [(1, 85), (7, 98), (18, 142), ]],
    ["Vaslui", 199, [(8, 92), (17, 142), ]],
    ["Zerind", 374, [(0, 75), (12, 71), ]],
]


def bfs(start, end):
    cost = 0
    visited = []
    prev = []
    queue = []
    queue.append(start)
    visited.append(start)
    prev.append(start)
    while queue:
        queue_start = queue.pop(0)
        for dist in graph[queue_start][2]:
            if dist[0] not in visited:
                cost += 1
                visited.append(dist[0])
                prev.append(queue_start)
                queue.append(dist[0])
                if dist[0] == end:
                    break
        else:
            continue
        break
    path = []
    last_val = visited[-1]
    while last_val != start:
        path.append(last_val)
        last_val = prev[visited.index(last_val)]
    else:
        path.append(last_val)
    path = path[::-1]
    return [cost, travel_cost(path), path]


def ucs(start, end):
    graphX = graph
    q = [(start, 0)]
    visited = []
    past = []
    seq = []
    step_cost = 0
    cost = 99999
    for list in graphX:
        list[2].sort(key=itemgetter(1))
    while q:
        cur = q.pop(0)
        for dist in graphX[cur[0]][2]:
            if dist[0] not in visited:
                step_cost += 1
                q.append((dist[0], cur[1] + dist[1]))
                seq.append(dist[0])
                for oldi, old in enumerate(past):
                    if old[-1] == cur[0]:
                        past[oldi].append(dist[0])
                        break
                    elif cur[0] in old:
                        past.append(
                            old[0: old.index(cur[0])] + [cur[0], dist[0]])
                        break
                else:
                    past.append([cur[0], dist[0]])
        visited.append(cur[0])
        if end in visited:
            cost = cur[1]
        q.sort(key=itemgetter(1))
        if cost < (min(q, key=itemgetter(1)))[1]:
            break

    total = 99999
    index = 0
    for i, old in enumerate(past):
        if end in old:
            temp = travel_cost(old[0:old.index(end)+1])
            if temp < total:
                total = temp
                index = i
                t_path = old[0:old.index(end)+1]
    return [step_cost, total, t_path]


def gbfs(start, end):
    path = [start]
    cost = 0
    while True:
        min = 99999
        minI = 0
        if path[-1] == end:
            break
        for dist in graph[path[-1]][2]:
            if graph[dist[0]][1] < min:
                min = graph[dist[0]][1]
                minI = dist[0]
        path.append(minI)
        cost += 1
    return [cost, travel_cost(path), path]


class DFS:
    visited = []
    max_cost = 0
    temp_cost = 0

    def iter(self, start, end):
        for i in range(0, 10):
            val = self.dfs(start, end, 0, i)
            if self.temp_cost > self.max_cost:
                self.max_cost = self.temp_cost
                self.temp_cost = 0
            if val == 1:
                return [self.max_cost, travel_cost(self.visited), self.visited]
            self.visited = []

    def dfs(self, start, end, cur, len):
        if cur == len:
            return 0
        cur += 1
        self.visited.append(start)
        if start == end:
            return 1

        for dist in graph[start][2]:
            if dist[0] not in self.visited:
                val = self.dfs(dist[0], end, cur, len)
                self.temp_cost += 1
                if val == 1 or val == 0:
                    return val


def travel_cost(path):
    cost = 0
    for i in range(len(path)):
        for node in graph[path[i]][2]:
            if i+1 < len(path) and path[i+1] == node[0]:
                cost += node[1]
    return cost


def print_path(path):
    str = ""
    for node in path:
        str += graph[node][0] + " -> "
    print(str[:-3:])


if __name__ == "__main__":
    start = 0
    end = 1
    dfs = DFS()
    d = dfs.iter(start, end)
    b = bfs(start, end)
    g = gbfs(start, end)
    u = ucs(start, end)

    print()
    print("DFS: ")
    print("Process Cost: \t", d[0])
    print("Path Cost: \t", d[1])
    print("Path Taken: \t", d[2])
    print_path(d[2])

    print()
    print("BFS: ")
    print("Process Cost: \t", b[0])
    print("Path Cost: \t", b[1])
    print("Path Taken: \t", b[2])
    print_path(b[2])

    print()
    print("GBFS: ")
    print("Process Cost: \t", g[0])
    print("Path Cost: \t", g[1])
    print("Path Taken: \t", g[2])
    print_path(g[2])

    print()
    print("UCS: ")
    print("Process Cost: \t", u[0])
    print("Path Cost: \t", u[1])
    print("Path Taken: \t", u[2])
    print_path(u[2])

    print()

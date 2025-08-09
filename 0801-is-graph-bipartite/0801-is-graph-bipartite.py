class Solution(object):
    def isBipartite(self, graph):
        color = [-1] * len(graph)
        queue = deque()
        for i in range(len(graph)):
            if color[i] == -1:
                color[i] = 0
                queue.append(i)
            
            while queue:
                node = queue.popleft()
                
                for ne in graph[node]:
                    if color[ne] == -1:
                        color[ne] = 1 - color[node]
                        queue.append(ne)
                    else:
                        if color[ne] == color[node]:
                            return False
        return True
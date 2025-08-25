class Solution(object):
    def findCircleNum(self, isConnected):
        visited = set()
        provinces = 0

        for ne in range(len(isConnected)):
            if ne not in visited:
                self.dfs(isConnected,ne,visited)
                provinces += 1 
            
        return provinces
    
    def dfs(self,g,source,visited):
        visited.add(source)

        for ne in range(len(g)):
            if g[source][ne] == 1 and ne not in visited:
                self.dfs(g,ne,visited)
        
        
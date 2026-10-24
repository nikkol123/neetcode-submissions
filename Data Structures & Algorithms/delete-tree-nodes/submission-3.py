import sys
sys.setrecursionlimit(20000)

class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:

        toDelete = 0
        adjlist = {i:[] for i in range(nodes)}

        for i in range(len(parent)):
            if parent[i] == -1:
                continue
            adjlist[parent[i]].append(i)

    
    
        def dfs(node):
            nonlocal toDelete

            cur_total = value[node]
            cur_nodes = 1

            for neighbour in adjlist[node]:
                chilren_total, children_count = dfs(neighbour)
                cur_total += chilren_total
                cur_nodes += children_count
            
            if cur_total == 0:
                toDelete += cur_nodes
                return (0, 0)

            return (cur_total, cur_nodes)  
        dfs(0)
        return nodes - toDelete


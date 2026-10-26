class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adjlist = {i: [] for i in range(len(edges) + 1)}

        for a, b in edges:
            adjlist[a].append(b)

        tree_diameter = 0

        def dfs(node):
            nonlocal tree_diameter
           
            max1 = 0
            max2 = 0

            for neighbour in adjlist[node]:
                length = dfs(neighbour)
                if length > max1:
                    max1 = length
                elif length > max2:
                    max2 = length
            print(node, max1, max2)
            tree_diameter = max(tree_diameter, max1 + max2)
            return 1 + max(max1, max2)
        
        dfs(0)
        return tree_diameter
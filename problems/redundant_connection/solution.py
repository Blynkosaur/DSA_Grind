class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i+1 for i in range(len(edges))]
        rank = [1 for i in range(len(edges))]
        """print(parent)"""
        for edge in edges:
            """print(edge)"""
            one = parent[edge[0]-1]
            two = parent[edge[1]-1]
            if one == two:
                return edge
            if rank[one-1]>= rank[two-1]:
                newrank = rank[one-1] + rank[two-1]
                for i in range(len(parent)):
                    if parent[i] == one or parent[i] == two:
                        parent[i] = one
                        rank[i] = newrank
            else:
                newrank = rank[one-1] + rank[two-1]
                for i in range(len(parent)):
                    if parent[i] == one or parent[i] == two:
                        parent[i] = two
                        rank[i] = newrank
            """ print(parent)
            print(rank) """
        return edges[-1]
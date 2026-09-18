class Solution:
    def findRedundantConnection(self, edges):
        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False

            parent[pb] = pa
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
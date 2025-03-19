class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(Self.parent[p])
        return self.parent[p]
    
    def union(self, p, q):
        root_p, root_q = self.find(p), self.find(q)

        if root_p != root_q:
            if self.rank[root_p] >= self.rank[root_q]:
                self.parent[root_q] = root_p
                self.rank[root_p] += self.rank[root_q]

            else:
                self.parent[root_p] = root_q
                self.rank[root_q] += self.rank[root_p]

    def connected(self, p, q):
        return self.find(p) == self.find(q)

        
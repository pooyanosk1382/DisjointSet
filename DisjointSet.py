class DisjointSet:
    parent = {}
    rank = {}

    def makeSet(self, universe):
        for i in universe:
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, k):
        if self.parent[k] != k:
            self.parent[k] = self.find(self.parent[k])
        return self.parent[k]

    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x == y:
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] += 1


def printSets(universe, ds):
    print([ds.find(i) for i in universe])


def main():
    universe = [1, 2, 3, 4, 5]
    ds = DisjointSet()
    ds.makeSet(universe)
    printSets(universe, ds)
    ds.union(4, 3)
    printSets(universe, ds)
    ds.union(2, 1)
    printSets(universe, ds)
    ds.union(1, 3)
    printSets(universe, ds)


main()
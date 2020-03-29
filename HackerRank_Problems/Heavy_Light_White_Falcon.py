# que type 1: '1 u x' assign value at x to value at node u.
# que type 2: '2 u v' print max value of the nodes on unique path btw u and v.

tree = [[0,1], [1,2]] # they are undirected edges of tree.
       #  all are u
queries = [[1,0,1],[1,1,2],[2,0,2]] # queries[0] and [1] and type 1 and other type 2.
          # 1 u x   1 u x   2 u v 
ht = dict()
for x, y in tree:
    ht[x] = 0
    ht[y] = 0
for val, u , x in queries:
    if val == 1:
        ht[u] = x
    elif val == 2:
        print(max(ht[u], ht[x]))
 
 ### incomplete 
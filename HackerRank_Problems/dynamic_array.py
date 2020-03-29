n = 2

queries = [[1,0,5],[1,1,7],[1,0,3],[2,1,0],[2,1,1]]
#########   1 x y   .............   2 x y   2 x y
lastAnswer = 0
seqLists = [[] for i in range(n)]

for query_type, x, y in queries:
    if query_type == 1:
        seq = (x^lastAnswer) % n
        seqLists[seq].append(y)
    else:
        seq = (x^lastAnswer) % n
        size = len(seqLists[seq])
        lastAnswer = seqLists[seq][y%size]
        print(lastAnswer)

def s(a,k):
    for _ in range(k):
        for j in a:
            yield j
a=(input().split())
k=int(input())
w=s(a,k)
for i in w:
    print(i,end=" ")
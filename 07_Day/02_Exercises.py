#1
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C = A.union(B)
print(C)
#2
print("///////////////////////////////////")
print(A.intersection(B))
#3
print("///////////////////////////////////")
print(A.issubset(B))
#4
print("///////////////////////////////////")
print(A.isdisjoint(B))
#5
print("///////////////////////////////////")
#No le supe TwT
#6
print("///////////////////////////////////")
print(A.symmetric_difference(B))
#7
del A
del B
print(A, B)
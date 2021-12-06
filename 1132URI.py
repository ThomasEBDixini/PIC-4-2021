x = int(input())
y = int(input())
z = 0
k = 0
if x > y:
    z = y
    w = x
else:
    z = x
    w = y

while z <= w:
    if z % 13 != 0:
        k += z
    z += 1
print(k)

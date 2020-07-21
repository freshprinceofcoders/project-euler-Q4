iterations = 0 
for x in range(999,100,-1):
    for y in range(999,100,-1):
        z = x * y
        if z > iterations:
            a = str(x*y)
            if a == a[::-1]:
                iterations = x * y 
print(iterations)                

L = input("please enter your list :")
L = L.strip('[]')
Q = [int(x.strip()) for x in L.split(',')]
T = [] 
for n in Q:
    if n not in T:
        T.append(n)
print(T)

     
string = str(input("please enter your string"))
Lowercase_Letters = [ chr(i) for i in range(ord('a'),ord('z')+1)]
Capital_Letters = [ chr(y) for y in range(ord('A'),ord('Z')+1)]
Distance = (" ")
T = 0
B = 0
F = 0
# string.count(" ")
for x in string:
    if x in Lowercase_Letters:
        T = T+1
    elif x in Capital_Letters:
        B = B+1
    elif x in Distance:
        F = F+1
print("Number of Capital letters =",B , "Number of Lowercase letters =",T ,"Number of intervals=",F )


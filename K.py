def English_letters(d):
# d = input("please enter your string:" )
     a = [chr(i) for i in range(ord('a'),ord('z')+1)]
     h =  [chr(i) for i in range(ord('A'),ord('Z')+1)]
     g = (' ')
     x = 0 
     y = 0 
     j = 0 
     for t in d : 
         if t in a :
             x = x + 1
         if t in h :
             y = y + 1
         if t in g :
             j = j +1 
     return(x,y,j)
d = input("please enter your string:" )
result = English_letters(d)
print (result)
# def larger_than_average(n):
#     n = n.strip('[]')
#     s = 0 
#     k = 0 
#     for x in n :
#         s= s+x 
#         k = k+1
#     d = []    
#     for e in n :
#         if e > s/k :
#             d = d.append(e)
#     return(d) 
# print(larger_than_average(n))

def larger_than_average(n):
    n = n.strip("[]")
    n = [int(x.strip()) for x in n.split(',')]
    # s = sum(n)
    # k = len(n)
    s = 0
    k = 0 
    for e in n :
        s = s + e 
        k = k + 1
    j = []
    for e in n :
        if e > s/k :
            j.append(e)
    return j 
user_input = input("please enter your list:")
result = larger_than_average(user_input)
print(result)





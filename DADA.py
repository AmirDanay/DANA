import ast 
user_input = (input("please enter your dictionary :"))
dictionary = ast.literal_eval(user_input)
score_max = -float('inf')
for x in dictionary.values():
    if x > score_max:
        score_max = x
name = None        
for key,val in dictionary.items():
    if val == score_max:
        name = key 
        break
# return(score_max)
print(name,score_max)


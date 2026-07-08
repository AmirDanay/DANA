# x = int(input("please enter your guess:"))

# import random
# a = range(2,100)
# b = random.choice(a)
# if x == b:
#     print("correct guess")
# else:
#     print("incorrect guess",b)

# x = int(input("please enter your guess:"))
# import random
# b = random.randint(2,100)
# if x == b :
#     print("correct guess" )
# else:
#     print("incorrect guss",b)

x = float(input("please enter your guess:"))
import random
b = random.uniform(2,100)
# b = round(b,2)
b = (f"{b:.3f}")
if x == b :
    print("correct guess" )
else:
    print("incorrect guss",b)

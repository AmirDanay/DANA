# # import math 
# # print("عملیات های موجود در ماشین حساب:","\n","sin , sqrt or pow , log , ** ")

# # while True :
# #     x1 = float(input())
# #     op = input()
# #     x2 = float(input())

# import math 
# print("عملیات های موجود در ماشین حساب:","\n","sin , sqrt or pow , log , ** ")

# while True :
#     try:
#         x1 = float(input())
#         op = input()
#         x2 = float(input())

#         if op == "sqrt" :

import math 
while True :
    #  try :
          print("please select your operator:(sqrt ,sin , log , pow )")
          op = input("operator :").strip().lower()
          if op == "sqrt" :
               x1 = float(input("enter your number:"))
               if x1>=0 :
                    result = math.sqrt(x1)
                    print(result)
               else :
                    print("the square root of negative number is undefined")
                    continue
          elif op == "sin" :
               x1 = float(input("please enter the desired angle :"))
               x2 = math.radians(x1)
               result = math.sin(x2)
               print("sin = " , round(result,4))
          elif op == "log":
               base = float(input("enter your desired base:"))
               x1 = float(input("enter your desired number :"))
               if x1 > 0 and base >0 and base != 1 :
                    result = math.log(x1,base)
                    print(result)
               else :
                    print("The number and the base must be greater than zero \n and the base must not be equal to one ")
                    continue 
          elif op == "pow":
             degree = float(input("enter the desired degree:"))
             x1 = float(input("enter the desired number"))
             result = math.pow(x1,degree) 
             print(result )
          again = input("do you want to calculate again ? (yes Or no)")
          if again == "no":
            break 
                    
                     



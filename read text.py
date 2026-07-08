# text = input("please enter your text:")
# G = text.splitlines()[ : 5]
# h = "\n".join(G)


# file1 = open("AMIR.txt",'a+')
# file1.write(h)
# file1.read()
# print(file1)
# file1.close()
# import os
# print("مسیر",os.getcwd())
Lines = []
print("please enter your text and for run pressed enter:")
while True :
    text = input()
    if text =="" :
       break
    Lines.append(text)
my_text = Lines[ : 5]    
# my_text = Lines.splitlines()[ : 5]
my_text_main = "\n".join(my_text)
F = open("E:/dana/Amir.txt","a+")
F.write(my_text_main + "\n")
F.seek(0)
C = F.read()
print("محتوای فایل:", C )
F.close()

# print("please enter your text and for run pressed enter:")
# while True :
#     text = input()
#     print(f"")
#     if Lines==" " :
#        print("")
#        break
#     Lines.append(text)
#     print(f"")
# print(f"")    
# my_text = Lines[ : 5]    
# # my_text = Lines.splitlines()[ : 5]
# print(f"")
# my_text_main = "\n".join(my_text)
# print(f"")
# F = open("Amir.txt","a+")
# F.write(my_text_main + "\n")
# F.seek(0)
# print("")
# C = F.read()
# print("محتوای فایل:", C )
# F.close()



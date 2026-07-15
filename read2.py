# lines = []
# print("enter your text:")
# while True:
#     text = input()
#     if text == text[ : 5]:
#         break
#     lines.append(text)
# lines = "\n".join(lines)
# with open("mamd.txt","+a")as f1:     # lines.seek(0)
#      f1.write(lines + "\n")
#      f1.seek(0)
#      print(f1.read())
lines = []
print("enter your text:")
while True:
     text = input()
     lines.append(text)
     if len(lines)==5:   
        break
    
L = "\n".join(lines)
with open("mamd.txt","a+")as f1:     # lines.seek(0)
     f1.write(L + "\n")
     f1.seek(0)
     print(f1.read())


    
    


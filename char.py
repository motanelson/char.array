print("\033c\033[47;31m")
print("give me a string to convert ...")
a=input()
print("give me a var name ...")
b=input().strip()
counter=0
for aa in a:
  print(b+"["+str(counter)+"]='"+aa+"';")
  counter=counter+1

print(b+"["+str(counter)+"]='"+"\\0"+"';")
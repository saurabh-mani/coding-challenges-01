'''
    Program for fibonacci series
'''
num = int(input("Enter the value for n: "))
f0 = 0
f1 = 1
i=0
print(f0)
while i<num-2:
   temp = f0
   f0 += f1
   f1 = temp
   print(f0)
   i+=1 

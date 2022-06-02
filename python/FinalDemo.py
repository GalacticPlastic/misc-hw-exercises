#Final Exam demo

#for loop is better when you know the loop will be executed a fixed number of times
for i in range(5):
    print("in for loop i=", i)

j=0
while j <5:
    print("in while loop j=", j)
    j=j+1

#while loop is better when you have a sentinal value to look for
j="d"
while j!="":
    j = input("enter a value, when you leave the value blank the loop will stop")
#Note: if you never change the value of j this will be an infinite loop          
    

#in both of the below examples the second half of the expression is "short-circuit"
#Since we know the results of the first part is doesn't matter what the second part is
          
x=4
boolVariable = x==1 and x>5
boolVariable = x>1 or x==7


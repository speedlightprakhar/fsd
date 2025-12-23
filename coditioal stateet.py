'''a,b,c=(input("enter the number"))
if(a>b and a>c ):
    print("a is greater no.")
elif(b>a and b>c):
    print("b is greater no.")
else:
    print("c is greater no.")
    y=0.1*3
    print("launc a missile ")
else:
    print("let's ave peace")'''
'''if y!=0.3:

''''''

y=0.1*3

print(y)
'''
'''loops'''
'''for loop'''
'''sum=0
for i in range(11):
    sum=sum+i



print("sum")'''
'''for i in {1:'a',2:'b',3:'4',4:'c'}:
    print(i)'''''''while loop'''
'''i=0
while(i<10):
    print(i)
    i=i+1
print("done")'''
'''string="python"
i="p"
while(i in string):
    print(i,end="")
    x=x+1'''

'''i=0
while(i<3):
    print(i)
    i=i+1
else:
    print(0)'''
'''NUM1=16
NUM2=6
while(NUM1>=NUM2):
    if(NUM1>=2):
        print("num1 is greater")
        break
    else:

        print("num2 is greater")
        break'''
N=int(input("enter the number"))
count=0 
while(N>0):
    
    N=N//10
    count=count+1
print("the number of digits in a number is",count)  
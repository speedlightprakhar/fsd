"""list1=[1,5,99,77,5]
list2=[2,5,88,77,4]
list1=list1+list2
print(list1)"""
"""print("swap element in the list")
list1=[1,5,99,77,5]
list2=[2,8,88,7,4]
list1[0],list2[0]=list2[0],list1[0]
print("after swapping")
print(list1)"""
listNum =list(map(int,input("Enter the numbers: ").split()))
averageNum= 0
sumNum=0
for i in range(len(listNum)):
    sumNum +=listNum[i]
    print(sumNum)
    print(sumNum/len(listNum))
#validity of password







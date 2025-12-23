passwowrd= input("Enter your password: ")
print("the password contain one special character one capital letter and one digit")
count=0
for i in passwowrd:
    if (i.isupper()):
        count=count+1
    if(i.isdigit()):
        count=count+1
    if(i in ['@','#','$','%','&','*']):
        count=count+1
if(count==3):
    print("valid password")
    
else:
    print("invalid password")


                                                                                          
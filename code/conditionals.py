# if elif and else ladder
age = int(input("enter age: "))
if (age>=18):
    print("yes you are eligible") #indent

elif(age<0):
    print("you are entering negative age")

elif(age==0):
    print("0 inavlid")

else :
    print("no you are not eligible")

print("thank you")
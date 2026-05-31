try:
    x = int(input("enter a number: "))
    ans = 10/x

except ZeroDivisionError:
    print(f"divide by 0 is not allowed")

except  ValueError:
    print(f"invalid input")

else: 
    print(f"ans={ans}")

finally :
    print("end of program")
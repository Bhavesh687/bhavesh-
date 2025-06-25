# vote elgibility
Birth_year= input("Enter your birth year")
age=2025-int(Birth_year)
print(age)
if age>2025:
    print("Invalid age ")
elif age>18:
    print("Elgible to vote")
elif age<18:
    print("Not eligible")
elif age>110:
    print("Dead")
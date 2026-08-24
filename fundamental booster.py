print(" Welcome to the Interactive Personal Data Collecter!")


name = input("enter your name : ")

age = int(input("enter your age :"))

height =float(input("enter your height in cm:"))

favourite_number = int(input("please enter your favourite number:"))
print("THANK YOU ! Here is the information collected")

print("Name:", name,("Type:", type(name), "Memory address:", id(name)))

print("age:",age,("Type:", type(age), "Memory address:", id(age)))

print("height:",  height,("Type:", type(height), "Memory address:", id(height)))

print("favourite_number:" , favourite_number,("Type:", type(favourite_number), "Memory address:", id(favourite_number)))


current_year = 2026
birth_year = current_year - age

print("your birth year is approximately:",  birth_year,"based on your age of:",age)

print(" THANK YOU for using personal data collecter . Good Bye! ")

age = int(input("Please enter your age?"))
factor = int(input("How many diseases/conditions do u have?"))
factor = factor*10

vulnerability = age + factor

print("Your vulnerability score is " + str(vulnerability))
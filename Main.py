age = int(input("Please enter your age?"))
factor = int(input("How many diseases/conditions do u have?"))
factor = factor*10

vul = age + factor

print("Your vulnerability score is " + str(vulnerability))

if vul > 200:
    print("sahhh, uda stay indoors")
else:
    print("you gud m8 go enjoy life!")

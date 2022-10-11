print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combine_names = (name1 + name2).lower()

t = combine_names.count("t")
r = combine_names.count("r")
u = combine_names.count("u")
e = combine_names.count("e")
first = t + r + u + e
l = combine_names.count("l")
o = combine_names.count("o")
v = combine_names.count("v")
e = combine_names.count("e")
second = l + o + v + e
result = int(str(first) + str(second))
if (result < 10) or (result > 90):
    print(f"Your love score is {result}, you go together like coke and mentos.")
elif (result >= 40) and (result <= 50):
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}")


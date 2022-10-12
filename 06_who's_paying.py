import random
test_seed =int(input("Create a seed number: "))
random.seed(test_seed)

namesAsCSV = input("Give me everbody's names, separated by a coma. ")
names = namesAsCSV.split(", ")
num_items = len(names)

random_choise = random.randint(0, num_items - 1)
print(names[random_choise] + " is going to buy the meal today!")
  

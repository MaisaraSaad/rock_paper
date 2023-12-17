import random



user = input(" enter your choice ")
pc = random.choice(['r', 'p', 's'])

print(" you played "+ user)
print(" PC played " + pc)

if user == pc:
    print("It's a tie!")
elif (user == "p"and pc == "r") or (user == "r" and pc == "s") or (user == "s" and pc == "p"):
    print("You won")
else:
    print("You lose")
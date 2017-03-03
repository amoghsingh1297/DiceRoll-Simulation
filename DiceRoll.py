#Program
#Importing random module from py library
from random import randint
output=random.randint(1,6)
quit=0
while (quit!='q'):
	print("Enter to roll\n")
	#Declaring a variable keyenter to take input
	keyenter=input()
	print("Value on dice is:\t")
	#Value generated will be random after using randint
	print(output)
	if output==(1,2,3,4,5):
		print("Enter to roll")
		quit=input()
	if output==6:
		print("Awesome! You get another chance..")
		print("\Enter to roll again")
		print(output)
		quit=input()
print("""\nThank you for playing!
		   Hope you enjoyed..""")




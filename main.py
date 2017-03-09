from random import randint
dice1 = randint(1,6)
dice2 = randint(1,6)
p1win = 0
p2win = 0



userinput = raw_input("Lets Play Dice! Grab a partner and type 'go' to start...")
if userinput == "go":
	print(dice1)
	print(dice2)

	if dice1>dice2:
		print("player1 wins the round")

	else:
		print("player2 wins the round")

	
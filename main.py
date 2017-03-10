from random import randrange

p1 = 0
p2 = 0


while p1 != 3 or p2 != 3:
	
	dice1 = randrange(1,6)
	dice2 = randrange(1,6)

	userinput = raw_input("Lets Play Dice! Grab a partner and type 'go' to start...")
	if userinput == "go":
		print(dice1)
		print(dice2)

		if dice1>dice2:
			print("player1 wins the round")
			p1 = p1 + 1

		if dice1<dice2:
			print("player2 wins the round")
			p2 = p2 + 1

		if dice1==dice2:
			print("draw")

		if p2 == 3:
			print("Player 2 Wins!!!")

		if p1 == 3:
			print("Player 1 Wins!!!")


from random import randrange

p1 = 0
p2 = 0


while p1 == p2: 
	
	dice1a = randrange(1,7)
	dice2a = randrange(1,7)
	dice1b = randrange(1,5)
	dice2b = randrange(1,5)
	dice1c = randrange(1,13)
	dice2c = randrange(1,13)
	dice1d = randrange(1,21)
	dice2d = randrange(1,21)
	
	userinput = raw_input("Lets Play Dice! Grab a partner and type 'go'")
	if(userinput == "go"):
		print("player 1 rolled {}, {}, {}, {}.".format(dice1a,dice1b,dice1c,dice1d))
		print("player 2 rolled {}, {}, {}, {}.".format(dice2a,dice2b,dice2c,dice2d))
		p1= dice1a+dice1b+dice1c+dice1d
		p2= dice2a+dice2b+dice2c+dice2d
		print(p1)
		print(p2)
		
		if(p1 == 42):
			print("Player 1 burnt out")

		if(p2 == 42):
			print("Player 2 burnt out")

		if(p1 == 4):
			print("player 1 has reached the golden number")

		if(p2 == 4):
			print("player 2 has reached the golden number")

		elif(p1 > p2):
			print("player 1 has a greater score")

		elif(p1 < p2):
			print("player 2 has a greater score")

		if(p1 == p2):
			print("its a tie")










	



	
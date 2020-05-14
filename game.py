#Guess The Number

#This is the game of the name guess the no. in which you have to guess right ans.

def main():
	import random

	guessTaken=0

	print("Hello Welcome to the game 'Guess The Number':")
	print("New User")
	print("please enter your name:")
	myName=str(input())
	#Now system will first assume a no.
	number1=random.randint(1,20)
	print(f"Well {myName},Let's Play the game!")
	print("I am going to select a number ")
	print("You have 4 chances to Guess what i have thought.If you succedd to guess thr right no then you will win or otherwise you will loose.")
	while guessTaken<4:
		print("Take a guess. What is in my mind")
		guess=int(input())


		guessTaken=guessTaken+1

		if (guess<number1):
			print(f"{myName},your guess is too low. Try again!")
		elif(guess>number1):
			print(f"{myName},your guess is too high. Try again!")
		else:
			print(f"Congratulations!!! {myName},you have a sharp mind.you have cracked it what i have guessed in just {guessTaken} guesss!")
			break

	if guess != number1:
		print(f"Nope!,{myName}you loose the game")
main()
input("Press <enter> key to quit game")
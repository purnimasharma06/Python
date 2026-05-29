import random 

a = -1
guesses = 0
n = random.randint(0, 100)

while(a != n):
    a = int(input("Enter your guess: "))

    if(a > n):
        print("Lower your guess. Try again.")
        guesses += 1

    elif(a < n):
        print("Higher your guess. Try again.")
        guesses += 1

print(f"Congratulations! You guessed the number {n} in {guesses} guesses.")
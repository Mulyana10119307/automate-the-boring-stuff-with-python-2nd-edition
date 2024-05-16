import random

secret_number = random.randint(1,20)

print('I am thinking of a number between 1 and 20.')

# Bertanya kepada player selama 6 kali
for guesses_taken in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess < secret_number:
        print('Your guess is to low')
    elif guess > secret_number:
        print('Your guess is to high')
    else:
        break

# Jika tebakannya benar
if guess == secret_number:
    print('Good job, you guessed my number '+ str(guesses_taken) +' guesses.')
else:
    print('Nope. The number i was thinking of was ' + str(secret_number) + ' .')
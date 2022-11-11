import random #this imports the random function


def guess(): #this will allow the user to guess the computers number
    rand_num = random.randint(1, 100) #generates a number between 1 and the number inputted
    guessnum = 0 #starting integer
    while guessnum != rand_num: #whilst the computer hasn't guessed the number
        guessnum = int(input(f'guess a number between 1 and 100: '))
        if guessnum > rand_num:# if the user num is greater than the target
            print("guess again, the number is small than " + str(guessnum))#tell them it is smaller than inputted number
        elif guessnum < rand_num:#if the inputted number is too small
            print("guess again, the number is bigger than " + str(guessnum))#tell them the target is bigger

    print("Congratulation, you guessed the number")


def computer_guess(x):
    low = 0
    high = 100
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess_num = random.randint(low, high)
        else:
            guess_num = low
        feedback = input(f'Is {guess_num} too high (H), too low (L) or correct (C)???').lower()
        if feedback == 'h':
            high = guess_num - 1
        elif feedback == 'l':
            low = guess_num + 1
    print(f"We guessed your number, {guess_num}, correct!!!!")

def main():
    end = False
    while end != True:
        print("For the computer to guess your number, enter 1")
        print("For you to guess the computer's number, enter 2")
        print("For the game to end, enter 3")
        game = str(input("Please Enter your option: "))
        if game == '1':
            number = int(input("please enter a number between 1-100: "))
            computer_guess(number)
        elif game == '2':
            guess()
        elif game == '3':
            print("Goodbye!")
            end = True
        else:
            print("You entered something wrong, try again")

main()

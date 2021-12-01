a=0
while a==0:
        from random import randint
        number=randint(1,50)
        guess=int(input("Guess a number between 1 and 50: "))
        if guess == number:
                print("Correct, Good Guess")
        if guess>number:
                print("Your guess is too high！")
        if guess<number:
                print("Your guess is too low！")
        while guess!=number:
                guess=int(input("Guess a number between 1 and 50: "))
                if guess > number:
                        print("Your guess is too high!")
                elif guess < number:
                        print("Your guess is too low!")
                if guess == number:
                        print("Correct, Good Guess")
                continue
        a=int(input("Enter restart code 0 to start another round or click close to exit\n"))
        continue

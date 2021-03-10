count = 0
lucky_num = 10
while count <= 4:
    guess = int(input("Guess the lucky number: "))
    if guess == lucky_num:
        print("Good guess")
        break
    else:
        print("Try again")
    count += 1
    if count == 5 and guess != lucky_num:
        print("Sorry but that was not very successful")
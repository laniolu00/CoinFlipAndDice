import random
#code by lani
while True:
    count_cf = 0
    count_dr = 0
    game = input("What Game will you play Coin Flip or Dice roll: C or D and press any other key to leave the game entirely ")
    game.upper()
    if game == "C":
        while True:
            rand = random.randint(0,1)

            print("welcome to Coin Flip by Lani")
            ans = str(input("Guess the outcome: Heads or Tails: type H or T "))

            ans.upper()
            holding = {"H":0, "T":1}
            holdinga = ["H","T"]

            result = "coin landed on {ans}".format(ans=holdinga[rand])
            while True:
                if ans not in holding:
                    ans = input("Type H or T pls: ")
                else:
                    if rand == holding[ans]:
                        print("Correct!")
                        print(result)
                        count_cf += 1
                        break
                    else:
                        ans = input("Incorrect! Unlucky :(")
                        break

            print("\nyour current score is " + str(count_cf))
            exit_str = input("play again? Yes or No. Type Y or N  ")
            exit_str.upper()
            if exit_str == "N":
                break
    if game == "D":
        while True:
            rand_d = random.randint(1,6)

            print("welcome to Dice Roll by Lani")
            ans_d = int(input("Guess the number the dice will roll on: pick between 1-6 "))

            holding_d = [1,2,3,4,5,6]
            result_d = "dice landed on {ans}".format(ans=rand_d)
            while True:
                if ans_d not in holding_d:
                    ans_d = int(input("Enter a number in the range of 1-6 "))
                else:
                    if rand_d == ans_d:
                        print("Correct!")
                        print(result_d)
                        count_dr += 1
                        break
                    else:
                        ans = input("Incorrect! Unlucky :(")
                        break

            print("\nyour current score is " + str(count_dr))
            exit_str = input("play again? Yes or No. Type Y or N  ")
            exit_str.upper()
            if exit_str == "N":
                break
    exit_str = input("Do you want to leave? Y or N: ")
    exit_str.upper()
    if exit_str == "Y":
        break




            






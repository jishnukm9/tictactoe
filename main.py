numbers=[1,2,3,4,5,6,7,8,9]
def tictactoe():
    #printing the tic tac toe board
    def print_board(positions):
        print('\n' * 100)
        li= f"   |   |   \n" \
            f" {numbers[6]} | {numbers[7]} | {numbers[8]} \n" \
            f"   |   |   \n" \
            f"--- --- ---\n" \
            f"   |   |   \n" \
            f" {numbers[3]} | {numbers[4]} | {numbers[5]} \n" \
            f"   |   |   \n" \
            f"--- --- ---\n" \
            f"   |   |   \n" \
            f" {numbers[0]} | {numbers[1]} | {numbers[2]} \n" \
            f"   |   |   "
        print(li)

    #asking players to select a position
    def position_choice_player1():
        choice = int(input("player:1 select a position 1/2/3/4/5/6/7/8/9: "))
        return choice
    def position_choice_player2():
        choice = int(input("player:2 select a position 1/2/3/4/5/6/7/8/9: "))
        return choice

    def reset_list():
        global numbers
        numbers =[1, 2, 3, 4, 5, 6, 7, 8, 9]
    def update_board(choice,player):
        global  numbers
        numbers[choice-1]=player

    #checking if player1 or player 2 won the game
    def game_winner(listt):
        if listt[0]==listt[1] and listt[1]==listt[2]:
            game_on=False
            if listt[0]=="X":
                playernumber=1
            else:
                playernumber=2
            print(f"congratulations player {playernumber} won")
            return game_on

        elif listt[3]==listt[4] and listt[4]==listt[5]:
            game_on=False
            if listt[3]=="X":
                playernumber=1
            else:
                playernumber=2
            print(f"congratulations player {playernumber} won")
            return game_on

        elif listt[6]==listt[7] and listt[7]==listt[8]:
            game_on=False
            if listt[6]=="X":
                playernumber=1
            else:
                playernumber=2
            print(f"congratulations player {playernumber} won")
            return game_on

        elif listt[0]==listt[3] and listt[3]==listt[6]:
            game_on=False
            if listt[0]=="X":
                playernumber=1
            else:
                playernumber=2
            print(f"congratulations player {playernumber} won")
            return game_on

        elif listt[1]==listt[4] and listt[4]==listt[7]:
            game_on=False
            if listt[1]=="X":
                playernumber=1
            else:
                playernumber=2
            print(f"congratulations player {playernumber} won")
            return game_on

        elif listt[2]==listt[5] and listt[5]==listt[8]:
            game_on=False
            if listt[2]=="X":
                playernumber=1
            else:
                playernumber=2
            print(f"congratulations player {playernumber} won")
            return game_on

        elif listt[0]==listt[4] and listt[4]==listt[8]:
            game_on=False
            if listt[0]=="X":
                playernumber=1
            else:
                playernumber=2
            print(f"congratulations player {playernumber} won")
            return game_on
        elif listt[2]==listt[4] and listt[4]==listt[6]:
            game_on=False
            if listt[2]=="X":
                playernumber=1
            else:
                playernumber=2
            print(f"congratulations player {playernumber} won")
            return game_on
        elif listt[0] != 1 and listt[1] != 2 and listt[2] != 3 and listt[3] != 4 and listt[4] != 5 and listt[5] != 6 and listt[6] != 7 and listt[7] != 8 and listt[8] != 9:
            game_on = False
            print("its a draw")
            return game_on
        else:
            game_on=True
            return game_on

    #playing the game
    game_on= True
    print_board(numbers)
    while game_on:
        player1=position_choice_player1()
        update_board(player1,"X")
        print_board(numbers)
        game_on = game_winner(numbers)
        if game_on ==False:
            answer1 = input("Do you wanna play again(y/n): ").lower()
            if answer1 == "y":
                reset_list()
                tictactoe()
        elif game_on==True:
            player2=position_choice_player2()
            update_board(player2,0)
            print_board(numbers)
            game_on = game_winner(numbers)
            if game_on==False:
                answer2 = input("Do you wanna play again(y/n): ").lower()
                if answer2=="y":
                    reset_list()
                    tictactoe()

tictactoe()

from random import randint
from time import sleep

for i in '\nGame: Tic-Tac-Toe\n':
    print(i,flush=True,end='')
    sleep(0.06)
sleep(1)

def tic_tac_toe():
    global moves_bot,moves_player,player_symbol,mode

    moves_bot = 0
    moves_player = 0

    board = ['-','-','-',
            '-','-','-',
            '-','-','-',]
    

    while True:
        try:
            mode = int(input('1.Very easy\n2.Advanced\n3.Impossible\n4.Leave\nChoose mode to play(1-3 or 4): '))
            if mode == 1 or mode == 2 or mode == 3:
                break
            elif mode == 4:
                exit()
            else:
                pass

        except Exception:
            pass


    while True:
        player_symbol = input('\nChoose symbol to play as(X/O): ').title()
        print()

        if player_symbol == 'X':
            bot_symbol = 'O'
            break
        elif player_symbol == 'O':
            bot_symbol = 'X'
            break
        else:
            pass


    def display_board():
        print(f"{board[0]} | {board[1]} | {board[2]}        1|2|3")
        print(f"{board[3]} | {board[4]} | {board[5]}   ->   4|5|6")
        print(f"{board[6]} | {board[7]} | {board[8]}        7|8|9\n")


    def bot_move_mode(symbol_bot:str):
        '''1.Very Easy:
        Ruch bota polega na losowaniu pola, na które postawi swój znak nie zważając na potencjalną wygraną'''

        '''2.Advanced:
        Ruch bota, który priorytezuje zajęcie środka jeśli jest wolny, 
        jeśli jest zajęty to szuka czy może wygrać,
        jeśli nie może wygrać, ale ma okazję zablokować gracza to go blokuje,
        jeśli są wolne rogi to je zajmuje,
        else losowy ruch
        (da się wygrać)'''

        '''3.Impossible:
        Ruch bota, który priorytezuje zajęcie środka jeśli jest wolny, 
        jeśli jest zajęty to szuka czy może wygrać,
        jeśli nie może wygrać, ale ma okazję zablokować gracza to go blokuje,
        jeśli widzi, że gracz chce stworzyć podwójne zagrożenie to temu zapobiega,
        jeśli są wolne rogi to je zajmuje,
        else losowy ruch
        (nie da się wygrać)'''

        global moves_bot,player_symbol,mode
        sleep(1)

        if mode == 3 or mode == 2:

            '''Zajmuje środek jeśli jest wolny'''
            if board[4] == '-':
                board[4] = symbol_bot
                moves_bot += 1
                return 1


            '''Pionowo'''
            for i in range(3): 
                
                if board[i] == symbol_bot and board[i+3] == symbol_bot and board[i+6] == '-':
                    board[i+6] = symbol_bot
                    moves_bot += 1
                    return 1
                
                elif board[i] == symbol_bot and board[i+6] == symbol_bot and board[i+3] == '-':
                    board[i+3] = symbol_bot
                    moves_bot += 1
                    return 1

                elif board[i+3] == symbol_bot and board[i+6] == symbol_bot and board[i] == '-':
                    board[i] = symbol_bot
                    moves_bot += 1
                    return 1


            '''Poziomo'''
            for i in range(0,8,3): 
                
                if board[i] == symbol_bot and board[i+1] == symbol_bot and board[i+2] == '-':
                    board[i+2] = symbol_bot
                    moves_bot += 1
                    return 1

                elif board[i] == symbol_bot and board[i+2] == symbol_bot and board[i+1] == '-':
                    board[i+1] = symbol_bot
                    moves_bot += 1
                    return 1

                elif board[i+1] == symbol_bot and board[i+2] == symbol_bot and board[i] == '-':
                    board[i] = symbol_bot
                    moves_bot += 1
                    return 1


            '''Na ukos'''
            if board[0] == symbol_bot and board[4] == symbol_bot and board[8] == '-':
                board[8] = symbol_bot
                moves_bot += 1
                return 1

            elif board[4] == symbol_bot and board[8] == symbol_bot and board[0] == '-':
                board[0] = symbol_bot
                moves_bot += 1
                return 1
                
            elif board[0] == symbol_bot and board[8] == symbol_bot and board[4] == '-':
                board[4] = symbol_bot
                moves_bot += 1
                return 1

            elif board[2] == symbol_bot and board[4] == symbol_bot and board[6] == '-':
                board[6] = symbol_bot
                moves_bot += 1
                return 1

            elif board[4] == symbol_bot and board[6] == symbol_bot and board[2] == '-':
                board[2] = symbol_bot
                moves_bot += 1
                return 1
                
            elif board[2] == symbol_bot and board[6] == symbol_bot and board[4] == '-':
                board[4] = symbol_bot
                moves_bot += 1
                return 1


            '''Blokada gracza pionowo'''
            for i in range(3): 
                
                if board[i] == player_symbol and board[i+3] == player_symbol and board[i+6] == '-':
                    board[i+6] = symbol_bot
                    moves_bot += 1
                    return 1
                
                elif board[i] == player_symbol and board[i+6] == player_symbol and board[i+3] == '-':
                    board[i+3] = symbol_bot
                    moves_bot += 1
                    return 1

                elif board[i+3] == player_symbol and board[i+6] == player_symbol and board[i] == '-':
                    board[i] = symbol_bot
                    moves_bot += 1
                    return 1


            '''Blokada gracza poziomo'''
            for i in range(0,8,3): 
                
                if board[i] == player_symbol and board[i+1] == player_symbol and board[i+2] == '-':
                    board[i+2] = symbol_bot
                    moves_bot += 1
                    return 1

                elif board[i] == player_symbol and board[i+2] == player_symbol and board[i+1] == '-':
                    board[i+1] = symbol_bot
                    moves_bot += 1
                    return 1

                elif board[i+1] == player_symbol and board[i+2] == player_symbol and board[i] == '-':
                    board[i] = symbol_bot
                    moves_bot += 1
                    return 1


            '''Blokada gracza na ukos'''
            if board[0] == player_symbol and board[4] == player_symbol and board[8] == '-':
                board[8] = symbol_bot
                moves_bot += 1
                return 1

            elif board[4] == player_symbol and board[8] == player_symbol and board[0] == '-':
                board[0] = symbol_bot
                moves_bot += 1
                return 1
                
            elif board[0] == player_symbol and board[8] == player_symbol and board[4] == '-':
                board[4] = symbol_bot
                moves_bot += 1
                return 1

            elif board[2] == player_symbol and board[4] == player_symbol and board[6] == '-':
                board[6] = symbol_bot
                moves_bot += 1
                return 1

            elif board[4] == player_symbol and board[6] == player_symbol and board[2] == '-':
                board[2] = symbol_bot
                moves_bot += 1
                return 1
                
            elif board[2] == player_symbol and board[6] == player_symbol and board[4] == '-':
                board[4] = symbol_bot
                moves_bot += 1
                return 1
        

            '''Zapobieganie podwójego zagrożenia dwóch konkretnych przypadkach, drugi przypadek jest w ostatnim elif'ie'''
            if board[7] == player_symbol and (board[0] == player_symbol or board[2] == player_symbol) and board[8] == '-':
                if board[8] == '-':
                    board[8] = bot_symbol
                    moves_bot += 1
                    return 1
            
            elif board[3] == player_symbol and (board[2] == player_symbol or board[8] == player_symbol):
                if board[6] == '-':
                    board[6] = bot_symbol
                    moves_bot += 1
                    return 1
            
            elif board[1] == player_symbol and (board[6] == player_symbol or board[8] == player_symbol):
                if board[0] == '-':
                    board[0] = bot_symbol
                    moves_bot += 1
                    return 1

            elif board[5] == player_symbol and (board[0] == player_symbol or board[6] == player_symbol):
                if board[2] == '-':
                    board[2] = bot_symbol
                    moves_bot += 1
                    return 1

            elif (board[0] == player_symbol and board[8] == player_symbol) or (board[2] == player_symbol and board[6] == player_symbol):
                if board[1] == '-':
                    board[1] = bot_symbol
                    moves_bot += 1
                    return 1


            '''Zajmuje rogi jeśli są wolne'''
            if board[0] == '-':
                board[0] = symbol_bot
                moves_bot += 1
                return 1

            elif board[2] == '-':
                board[2] = symbol_bot
                moves_bot += 1
                return 1

            elif board[6] == '-':
                board[6] = symbol_bot
                moves_bot += 1
                return 1

            elif board[8] == '-':
                board[8] = symbol_bot
                moves_bot += 1
                return 1


        '''Losowo jeżeli nie ma możliwości blokady, wygrania lub zajęcia jednego z rogów'''
        while True:
            index = randint(0,8)
            if board[index] == '-':
                board[index] = symbol_bot
                moves_bot += 1
                break


    def player_move(symbol_player:str):
        global moves_player
        while True:
            try:
                player = int(input(f'Choose number to place {symbol_player} on(1-9): '))
                print()
                
                if board[player-1] == '-':
                    board[player-1] = symbol_player
                    moves_player += 1
                    break

                else:
                    print('This board space is already taken!')
                    pass

            except Exception:
                pass


    def another():
        while True:
            again = input('Another game? (Y/N): ').title()

            if again == 'Y':
                tic_tac_toe()
            elif again == 'N':
                exit()
            else:
                pass
    

    def check_win(symbol, moves):

        if board[0] == symbol and board[1] == symbol and board[2] == symbol:
            print(f"{symbol}'s won in {moves} moves.")
            return 1
        
        elif board[3] == symbol and board[4] == symbol and board[5] == symbol:
            print(f"{symbol}'s won in {moves} moves.")
            return 1
        
        elif board[6] == symbol and board[7] == symbol and board[8] == symbol:
            print(f"{symbol}'s won in {moves} moves.")
            return 1
        
        elif board[0] == symbol and board[3] == symbol and board[6] == symbol:
            print(f"{symbol}'s won in {moves} moves.")
            return 1
        
        elif board[1] == symbol and board[4] == symbol and board[7] == symbol:
            print(f"{symbol}'s won in {moves} moves.")
            return 1
        
        elif board[2] == symbol and board[5] == symbol and board[8] == symbol:
            print(f"{symbol}'s won in {moves} moves.")
            return 1
        
        elif board[0] == symbol and board[4] == symbol and board[8] == symbol:
            print(f"{symbol}'s won in {moves} moves.")
            return 1
        
        elif board[2] == symbol and board[4] == symbol and board[6] == symbol:
            print(f"{symbol}'s won in {moves} moves.")
            return 1
        
        elif '-' not in board:
            print('Draw!')
            return 1


    game = True
    while game:
        display_board()

        if check_win(player_symbol,moves_player):
            break
        elif check_win(bot_symbol,moves_bot):
            break

        player_move(player_symbol)
        display_board()

        if check_win(player_symbol,moves_player):
            break
        elif check_win(bot_symbol,moves_bot):
            break

        bot_move_mode(bot_symbol)

    another()
tic_tac_toe()
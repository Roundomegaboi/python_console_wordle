from colorama import Fore, Back, Style

#procedure displays the board
def display_board(board: list):
    for guess in board:
        for index, color in enumerate(guess[::2]):
            print('| ',end='')
            if color == 'G':
               print(Fore.GREEN + f'{guess[index*2+1]}',end='')
            elif color == 'O':
                print(Fore.YELLOW + f'{guess[index*2+1]}',end='')
            else:
                print(Fore.RED + f'{guess[index*2+1]}',end='')
                
            print(Style.RESET_ALL,end='')
            print(' |',end='')
        print('')
    
    for i in range(6-len(board)):
        print(Style.DIM + '| x || x || x || x || x || x |')
            
word = 'zebras'

board = []
guesses = 0
while True: #game loop
    if guesses > 6:
        print('You are out of guesses! ')
        break
    
    display_board(board)
    user_word = input('Enter word: ')
    
    if len(user_word) != 6: #invalid word
        print('Invalid Word')
        continue
    
    guesses += 1
    word_layout = '' #this variable stores the output of the program based on the location of letters in the word
    for index, letter in enumerate(word): #check how many letters in user word are correct
        if user_word[index] == word[index]:
            word_layout += f'G{user_word[index]}'
        elif user_word[index] in word:
            word_layout += f'O{user_word[index]}'
        else:
            word_layout += f'R{user_word[index]}'
            
    board.append(word_layout)
        
    #check victory
    if user_word == word:
        print('You found the word, well done')
        display_board(board)
        break
    
    print('')
    
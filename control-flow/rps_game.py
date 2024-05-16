import random, sys

print('ROCK, PAPER, SCISSORS')

# menyimpan variabel menang, kalah , dan draw
wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop
        print('Enter your move: (r)ock, (p)aper (s)cissors or (q)uit')
        print('------------------------------------------------------')
        player_move = input() # menyimpan inputan player
        if player_move == 'q':
            print('are you sure want to quit? (y)/(n)') # menanyakan apakah memang ingin keluar
            input_quit = input()
            if input_quit == 'n':
                continue
            elif input_quit == 'y':
                print('Thanks for playing the game.')
                sys.exit()
        if player_move == 'r' or player_move == 'p' or player_move == 's':
            break # keluar dari looping input player
        print('Type one of r, p, s, and q.')
        
    # Menampilkan yang dipilih oleh player
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')
        
    # Menampilkan pilihan komputer
    random_number = random.randint(1,3)
    if random_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif random_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif random_number == 3:
        computer_move = 's'
        print('SCISSORS')
        
    # Menampilkan dan merekan skor win/loss/tie
    if player_move == computer_move:
        print('It\'s a tie')
        ties += 1
    elif (player_move == 'r' and computer_move == 's') or (player_move == 'p' and computer_move == 'r') or (player_move == 's' and computer_move == 'p'):
        print('You win!')
        wins += 1
    elif (computer_move == 'r' and player_move == 's') or (computer_move == 'p' and player_move == 'r') or (computer_move == 's' and player_move == 'p'):
        print('You lose!')
        losses += 1

    # Jika akumulasi point sudah lebih dari 5 maka kesimpulan game
    if (wins + losses + ties) == 5:
        if wins > losses:
            print('Congratulations. You won the game!')
        if wins < losses:
            print('Unfortunately, you lost.')
        if (ties > wins) or (ties > losses):
            print('You and the computer are equally strong')
        print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
        break

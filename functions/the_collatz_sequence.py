def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    
    print(result)
    return result
    
def main():    
    try:
        print('Enter number:')
        player_input = int(input())
        while player_input != 1:
            player_input = collatz(player_input)
    except ValueError:
        print('Kesalahan Value')
        
if __name__ == '__main__':
    main()
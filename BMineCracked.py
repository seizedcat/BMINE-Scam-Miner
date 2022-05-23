import time
import random
import urllib.request as urllib
loop = False

def connect():
    try:
        urllib.request.urlopen('http://google.com')
    finally:
        return True
        return False


print(' _________ ')
print('|  ____   |           /\\      /\\        __   __            _______ ')
print('| |    |  |          /  \\    /  \\      |__| |  \\  ___     /  ____ \\ ')
print('| |___|  _|         /    \\  /    \\      __  |   \\/   \\   /  |____\\ \\ ')
print('|  __   |_         /      \\/      \\    |  | |   ___   \\ |   _______/')
print('| |  |_   |       /    /\\    /\\    \\   |  | |  |   |  | |  |________   ')
print('| |____|  |      /    /  \\  /  \\    \\  |  | |  |   |  |  \\         |')
print('|_________|     /____/    \\/    \\____\\ |__| |__|   |__|   \\________|  ')
print('')
print('https://discord.gg/PTSPGHhKEq')
print('')
if connect():
    if loop == False:
        user = input('username: ')
        address = input('e-wallet: ')
        print('Authenticating...')
        if 'user1' in user and 'bc1' in address and len(address) == 16:
            time.sleep(3)
            print('Connecting to your e-wallet...')
            time.sleep(5)
            print('')
            print('Welcome', user)
            time.sleep(2)
            print('')
            print('mining...')
            loop = True
            time.sleep(random.randrange(900, 1800))
        else:
            time.sleep(3)
            loop = False
        if loop == False or loop == True:
            BTC = random.randrange(1, 49)
            zeros = random.randrange
            print('0.0000' + str(BTC), 'BTC', 'were mined and saved in your e-wallet')
            print('')
            print('mining...')
            print('')
            print('')
            time.sleep(random.randrange(900, 1800))
            if not loop == True:
                print("XD CRACKED")

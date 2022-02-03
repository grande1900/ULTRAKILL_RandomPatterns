from random import *


def mainLoop():
    print('PRESS CTRL+C TO QUIT')
    Intensity = int(input('Intensity 1-50 = '))
    NoJump = bool(input('No JumpPads/Stairs? [True], [False]'))
    P = ('0', 'n', 'p', 's', 'J', 'H')
    if NoJump is not True:
        P = ('0', 'n', 'p', 'H')
        NoJ = 'NoJ'
    else:
        P = ('0', 'n', 'p', 's', 'J', 'H')
        NoJ = ''
    for n in range(1024):
        seed(n)
        try:
            _ = open(
                f'C:/Program Files (x86)/Steam/steamapps/common/ULTRAKILL/Cybergrind/Patterns/Random{NoJ}X'
                + f'{Intensity}/#{n}{NoJ}x{Intensity}.cgp', 'w')
        except:
            input(f'ERROR, Patterns/Random{Noj}X Does not exist.')
            break
        _ = open(
f'C:/Program Files (x86)/Steam/steamapps/common/ULTRAKILL/Cybergrind/Patterns/Random{NoJ}X'
+ f'{Intensity}/#{n}{NoJ}x{Intensity}.cgp', 'w')
        _.write('')
        f = open(
f'C:/Program Files (x86)/Steam/steamapps/common/ULTRAKILL/Cybergrind/Patterns/Random{NoJ}X'
+ f'{Intensity}/#{n}{NoJ}x{Intensity}.cgp', 'a')
        for C in range(16):
            for R in range(16):
                f.write(f'({randrange(-Intensity, Intensity)})')
            f.write('\n')
        f.write('\n')
        for C in range(16):
            for R in range(16):
                f.write(f'{P[randrange(0, len(P))]}')
            f.write('\n')
        print(f'File #{n}{NoJ} Wrote, {str((n/1024)*100)[:4]}% Done...')
        f.close()


while True:
    mainLoop()

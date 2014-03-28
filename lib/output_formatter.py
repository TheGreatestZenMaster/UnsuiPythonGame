from colorama import init, Fore
import sys




#sys.stdout.write('%s%-7s' % (Fore.RED, 'RED'))

#sys.stdout.write('%s%-7s' % (Fore.CYAN, 'testsetadfsd'))

def print_c( inputString ):
    sys.stdout.write(inputString)


if __name__ == '__main__':
    print Fore.CYAN + 'abcd' + Fore.RED + 'asadfad'
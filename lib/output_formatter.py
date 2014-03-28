from colorama import init, Fore
import sys

init()


#sys.stdout.write('%s%-7s' % (Fore.RED, 'RED'))

#sys.stdout.write('%s%-7s' % (Fore.CYAN, 'testsetadfsd'))

def output( inputString ):
    print inputString


if __name__ == '__main__':
    print Fore.CYAN + 'abcd' + Fore.RED + 'asadfad'
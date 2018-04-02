from lib import liblist
import sys

args = sys.argv
del args[0]

def main():
    print(args)
    liblist.loadList()

if __name__ == '__main__':
    main()
else:
    print("--we are not in main process, aborting!")

from lib import liblist
import sys

def main():
    print(sys.argv)
    liblist.loadList()

if __name__ == '__main__':
    main()
else:
    print("--we are not in main process, aborting!")

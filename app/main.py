from lib import liblist
from lib import libconsole
import sys

args = sys.argv
del args[0]

def main():
    returnstr = "--Everything done!"
    command = "update"
    parsed_args = libconsole.get_args(args)
    if parsed_args["ok"]:
        command = parsed_args["command"]
        parsed_args = libconsole.get_args(args, sequence = "run")
        doInlineUpdate = parsed_args["doUpdate"]
        if command == "version" or command == "help":
            doInlineUpdate = False
        if parsed_args["ok"]:
            if command != "update_lists":
                if doInlineUpdate:
                    liblist.loadList(silent=True)
                if command == "version":
                    print("OpenPackage –– Version 0.1.0\nCopyright 2018 MagicMarvMan")
            else:
                liblist.loadList(silent=False)
    return returnstr

if __name__ == '__main__':
    print(main())
else:
    print("--we are not in main process, aborting!")

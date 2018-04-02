
def get_args(arglist = [], command = "", sequence = "initial"):
    argdict = {"ok": True}
    if sequence == "initial":
        if "--version" in arglist or "-v" in arglist or "version" in arglist:
            return {"ok": True, "command": "version"}
        else:
            if len(arglist) >= 2:
                if arglist[0] == "install" or arglist[0] == "--install" or arglist[0] == "-i":
                    return {"ok": True, "command": "install"}
                else:
                    return {"ok": False}
            else:
                return {"ok": True, "command": "update_lists"}

    elif sequence == "run":
        argdict = {"doUpdate": True, "ok": True}
        if "--noupdate" in arglist:
            argdict["doUpdate"] = False

        if command == "install":
            argdict["package"] = arglist[1]

        return argdict
    else:
        return {"ok": False}

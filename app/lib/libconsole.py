
def get_args(arglist = [], sequence = "initial"):
    argdict = {"ok": True}
    if sequence == "initial":
        if "--version" in arglist or "-v" in arglist or "version" in arglist:
            return {"ok": True, "command": "version"}
        else:
            return {"ok": True, "command": "update_lists"}
    elif sequence == "run":
        argdict = {"doUpdate": True, "ok": True}
        if "--noupdate" in arglist:
            argdict["doUpdate"] = False

        return argdict
    else:
        return {"ok": False}

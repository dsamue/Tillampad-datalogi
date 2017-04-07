def isNum(x):
    try:
        int(x)
        return True
    except (ValueError, TypeError): return False

def isLet(x):
    try:
        if x.isupper() or x.islower():
            return True
        else:
            return False
    except AttributeError: return False


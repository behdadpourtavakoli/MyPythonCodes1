from goto import with_goto
from goto import goto, label  # optional, for linter purpose

#@with_goto
def x():
    goto .end
    print("this will not print")
    label .end
    print("this will print")
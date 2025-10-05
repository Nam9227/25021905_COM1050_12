def T_row(i):
    return "###" if i == 0 else " # "

def D_row(i):
    if i == 0 or i == 4:
        return "## "
    else:
        return "# #"


for r in range(5):
    line = T_row(r) + " " + D_row(r) + " " + T_row(r) + " " + T_row(r)
    print(line)

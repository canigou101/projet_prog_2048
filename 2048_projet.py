def construction_sep(n):
    sep=""
    for i in range(n):
        sep+=("------"*n)
    return sep
def construction_grille(n):
    res=construction_sep(n)
    for i in range(n):
        res+=("|   |"*n)+construction_sep(n)
    

    

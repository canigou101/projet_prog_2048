import random

def create_grid(taille):
    grid=[]
    for i in range(taille):
        grid.append([0]*taille)
    return grid


def changerVal(grid,x,y,Nval):
    grid[x][y]=Nval
    return grid

def getinput():
    move=""
    while move not in ['z', 'q', 's', 'd']:
        move = input("Votre mouvement (Z/Q/S/D) : ").strip().lower()
        if move not in ['z', 'q', 's', 'd']:
            print("mouvement incorrect")
    return move


def recherche(grid):
    pairs = []
    size = len(grid)
    
    for i in range(size):
        for j in range(size):
            
            if i < size - 1 and grid[i][j] == grid[i + 1][j] and grid[i][j] != 0:  
                pairs.append(((i, j), (i + 1, j)))
            if j < size - 1 and grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:  
                pairs.append(((i, j), (i, j + 1)))
    return pairs



def move(grid, direction):
   
    size = len(grid)
    moved = False

    def compress_and_merge(line):
        
        non_zero = [x for x in line if x != 0]
        merged = []
        skip = False
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if i < len(non_zero) - 1 and non_zero[i] == non_zero[i + 1]:
                merged.append(non_zero[i] * 2)  
                skip = True  
            else:
                merged.append(non_zero[i])
        return merged + [0] * (size - len(merged))

    if direction == 'q':
        for i in range(size):
            original = grid[i][:]
            grid[i] = compress_and_merge(grid[i])
            if grid[i] != original:
                moved = True

    elif direction == 'd':
        for i in range(size):
            original = grid[i][:]
            grid[i] = compress_and_merge(grid[i][::-1])[::-1]
            if grid[i] != original:
                moved = True

    elif direction == 'z':
        for j in range(size):
            original = [grid[i][j] for i in range(size)]
            merged = compress_and_merge(original)
            for i in range(size):
                grid[i][j] = merged[i]
            if [grid[k][j] for k in range(size)] != original:
                moved = True

    elif direction == 's':
        for j in range(size):
            original = [grid[i][j] for i in range(size)]
            merged = compress_and_merge(original[::-1])[::-1]
            for i in range(size):
                grid[i][j] = merged[i]
            if [grid[k][j] for k in range(size)] != original:
                moved = True

    return moved


def createCase(nombre):
    if nombre==2:
        return "|   2|"
    elif nombre==4:
        return "|   4|"
    elif nombre==8:
        return "|   8|"
    elif nombre==16:
        return "|  16|"
    elif nombre==32:
        return "|  32|"
    elif nombre==64:
        return "|  64|"
    elif nombre==128:
        return "| 128|"
    elif nombre==256:
        return "| 256|"
    elif nombre==512:
        return "| 512|"
    elif nombre==1024:
        return "|1024|"
    elif nombre==2048:
        return "|2048|"
    return "|    |"

def createSep(taille):
    res=""
    for i in range(taille):
        res+=('------')
    return res

def rechercheVide(grid):
    celluleVide = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                celluleVide.append((i, j))
    return celluleVide

import random

def add_random_tile(grid):
    cellVide = rechercheVide(grid)
    if not cellVide:
        return False  
    
    i, j = random.choice(cellVide)
    grid[i][j] = 2 if random.random() < 0.9 else 4  
    return True

def definitionTaille():
    move=0
    while int(move) ==0:
        move = input("indiquez une taille de grille >0 ")
        if int(move)==0:
            print("mouvement incorrect")
    return int(move)
    

def play_game(taille):
    
    
    grid = create_grid(taille)
    
    
    add_random_tile(grid)
    add_random_tile(grid)
    
    
    while True:
        
        print(createSep(taille))
        for row in grid:
            print("".join(createCase(cell) for cell in row))
            print(createSep(taille))
        
        
        if not any(recherche(grid)) and not rechercheVide(grid):
            print("Game Over! Vous avez perdu.")
            break
        
        
        move_input = getinput()
        
       
        if move(grid, move_input):
           
            if not add_random_tile(grid):
                print("Game Over! Aucune case vide disponible.")
                break
        else:
            print("Mouvement invalide, essayez un autre.")
        
        
        if any(2048 in row for row in grid):
            print("Félicitations ! Vous avez atteint 2048 !")
            break

size=definitionTaille()
play_game(size)

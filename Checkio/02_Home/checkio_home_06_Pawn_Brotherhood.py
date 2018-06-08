"""\
    Pawn Brotherhood

    Chess is a two-player strategy game played on a checkered game board laid
    out in eight rows (called ranks and denoted with numbers 1 to 8) and eight
    columns (called files and denoted with letters a to h) of squares. Each
    square of the chessboard is identified by a unique coordinate pair — a
    letter and a number (ex, "a1", "h8", "d6"). For this mission we only need to
    concern ourselves with pawns.

    A PAWN MAY CAPTURE AN OPPONENT'S PIECE ON A SQUARE DIAGONALLY IN FRONT OF
    IT ON AN ADJACENT FILE, BY MOVING TO THAT SQUARE. FOR WHITE PAWNS THE FRONT
    SQUARES ARE SQUARES WITH GREATER ROW NUMBER THAN THE SQUARE THEY CURRENTLY
    OCCUPY.
    
    A pawn is generally a weak unit, but we have 8 of them which we can use to
    build a pawn defense wall. With this strategy, one pawn defends the others.
    
    A PAWN IS SAFE IF ANOTHER PAWN CAN CAPTURE A UNIT ON THAT SQUARE.
    
    We have several white pawns on the chess board and only white pawns.
    You should design your code to find how many pawns are safe.
    
    [Példaábra: checkio_home_06_Pawn_Brotherhood.jpg]

    You are given a set of square coordinates where we have placed white pawns. You should count how many pawns are safe.

    Input: Placed pawns coordinates as a set of strings.

    Output: The number of safe pawns as an integer.

    Example:
     safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
     safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
     safe_pawns(["a1", "a2", "a3", "a4", "h1", "h2", "h3", "h4"]) == 0

    How it is used:
     For a game AI one of the important tasks is the ability
     to estimate game state. This concept will show how you can do this on the
     simple chess figures positions.

    Precondition:
     0 < pawns ≤ 8  
"""
def safe_pawns(pawns: set) -> int:
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    rows = [1, 2, 3, 4, 5, 6, 7, 8]
    num_safe_pawns = 0
    
    for i in sorted(pawns):
        # Melyik cella van tőle egy sorral hátrébb, egy oszloppal BALRA?
        if columns.index(i[0]) - 1 in range(0, 8) and int(i[1]) - 1 in rows:
            """\
            Ide én magamtól range(0, 7)-et írtam, de az nem ment át egy teszten
            (ahol h1-től a8-ig végig voltak bábuk az átlóban, a helyes válasz '7'
             lett volna, a programom eredménye viszont '6' volt),
            és csak megérzésből írtam át range(0, 8)-ra. Beszéljünk róla, mert
            úgy tűnik, még mindig nem értem az indexálás logikáját...
            """
            safe_pos_1 = columns[columns.index(i[0]) - 1] + str(int(i[1]) - 1)
        else:
            safe_pos_1 = 'xx' # Ilyen mező nem létezik, ezért a
                              # safe_pos_1 in pawns kifejezés értéke
                              # mindig hamis lesz
        
        # Melyik cella van tőle egy sorral hátrébb, egy oszloppal JOBBRA?
        if columns.index(i[0]) + 1 in range(0, 8) and int(i[1]) - 1 in rows:
            """\
            Ide én magamtól range(0, 7)-et írtam, de az nem ment át egy teszten
            (ahol h1-től a8-ig végig voltak bábuk az átlóban, a helyes válasz '7'
             lett volna, a programom eredménye viszont '6' volt),
            és csak megérzésből írtam át range(0, 8)-ra. Beszéljünk róla, mert
            úgy tűnik, még mindig nem értem az indexálás logikáját...
            """
            safe_pos_2 = columns[columns.index(i[0]) + 1] + str(int(i[1]) - 1)
        else:
            safe_pos_2 = 'xx' # Ilyen mező nem létezik, ezért a
                              # safe_pos_2 in pawns kifejezés értéke
                              # mindig hamis lesz
        
        if safe_pos_1 in pawns or safe_pos_2 in pawns:
            num_safe_pawns += 1 # Ez num_safe_pawns++ is lehetne,
                                # de azt az IDLE nem érti...
                    
    return num_safe_pawns

print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))
print(safe_pawns(["a1", "a2", "a3", "a4", "h1", "h2", "h3", "h4"]))

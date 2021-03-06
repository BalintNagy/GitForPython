"""\
    Xs and Os Referee

    Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players
    (X and O) who take turns marking the spaces in a 3×3 grid. The player who
    succeeds in placing three respective marks in a horizontal, vertical, or
    diagonal rows (NW-SE and NE-SW) wins the game.

    But we will not be playing this game. You will be the referee for this games
    results. You are given a result of a game and you must determine if the game
    ends in a win or a draw as well as who will be the winner. Make sure to
    return "X" if the X-player wins and "O" if the O-player wins. If the game is
    a draw, return "D".

    A game's result is presented as a list of strings, where "X" and "O" are
    players' marks and "." is the empty cell.

    Input: A game result as a list of strings (unicode).

    Output: "X", "O" or "D" as a string.

    Example:

     checkio([
         "X.O",
         "XX.",
         "XOO"]) == "X"
     checkio([
         "OO.",
         "XOX",
         "XOX"]) == "O"
     checkio([
         "OOX",
         "XXO",
         "OXX"]) == "D"

    How it is used: The concepts in this task will help you when iterating data
    types. They can also be used in game algorithms, allowing you to know how to
    check results.

    Precondition:
     There is either one winner or a draw.
     len(game_result) == 3
     all(len(row) == 3 for row in game_result)
"""
from typing import List

def checkio(game_result: List[str]) -> str:
    """
    Nagyon robusztus megoldást akarok csinálni, ami bármilyen n×n-es pályán
    működik.
    Ehhez először beletöltöm az összes sort, oszlopot és átlót egy listába,
    majd végigloopolok a listán, és megnézem, van-e olyan eleme, amiben vagy
    csak X, vagy csak O van.
    """

    # az tök fasza gyakorlat,  ha úgy oldasz meg valamit hogy az kvázi ilyen nagyobb skálán is felhasználható
    # viszont akkor 4-el lehet nyerni, vagy 3-al? most fixen 3-ra vigygálsz, viszont akkor bizonyos további átlókat is meg kell nézni
    # a győzelmi feltételeket valahogy úgy lehetne megközelíteni, hogy egymáshoz viszonyítva határozzuk meg
    # lista[sorindex][oszlopindex] < ha indexálható elemekből áll a lista akkor így lehet kb egy 2D-s egy táblaként indexelni az elemeket, és egymáshoz képest relatív meghatározni, hogy mit kell vizsgálni
    # ha viszont így kezdenénk el, akkor arra is kell gondolni, hogy hogy kerülheted ki az IndexErrort
    # ezzel érdemes lenne kiegészíteni, a sor/oszlop vizsgálat az adott

    winner = 'D'
    all = []
    
    #1. sorok betöltése
    for i in game_result:
        all.append(i)

    # idáig annyi történik hogy all = game_result, mert eleve egy listát várunk a sorok stringjeival
    
    #2. oszlopok betöltése
    for i in range(0, len(game_result)):
        column = ''
        for j in game_result:
            column += j[i]
        all.append(column)
                
    #3. Balfelső-Jobbalsó átló (ULLR) betöltése
    # Jobbfelső-balalsó átló (URLL) betöltése
    ULLR = ''
    URLL = ''
    for i in range(0, len(game_result)):
        ULLR += game_result[i][i]
        URLL += game_result[i][len(game_result)-i-1]
    all.append(ULLR)
    all.append(URLL)

    #4. Eredményhirdetés
    for i in all:
       for j in ['X', 'O']:
           if i.count(j) == len(game_result): # Ez lehetne akár len(i) is, talán azzal könnyebben olvasható a kód...
               winner = j
               break
    return winner


print(checkio(["X.OX",
               "XX.X",
               "XOOX", "OOOO"]))
print(checkio(["OO.",
               "XOX",
               "XOX"]))
print(checkio(["OOX",
               "XOO",
               "OXO"]))

# kiri nagyon
# szerintem ehhez fasza lenne írni egy game loopot, és akkor van egy működő python játékod, pár feladattal kell kiagészíteni:
# // kérd be a táblaméretet egyszer
# // írj egy loopot ami
#     //minden körben kirajzolja az aktuális táblát
#     //vár két inputot a felhasználótól amik a sor és oszlopindexet adják
#     // páros körben O-val páratlanban X-el írd felül az adott elemet
#     // hívd meg rajta a megírt checkio() funkcíót amit kiegészítesz annyival, hogy ha nincs elég elem egyik 1-1 kiértékelésnél akkor nem ad vissza semmit
#     // ha van már eredmény, akkor eredményhirdetés

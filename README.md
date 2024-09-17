# Quixo-Project

The objective of this project is to write a QUIXO program that allows a human player to play QUIXO against another human player or against a computer player through a menu.

## Rules of the QUIXO game 
2 players will play with a 5x5 board, where one player uses the cross symbols and the other player uses the circle symbols. Each turn, the active player takes a cube that is
blank or bearing his own symbol from the outer ring of the grid, then adds it back to the grid by pushing it into one of the rows fromwhich it was removed. 

Thus, a few pieces of the grid change places each turn, and the cubes slowly go from blank to crosses and circles. Play continues until someone forms an horizontal, vertical or
diagonal line of five cubes bearing his symbol, with this person winning the game.

Moreover, if both players form a line at the very same time, the player who played that move loses the game.

## Skeleton of project 
Functions are implemented to play the game: 

check move(board, turn, index, push from): This function’s role is to check if a certain move is valid for a certain board. It returns a boolean value False if the move is not allowable,
and it returns True if the move is allowable. 

apply move(board, turn, index, push from): This function’s role is to apply a certain move to a game. 

check victory(board, who played): This function’s role is to check if a victory situation has been reached.

computer move(board, turn, level). This function’s role is to ask for the computer to make a move for a certain board.

EMPTY = "-"
PAWN = "PEON"
ROOK = "TORRE"
KNIGHT = "CABALLO"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = ROOK
board[7][7] = ROOK

board[0][1] = KNIGHT
board[0][-2] = KNIGHT
board[7][1] = KNIGHT
board[7][-2] = KNIGHT

board[1][:7] = [PAWN] * 8
board[6][:7] = [PAWN] * 8




for row in board:
    print(row)
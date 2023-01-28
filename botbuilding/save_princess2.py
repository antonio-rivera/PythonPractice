def moveVertical(p_loc: tuple, m_loc: list):
    p_row_idx = p_loc[0]
    m_row_idx = m_loc[0]
    moves = []
    next_move = ''
    if p_row_idx > m_row_idx:
        next_move = "DOWN"
    elif p_row_idx < m_row_idx:
        next_move = "UP"

    while next_move == "UP" and m_row_idx > p_row_idx:
        moves.append(next_move)
        m_row_idx -= 1

    while next_move == "DOWN" and m_row_idx < p_row_idx:
        moves.append(next_move)
        m_row_idx += 1

    m_loc[0] = m_row_idx  # Update original location of bot
    return moves


def moveHorizontal(p_loc: tuple, m_loc: list):
    p_col_idx = p_loc[1]
    m_col_idx = m_loc[1]
    moves = []
    next_move = ''
    if p_col_idx > m_col_idx:
        next_move = "RIGHT"
    elif p_col_idx < m_col_idx:
        next_move = "LEFT"

    while next_move == "RIGHT" and m_col_idx < p_col_idx:
        moves.append(next_move)
        m_col_idx += 1

    while next_move == "LEFT" and m_col_idx > p_col_idx:
        moves.append(next_move)
        m_col_idx -= 1

    m_loc[1] = m_col_idx  # Update original location of bot
    return moves


def nextMove(n, r, c, grid):
    p_idx = None
    # Find princess and bot location store them
    for j in range(n):
        for i in range(n):
            if grid[i][j] == 'p':
                p_idx = (i, j)
    m_idx = [r, c]
    verticals = moveVertical(p_idx, m_idx)
    horizontals = moveHorizontal(p_idx, m_idx)
    all_moves = []
    if verticals and horizontals:
        all_moves = verticals + horizontals
    else:
        all_moves = verticals or horizontals

    for m in all_moves:
        return m

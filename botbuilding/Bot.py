class Bot:
    def __init__(self, initial_loc: list, grid=None):
        if len(initial_loc) > 2:
            print(
                "Incorrect location format, should be [row_index, column_index]")
            return
        self.loc = initial_loc
        self.visited_cells = {tuple(initial_loc)}
        self.grid = grid
        self.visit_order = [tuple(initial_loc)]

    def __repr__(self) -> str:
        return f"Bot({self.loc[0]!r}, {self.loc[1]!r})"

    def __len__(self) -> int:
        return len(self.visited_cells)

    def get_location(self):
        return tuple(self.loc)

    def get_current_cell(self):
        i, j = self.loc
        if self.grid:
            return self.grid[i][j]
        else:
            print("No grid to get value from")
            return None

    def move_horizontal(self, target_idx: int) -> bool:
        current_row, current_col = self.loc
        if current_col < target_idx:
            current_col += 1
            print("RIGHT")
            self.visited_cells.add((current_row, current_col))
            self.visit_order.append((current_row, current_col))
            self.loc[1] = current_col
            return True
        elif current_col > target_idx:
            current_col -= 1
            print("LEFT")
            self.visited_cells.add((current_row, current_col))
            self.visit_order.append((current_row, current_col))
            self.loc[1] = current_col
            return True

        return False

    def move_vertical(self, target_idx: int) -> bool:
        current_row, current_col = self.loc
        if current_row < target_idx:
            current_row += 1
            print("DOWN")
            self.visited_cells.add((current_row, current_col))
            self.visit_order.append((current_row, current_col))
            self.loc[0] = current_row
            return True
        elif current_row > target_idx:
            current_row -= 1
            print("UP")
            self.visited_cells.add((current_row, current_col))
            self.visit_order.append((current_row, current_col))
            self.loc[0] = current_row
            return True

        return False

    def search_adjacent(self, target_val, loc=None) -> tuple:
        if self.grid is None:
            print("No grid to get limits")
            return None
        main_loc = loc or self.loc
        row_max, col_max = len(self.grid), len(self.grid[0])
        unvisited_adjacents = []

        adjacents = [(main_loc[0]-1, main_loc[1]), (main_loc[0], main_loc[1]+1),
                     (main_loc[0]+1, main_loc[1]), (main_loc[0], main_loc[1]-1)]
        for adj_loc in adjacents:
            if adj_loc not in self.visited_cells and (0 <= adj_loc[0] < row_max) and (0 <= adj_loc[1] < col_max):
                i, j = adj_loc
                if self.grid[i][j] == target_val:
                    return adj_loc

                unvisited_adjacents.append(adj_loc)

        if len(unvisited_adjacents) > 0:
            # Return the first looked at unvisited adjacent cell that does not contain the target_val
            return unvisited_adjacents[0]

        return unvisited_adjacents

    def backtrack(self, target_val):
        unvisited_adj = self.search_adjacent(target_val)
        while (unvisited_adj == [] and len(self.visit_order) > 0):
            self.visit_order.pop()
            i, j = self.visit_order[-1]
            self.move_vertical(i)
            self.move_horizontal(j)
            unvisited_adj = self.search_adjacent(target_val)

        if len(self.visit_order) == 0:
            return None

        return unvisited_adj

    def execute_action(self, condition: bool, action_str: str):
        if condition:
            print(action_str)


# def displayPathtoPrincess(n, grid):
#     m_idx = None
#     p_idx = None
#     # Find princess and bot location store them
#     for j in range(n):
#         for i in range(n):
#             if grid[i][j] == 'p':
#                 p_idx = (i, j)

#             if grid[i][j] == 'm':
#                 m_idx = [i, j]

#     bot_m = Bot(m_idx, grid)
#     while (bot_m.get_location()[0] != p_idx[0]):
#         bot_m.move_vertical(target_idx=p_idx[0])
#     while (bot_m.get_location()[1] != p_idx[1]):
#         bot_m.move_horizontal(target_idx=p_idx[1])

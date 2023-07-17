class QueensProblem:
    def __init__(self, n):
        self.n = n
        self.columns = []
    
    def solve(self):
        if self.place_queen(0):
            self.print_board()
        else:
            print("Решение не найдено.")
    
    def place_queen(self, row):
        if row == self.n:
            return True
        
        for col in range(self.n):
            self.columns.append(col)
            if self.is_valid(row):
                if self.place_queen(row + 1):
                    return True
            self.columns.pop()
        
        return False
    
    def is_valid(self, row):
        for i in range(row):
            if (
                self.columns[i] == self.columns[row] or
                self.columns[i] - self.columns[row] == i - row or
                self.columns[i] - self.columns[row] == row - i
            ):
                return False
        return True
    
    def print_board(self):
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if col == self.columns[row]:
                    line += "Q "
                else:
                    line += "- "
            print(line)


if __name__ == "__main__":
    problem = QueensProblem(8)
    problem.solve()
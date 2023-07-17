import random


def place_queen(columns, row, col):
    for i in range(row):
        if (
            columns[i] == col or
            columns[i] - col == i - row or
            columns[i] - col == row - i
        ):
            return False
    return True


def solve_queens():
    columns = [-1] * 8
    queens = []
    row = 0

    while row < 8:
        col = random.randint(0, 7)
        if place_queen(columns, row, col):
            columns[row] = col
            queens.append((row + 1, col + 1))
            row += 1

    return queens


def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if (
                queens[i][0] == queens[j][0] or
                queens[i][1] == queens[j][1] or
                abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1])
            ):
                return False
    return True


if __name__ == "__main__":
    random.seed()

    successful_count = 0
    attempts = 0

    while successful_count < 4 and attempts < 100:
        queens = solve_queens()

        if check_queens(queens):
            print("Успешная расстановка:")
            for queen in queens:
                print(queen[0], queen[1])
            print()
            
            successful_count += 1
        
        attempts += 1
from sys import stdin, stdout
#from typing import List
import math

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def is_valid_encoding(N, lb, cb, lt, ct, qb, db):
    # Check if the encoding is valid and can be decoded into a QR code
    ''''
    if sum(lb) != sum(cb):
        return False
    '''''
    for i in range(N):

        if lt[i] < abs(lb[i] - (N-lb[i])) or ct[i] < abs(cb[i] - (N-cb[i])):
            return False

        if(0>lb[i]>N or 0>cb[i]>N or  0>lt[i]>N-1 or 0>ct[i]>N-1 ):
            return False
        if(i<=1):
            if(0>db[i]>N):
                return False
        if(i<=3):
            if(0>qb[i]>(math.floor((N/2)+1)**(2))):
                return False

    return True
'''''
def generate_qr_codes(n, lb, cb, lt, ct, qb, db):

    grid = [[None for j in range(n)] for i in range(n)]
    solutions = []

    def backtrack(row: int, col: int, black_rows: List[int], black_cols: List[int], color_rows: List[int], color_cols: List[int], quadrants: List[int], diagonals: List[int]):

        # If we reached the last column, move to the next row
        if col == n:
            backtrack(row + 1, 0, black_rows, black_cols, color_rows, color_cols, quadrants, diagonals)
            return True
        #print(row, col)
        # If we reached the last row, we found a valid solution
        if row == n:
            solutions.append(grid)
            return True

        if black_rows[row] <= 0 and black_cols[col] <= 0 and color_rows[row] <= 0 and color_cols[col] <= 0 and quadrants[
            get_quadrant(row, col)] <= 0 and diagonals[get_diagonal(row, col)] <= 0:
            return False

        if (row == 0 or grid[row - 1][col] != 1) and (col == 0 or grid[row][col - 1] != 1):
            black_rows[row] -= 1
            black_cols[col] -= 1
            color_rows[row] -= 1
            color_cols[col] -= 1
            quadrants[get_quadrant(row, col)] -= 1
            diagonals[get_diagonal(row, col)] -= 1
            grid[row][col] = 1
            backtrack(row, col+1, black_rows, black_cols, color_rows, color_cols, quadrants, diagonals)
            black_rows[row] += 1
            black_cols[col] += 1
            color_rows[row] += 1
            color_cols[col] += 1
            quadrants[get_quadrant(row, col)] += 1
            diagonals[get_diagonal(row, col)] += 1
            grid[row][col] = 0
            backtrack(row, col + 1, black_rows, black_cols, color_rows, color_cols, quadrants, diagonals)
        return False




    def get_quadrant(row: int, col: int) -> int:
        if row <= N//2 and col > N//2:
            return 0
        elif row <= N//2 and col <= N//2:
            return 1
        elif row > N//2 and col <= N//2:
            return 2
        else:
            return 3

    def get_diagonal(row: int, col: int) -> int:
        if row == col:
            return 0
        elif row == N-col+1:
            return 1
        else:
            return -1

    backtrack(0, 0, lb.copy(), cb.copy(), lt.copy(), ct.copy(), qb.copy(), db.copy())
    return solutions
'''''

def backtrack_qr_codes(size, line, column, num_black_each_line, num_black_each_column, lt, ct, qb, db):
    matrix = [[0] * size for _ in range(size)]  # matriz de zeros do tamanho especificado
    matrix_to_print = [[0] * size for _ in range(size)]
    count_res = 0
    def check_qr_code(line, column):
        nonlocal matrix, matrix_to_print, count_res
        if (line >= size and column >= size) and not verify_matrix(line, column):
            print(line,column,size)
            print("oiiii")
            return False
        if line == size:
            if check_full_matrix():
                matrix_to_print = [row[:] for row in matrix] # deep copy matrix
                count_res += 1
                return True
            return False
        if column == size:
            check_qr_code(line + 1, 0)
            return True
        matrix[line][column] = 1
        check_qr_code(line, column + 1)
        matrix[line][column] = 0
        check_qr_code(line, column + 1)
        return False

    def check_full_matrix():
        if check_full_black_each_line() and check_full_black_each_column() and check_black_each_diagonal() and check_full_color_trans_each_line() and check_full_color_trans_each_column and check_full_black_each_quadrant():
            return True
        return False

    def verify_matrix(line, column):
        if check_black_each_line(line) and check_black_each_column(column) and check_color_trans_each_line() and check_color_trans_each_column() and check_black_each_quadrant() and check_black_each_diagonal():
            return True
        return False

    def check_black_each_line(line):
        count = 0
        for j in range(size):
            if matrix[line][j] == 1:
                count += 1
        if count > num_black_each_line[line]:
            return False
        return True

    def check_full_black_each_line():
        for i in range(size):
            count = 0
            for j in range(size):
                if matrix[i][j] == 1:
                    count += 1
            if count != num_black_each_line[i]:
                return False
        return True

    def check_black_each_column(column):
        count = 0
        for i in range(size):
            if matrix[i][column] == 1:
                count += 1
        if count > num_black_each_column[column]:
            return False
        return True

    def check_full_black_each_column():
        for j in range(size):
            count = 0
            for i in range(size):
                if matrix[i][j] == 1:
                    count += 1
            if count != num_black_each_column[j]:
                return False
        return True

    def check_color_trans_each_line():
        count = 0
        for j in range(size):
            if j + 1 <= size - 1 and ((matrix[line][j] == 1 and matrix[line][j+1] == 0) or (matrix[line][j] == 0 and matrix[line][j+1] == 1)):
                count += 1
        if count > lt[line]:
            return False
        return True

    def check_full_color_trans_each_line():
        for i in range(size):
            count = 0
            for j in range(size):
                if j + 1 <= size - 1 and ((matrix[i][j] == 1 and matrix[i][j+1] == 0) or (matrix[i][j] == 0 and matrix[i][j+1] == 1)):
                    count += 1
            if count != lt[i]:
                return False
        return True

    def check_color_trans_each_column():
        count = 0
        for i in range(size):
            if i + 1 <= size - 1 and ((matrix[i][column] == 1 and matrix[i + 1][column] == 0) or (matrix[i][column] == 0 and matrix[i+1][column] == 1)):
                count += 1
        if count > ct[column]:
            return False
        return True

    def check_full_color_trans_each_column():
        for j in range(size):
            count = 0
            for i in range(size):
                if i + 1 <= size - 1 and ((matrix[i][j] == 1 and matrix[i + 1][j] == 0) or (matrix[i][j] == 0 and matrix[i+1][j] == 1)):
                    count += 1
            if count != ct[j]:
                return False
        return True

    def get_quadrant(row: int, col: int) -> int:
        if row <= N // 2 and col > N // 2:
            return 0
        elif row <= N // 2 and col <= N // 2:
            return 1
        elif row > N // 2 and col <= N // 2:
            return 2
        else:
            return 3

    def check_full_black_each_quadrant():
        for q in range(4):
            if not check_black_each_quadrant():
                return False
        return True

    def check_black_each_quadrant():
        q = get_quadrant(line, column)
        count = 0
        for i in range(size):
            for j in range(size):
                if get_quadrant(i, j) == q and matrix[i][j] == 1:
                    count += 1
        if count > qb[q]:
            return False
        return True

    def check_black_each_diagonal():
        # check main diagonal
        count = 0
        for i in range(size):
            if matrix[i][i] == 1:
                count += 1
        if count > db[0]:
            return False

        # check secondary diagonal
        count = 0
        for i in range(size):
            if matrix[i][size - i - 1] == 1:
                count += 1
        if count > db[1]:
            return False

        return True

    check_qr_code(0, 0)
    return matrix_to_print, count_res


if __name__ == "__main__":

    try:

         
            while True: 
                N=int(readln())
                lb=list(map(int, readln().split()))
                cb=list(map(int, readln().split()))
                lt=list(map(int, readln().split()))
                ct=list(map(int, readln().split()))
                qb=list(map(int, readln().split()))
                db=list(map(int, readln().split()))

                if(N<2 or N>30 or len(lb)!=N or len(cb)!=N or len(lt)!=N or len(ct)!=N or len(qb)!=4 or len(db)!=2):
                    print("DEFECT: No QR Code generated.")
                else:

                    #print(is_valid_encoding(N, lb, cb, lt, ct, qb, db))
                    qrcodes ,n_qr_codes = backtrack_qr_codes(N,0,0, lb, cb,lt,ct,qb,db)
                    #print(len(n_qr_codes))
                    print("aquiiiii", n_qr_codes)
                    print(qrcodes)

                                     
    except :
        pass



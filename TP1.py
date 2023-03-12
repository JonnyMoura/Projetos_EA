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


def pre_processamento(matriz, size, lb, cb, qb, db):
    for i in range(size):
        if lb[i] == size or lb[i] == 0:
            for j in range(size):
                if lb[i] == size:
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 0

    for j in range(size):
        if cb[j] == size or cb[j] == 0:
            for i in range(size):
                if cb[j] == size:
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 0
'''''


def get_quadrant(row: int, col: int) -> int:
    if row <= math.floor(N / 2) and col > math.floor(N / 2):
        return 0
    elif row <= math.floor(N / 2) and col <= math.floor(N / 2):
        return 1
    elif row > math.floor(N / 2) and col <= math.floor(N / 2):
        return 2
    else:
        return 3


def get_diagonal(row: int, col: int) -> int:
    if row == col:
        return 0
    elif col == N - row + 1:
        return 1
    else:
        return -1


def pre_processamento(matriz, size, lb, cb, lt, ct, qb, db):
    for i in range(size):
        if 0 > lt[i] > size - 1 or 0 > ct[i] > size - 1 or 0 > lb[i] > size or 0 > cb[i] > size:
            return False

    for i in range(size):
        if lb[i] == size or lb[i] == 0:
            if lt[i] == 0:
                for j in range(size):
                    if ((qb[get_quadrant(i + 1, j + 1)] != 0 and lb[i] == size) or (
                            qb[get_quadrant(i + 1, j + 1)] == 0 and lb[i] != size)) and (
                            ((db[0] == size or db[1] == size) and lb[i] != 0) or (
                            (db[0] == 0 or db[1] == 0) and lb[i] != N)):
                        if lb[i] == size:
                            matriz[i][j] = 1
                        else:
                            matriz[i][j] = 0
                    else:
                        return False
            else:
                return False

    for j in range(size):
        if cb[j] == size or cb[j] == 0:
            if ct[j] == 0:
                for i in range(size):
                    if ((qb[get_quadrant(i + 1, j + 1)] != 0 and cb[j] == size) or (
                            qb[get_quadrant(i + 1, j + 1)] == 0 and cb[j] != size)) and (
                            ((db[0] == size or db[1] == size) and cb[j] != 0) or (
                            (db[0] == 0 or db[1] == 0) and cb[j] != N)):
                        if cb[j] == size:
                            matriz[i][j] = 1
                        else:
                            matriz[i][j] = 0
                    else:
                        return False
            else:
                return False

    for i in range(4):
        if 0 <= qb[i] <= (math.floor((size / 2) + 1)) ** 2:
            if qb[i] == (math.floor(size / 2)) ** 2 or qb[i] == 0:
                for k in range(size):
                    for j in range(size):
                        if (qb[i] == size):
                            if (i == 0):
                                if get_quadrant(k + 1, j + 1) == 0:
                                    matriz[k][j] = 1
                                if get_quadrant(j + 1, i + 1) == 0:
                                    matriz[j][k] = 1

                            elif (i == 1):
                                if get_quadrant(k + 1, j + 1) == 1:
                                    matriz[k][j] = 1
                                if get_quadrant(j + 1, k + 1) == 1:
                                    matriz[j][k] = 1
                            elif (i == 2):
                                if get_quadrant(k + 1, j + 1) == 2:
                                    matriz[k][j] = 1
                                if get_quadrant(j + 1, k + 1) == 2:
                                    matriz[j][k] = 1
                            elif (i == 3):
                                if get_quadrant(k + 1, j + 1) == 3:
                                    matriz[k][j] = 1
                                if get_quadrant(j + 1, k + 1) == 3:
                                    matriz[j][k] = 1
                        elif (qb[i] == 0):
                            if (i == 0):
                                if get_quadrant(k + 1, j + 1) == 0:
                                    matriz[k][j] = 0
                                if get_quadrant(j + 1, k + 1) == 0:
                                    matriz[j][k] = 0
                            elif (i == 1):
                                if get_quadrant(k + 1, j + 1) == 1:
                                    matriz[k][j] = 0
                                if get_quadrant(j, k) == 1:
                                    matriz[j][k] = 0
                            elif (i == 2):
                                if get_quadrant(k + 1, j + 1) == 2:
                                    matriz[k][j] = 0
                                if get_quadrant(j + 1, k + 1) == 2:
                                    matriz[j][k] = 0
                            elif (i == 3):
                                if get_quadrant(k + 1, j + 1) == 3:
                                    matriz[k][j] = 0
                                if get_quadrant(j + 1, k + 1) == 3:
                                    matriz[j][k] = 0
        else:
            return False

        if (db[0] == size and db[1] == size):
            for i in range(size):
                if (lb[i] == 2):
                    matriz[i][i] = 1
                    matriz[i][size - i - 1] = 1
                    for k in range(size):
                        if (matriz[i][k] != 1):
                            matriz[i][k] = 0
        else:
            for i in range(2):
                if 0 <= db[i] <= size:
                    if db[i] == size or db[i] == 0:
                        for j in range(size):
                            if (i == 0):
                                if (db[i] == size):
                                    matriz[j][j] = 1
                                    if (lb[j] == 1):
                                        for l in range(size):
                                            if (matriz[j][l] != 1):
                                                matriz[j][l] = 0
                                elif (db[i] == 0):
                                    matriz[j][j] = 0
                            elif (i == 1):
                                if (db[i] == size):
                                    matriz[size - j - 1][j] = 1
                                    if (lb[j] == 1):
                                        for l in range(size):
                                            if (matriz[j][l] != 1):
                                                matriz[j][l] = 0
                                elif (db[i] == 0):
                                    matriz[size - j - 1][j] = 0

                else:
                    return False



def backtrack_qr_codes(size, line, column, num_black_each_line, num_black_each_column, lt, ct, qb, db):
    matrix = [[-1] * size for _ in range(size)]  # matriz de zeros do tamanho especificado
    matrix_to_print = [[0] * size for _ in range(size)]
    count_res = 0
    num_black_line_diff=[0]*size
    num_black_column_diff=[0]*size
    lt_diff=[0]*size
    ct_diff=[0]*size
    qb_diff=[0]*4
    db_diff=[0]*2




    if pre_processamento(matrix, size, num_black_each_line, num_black_each_column, lt, ct, qb, db) == False:
        return matrix_to_print, count_res
    def count_matrix_(matrix):
        for i in range(size):
            for j in range(size):
                if matrix[i][j] == 1:
                    num_black_line_diff[i] += 1
                    num_black_column_diff[j] += 1
                    qb_diff[get_quadrant(i + 1, j + 1)] += 1
                    if (get_diagonal(i + 1, j + 1) != -1):
                        if j == N - i - 1 and i == j:
                            db_diff[0] += 1
                            db_diff[1] += 1
                        else:
                            db_diff[get_diagonal(i + 1, j + 1)] += 1


    count_matrix_(matrix)

    def check_qr_code(line, column,num_black_line_diff,num_black_column_diff,lt_diff,ct_diff,qb_diff,db_diff):
        nonlocal matrix, matrix_to_print, count_res
        #print(matrix)
        if line == size:
            for f in range(size):
                count = 0
                for i in range(size):
                    if i + 1 <= size - 1 and ((matrix[i][f] == 1 and matrix[i + 1][f] == 0) or (
                            matrix[i][f] == 0 and matrix[i + 1][f] == 1)):
                        count += 1
                if count != ct[f]:
                    return False

            if num_black_line_diff == num_black_each_line and num_black_column_diff == num_black_each_column and qb_diff == qb and db_diff == db:
                matrix_to_print =[row[:] for row in matrix] # deep copy matrix
                #print(matrix)
                count_res += 1
                return True
            #print(num_black_line_diff)
            #print(num_black_column_diff)
            #print(qb_diff)
            #print(db_diff)
            #print_qr_code(matrix)
            return False

        if column < size:
            count = 0
            for i in range(size):
                if i + 1 <= size - 1 and ((matrix[i][column] == 1 and matrix[i + 1][column] == 0) or (
                        matrix[i][column] == 0 and matrix[i + 1][column] == 1)):
                    count += 1
            if count > ct[column]:
                return False

        if (line < size and num_black_line_diff[line] > num_black_each_line[line]) or (column < size and
                num_black_column_diff[column] > num_black_each_column[column]) or (
                qb_diff[get_quadrant(line+1, column+1)] > qb[get_quadrant(line+1, column+1)]) or (get_diagonal(line+1,column+1)!= -1 and
                db_diff[get_diagonal(line+1, column+1)] > db[get_diagonal(line+1, column+1)]):
            #print(line < size and num_black_line_diff[line] > num_black_each_line[line],column < size and num_black_column_diff[column] > num_black_each_column[column])
            #print(qb_diff[get_quadrant(line+1, column+1)] > qb[get_quadrant(line+1, column+1)],get_diagonal(line+1,column+1)!= -1 and
                #db_diff[get_diagonal(line+1, column+1)] > db[get_diagonal(line+1, column+1)])

            #print(num_black_line_diff)
            #print(matrix)
            return False

        if column == size:
            count = 0
            for j in range(size):
                if j + 1 <= size - 1 and ((matrix[line][j] == 1 and matrix[line][j + 1] == 0) or (
                        matrix[line][j] == 0 and matrix[line][j + 1] == 1)):
                    count += 1
            if count != lt[line]:
                return False
            check_qr_code(line + 1, 0,num_black_line_diff,num_black_column_diff,lt_diff,ct_diff,qb_diff,db_diff)
            return True

        if matrix[line][column] != -1:
            check_qr_code(line, column + 1, num_black_line_diff, num_black_column_diff, lt_diff, ct_diff, qb_diff, db_diff)
            return False

        num_black_line_diff[line] += 1
        num_black_column_diff[column] += 1
        qb_diff[get_quadrant(line+1, column+1)] += 1
        if(get_diagonal(line+1,column+1)!=-1):
            if column == N-line-1 and line == column:
                db_diff[0] +=1
                db_diff[1] +=1
            else:
                db_diff[get_diagonal(line+1, column+1)] += 1

        matrix[line][column] = 1
        check_qr_code(line, column + 1,num_black_line_diff,num_black_column_diff,lt_diff,ct_diff,qb_diff,db_diff)
        matrix[line][column] = -1
        num_black_line_diff[line] -= 1
        num_black_column_diff[column] -= 1
        qb_diff[get_quadrant(line+1, column+1)] -= 1
        if(get_diagonal(line+1, column+1)!=-1):
            if column == N-line-1 and line == column:
                db_diff[0] -= 1
                db_diff[1] -= 1
            else:
                db_diff[get_diagonal(line+1, column+1)] -= 1

        matrix[line][column] = 0
        check_qr_code(line, column + 1,num_black_line_diff,num_black_column_diff,lt_diff,ct_diff,qb_diff,db_diff)
        matrix[line][column] = -1
        return False




    def check_full_matrix():
        if check_full_black_each_line() and check_full_black_each_column() and check_black_each_diagonal() and check_full_color_trans_each_line() and check_full_color_trans_each_column() and check_full_black_each_quadrant():
            return True
        return False


    def check_full_black_each_line():
        for i in range(size):
            count = 0
            for j in range(size):
                if matrix[i][j] == 1:
                    count += 1
            if count != num_black_each_line[i]:
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

    def check_color_trans_each_line(row):
        count = 0
        for j in range(size):
            if j + 1 <= size - 1 and ((matrix[row][j] == 1 and matrix[row][j+1] == 0) or (matrix[row][j] == 0 and matrix[row][j+1] == 1)):
                count += 1
        if count > lt[row]:
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

    def check_color_trans_each_column(col):
        count = 0
        for i in range(size):
            if i + 1 <= size - 1 and ((matrix[i][col] == 1 and matrix[i + 1][col] == 0) or (matrix[i][col] == 0 and matrix[i+1][col] == 1)):
                count += 1
        if count > ct[col]:
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


    def check_full_black_each_quadrant():
        for q in range(4):
            if not check_black_each_quadrant(q):
                return False
        return True

    def check_black_each_quadrant(q):
        #q = get_quadrant(line+1, column+1)
        count = 0
        for i in range(size):
            for j in range(size):
                if get_quadrant(i+1, j+1) == q and matrix[i][j] == 1:
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


    check_qr_code(0, 0,num_black_line_diff,num_black_column_diff,lt_diff,ct_diff,qb_diff,db_diff)
    return matrix_to_print, count_res

def print_qr_code(matrix):
    # define os caracteres de canto, borda e espaço vazio
    corner = "+"
    border = "|"
    empty = " "

    # define o tamanho da matriz
    rows = len(matrix)
    cols = len(matrix[0])

    # cria a linha superior da matriz
    top_row = corner + "-" * cols + corner

    # imprime a linha superior da matriz
    print(top_row)

    # itera sobre as linhas da matriz e as imprime
    for i in range(rows):
        row_string = border

        for j in range(cols):
            if matrix[i][j] == 1:
                row_string += "#"
            else:
                row_string += empty

        row_string += border
        print(row_string)

    # cria a linha inferior da matriz
    bottom_row = corner + "-" * cols + corner

    # imprime a linha inferior da matriz
    print(bottom_row)



if __name__ == "__main__":

    try:

            num = int(readln())
            for _ in range(num):
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
                    qrcode ,n_qr_codes = backtrack_qr_codes(N,0,0, lb, cb,lt,ct,qb,db)
                    if n_qr_codes == 1:
                        print("VALID: 1 QR Code generated!")
                        print_qr_code(qrcode)
                    elif n_qr_codes > 1:
                        print(f"INVALID: {n_qr_codes} QR Codes generated!")
                    elif n_qr_codes == 0:
                        print("DEFECT: No QR Code generated!")



                                     
    except :
        pass



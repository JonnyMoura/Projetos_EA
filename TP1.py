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
    # Verifica se o número de células pretas em cada linha e coluna é válido
    for j in range(N):
        if lb[j] > N or cb[j] > N or lb[j] + cb[j] > 2 * N:
            return False

    # Verifica se o número de transições de cor em cada linha e coluna é válido
    for j in range(N):
        if lt[j] > N - 1 or ct[j] > N - 1:
            return False

    # Verifica se o número de células pretas em cada quadrante e diagonal é válido
    q_sum = [qb[0] + qb[1], qb[1] + qb[2], qb[2] + qb[3], qb[3] + qb[0]]
    if any(q_sum[i] > N * (N - 1) / 4 or q_sum[i] + db[i % 2] > N * (N + 1) / 2 for i in range(4)):
        return False

    # Verifica se o número total de células pretas é válido
    total_blacks = sum(lb)
    if total_blacks != N * (N - 1) / 2:
        return False

    # Verifica se as restrições de adjacência são satisfeitas
    for j in range(N - 1):
        if lb[j] + lb[j + 1] + cb[j] + cb[j + 1] == 0 or lb[j] + lb[j + 1] + cb[j] + cb[j + 1] == 4:
           return False

    return True

def get_quadrant(N,row: int, col: int) -> int:
    if row <= math.floor(N / 2) and col > math.floor(N / 2):
        return 0
    elif row <= math.floor(N / 2) and col <= math.floor(N / 2):
        return 1
    elif row > math.floor(N / 2) and col <= math.floor(N / 2):
        return 2
    else:
        return 3


def get_diagonal(N,row: int, col: int) -> int:
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
                    if ((((db[0] == size or db[1] == size) and lb[i] != 0) or (
                        (db[0] == 0 or db[1] == 0) and lb[i] != N)) or (lb[i] == size or lb[i]==0)):
                        
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
                    if ((((db[0] == size or db[1] == size) and cb[j] != 0) or (
                           (db[0] == 0 or db[1] == 0) and cb[j] != N)) or (cb[j] == size or cb[j]==0)):
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
            if qb[i] == (math.floor(size / 2)+1) ** 2 or qb[i] == 0:
                for k in range(size):
                    for j in range(size):
                        if (qb[i] == size):
                            if (i == 0):
                                if get_quadrant(size,k + 1, j + 1) == 0:
                                    matriz[k][j] = 1
                                if get_quadrant(size,j + 1, i + 1) == 0:
                                    matriz[j][k] = 1

                            elif (i == 1):
                                if get_quadrant(size,k + 1, j + 1) == 1:
                                    matriz[k][j] = 1
                                if get_quadrant(size,j + 1, k + 1) == 1:
                                    matriz[j][k] = 1
                            elif (i == 2):
                                if get_quadrant(size,k + 1, j + 1) == 2:
                                    matriz[k][j] = 1
                                if get_quadrant(size,j + 1, k + 1) == 2:
                                    matriz[j][k] = 1
                            elif (i == 3):
                                if get_quadrant(size,k + 1, j + 1) == 3:
                                    matriz[k][j] = 1
                                if get_quadrant(size,j + 1, k + 1) == 3:
                                    matriz[j][k] = 1
                        elif (qb[i] == 0):
                            if (i == 0):
                                if get_quadrant(size,k + 1, j + 1) == 0:
                                    matriz[k][j] = 0
                                if get_quadrant(size,j + 1, k + 1) == 0:
                                    matriz[j][k] = 0
                            elif (i == 1):
                                if get_quadrant(size,k + 1, j + 1) == 1:
                                    matriz[k][j] = 0
                                if get_quadrant(size,j+1, k+1) == 1:
                                    matriz[j][k] = 0
                            elif (i == 2):
                                if get_quadrant(size,k + 1, j + 1) == 2:
                                    matriz[k][j] = 0
                                if get_quadrant(size,j + 1, k + 1) == 2:
                                    matriz[j][k] = 0
                            elif (i == 3):
                                if get_quadrant(size,k + 1, j + 1) == 3:
                                    matriz[k][j] = 0
                                if get_quadrant(size,j + 1, k + 1) == 3:
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

    if lb[size-1] == 0:
        count = 1
        c = size-2
        while lb[c] == 0:
            count +=1
            c -=1
        for f in range(size):
            if cb[f] == size - count:
                for k in range(size-count):
                    matriz[k][f] = 1
    elif lb[size-1] == size:
        count = 1
        c = size-2
        while lb[c] == size:
            count +=1
            c -=1
        for f in range(size):
            if cb[f] == size - count:
                for k in range(size-count):
                    matriz[k][f] =0
    
    ''' elif lb[0] ==0:
        count = 1
        c = 1
        while lb[c] == 0:
            count +=1
            c +=1
        for f in range(size):
            if cb[f] == size-count:
                for k in range(count,size):
                    matriz[k][f] =1
    elif lb[0] ==size:
        count = 1
        c = 1
        while lb[c] == 1:
            count +=1
            c +=1
        for f in range(size):
            if cb[f] == size-count:
                for k in range(count,size):
                    matriz[k][f] =1
    
    if cb[size-1] == 0:
        count = 1
        c = size-2
        while cb[c] == 0:
            count +=1
            c -=1
        for f in range(size):
            if lb[f] == size - count:
                for k in range(size-count):
                    matriz[f][k] = 1
    elif cb[size-1] == size:
        count = 1
        c = size-2
        while cb[c] == 1:
            count +=1
            c -=1
        for f in range(size):
            if lb[f] == size - count:
                for k in range(size-count):
                    matriz[f][k] = 0
    elif cb[0] ==0:
        count = 1
        c = 1
        while cb[c] == 0:
            count +=1
            c +=1
        for f in range(size):
            if lb[f] == size-count:
                for k in range(count,size):
                    matriz[f][k] =1
    
    elif cb[0] ==size:
        count = 1
        c = 1
        while cb[c] == 1:
            count +=1
            c +=1
        for f in range(size):
            if lb[f] == size-count:
                for k in range(count,size):
                    matriz[f][k] =0'''

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
        #print("fhfh")
    def count_matrix_(matrix):
        for i in range(size):
            for j in range(size):
                if matrix[i][j] == 1:
                    num_black_line_diff[i] += 1
                    num_black_column_diff[j] += 1
                    qb_diff[get_quadrant(size,i + 1, j + 1)] += 1
                    if (get_diagonal(size,i + 1, j + 1) != -1):
                        if j == N - i - 1 and i == j:
                            db_diff[0] += 1
                            db_diff[1] += 1
                        else:
                            db_diff[get_diagonal(size,i + 1, j + 1)] += 1


    count_matrix_(matrix)
    #print(matrix)

    def check_qr_code(line, column,num_black_line_diff,num_black_column_diff,lt_diff,ct_diff,qb_diff,db_diff):
        nonlocal matrix, matrix_to_print, count_res
        #print(matrix)
        if line < size and lt[line] == 0:
            check_qr_code(line + 1, 0, num_black_line_diff, num_black_column_diff, lt_diff, ct_diff, qb_diff, db_diff)
            return True

        if line == size:
            ''''
            print_qr_code(matrix)
            print(num_black_line_diff)
            print(num_black_column_diff)
            print(qb_diff)
            print(db_diff)
            '''
            for f in range(size):
                count = 0
                for i in range(size):
                    if i + 1 <= size - 1 and ((matrix[i][f] == 1 and matrix[i + 1][f] == 0) or (
                            matrix[i][f] == 0 and matrix[i + 1][f] == 1)):
                        count += 1
                #print(count,ct[f])
                if count != ct[f]:
                    return False
            #print_qr_code(matrix)
            if num_black_line_diff == num_black_each_line and num_black_column_diff == num_black_each_column and qb_diff == qb and db_diff == db:
                matrix_to_print =[row[:] for row in matrix] # deep copy matrix
                #print(matrix)
                count_res += 1
                return True
            #print(num_black_line_diff)
            #print(num_black_column_diff)
            #print(qb_diff)
            #print(db_diff)
            #count_res += 1
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
                qb_diff[get_quadrant(size,line+1, column+1)] > qb[get_quadrant(size,line+1, column+1)]) or (get_diagonal(size,line+1,column+1)!= -1 and
                db_diff[get_diagonal(size,line+1, column+1)] > db[get_diagonal(size,line+1, column+1)]) or (column == N-line-1 and line == column and db_diff > db):
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
            if num_black_line_diff[line] != num_black_each_line[line]:
                return False
            check_qr_code(line + 1, 0,num_black_line_diff,num_black_column_diff,lt_diff,ct_diff,qb_diff,db_diff)
            return True

        if matrix[line][column] != -1:
            check_qr_code(line, column + 1, num_black_line_diff, num_black_column_diff, lt_diff, ct_diff, qb_diff, db_diff)
            return False

        num_black_line_diff[line] += 1
        num_black_column_diff[column] += 1

        if line+1 <= math.floor(size / 2) and column+1 > math.floor(size / 2):
            qb_diff[0] += 1
        elif line+1 <= math.floor(size / 2) and column+1 <= math.floor(size / 2):
            qb_diff[1] += 1
        elif line+1 > math.floor(size / 2) and column+1 <= math.floor(size / 2):
            qb_diff[2] += 1
        else:
            qb_diff[3] += 1

        #qb_diff[get_quadrant(size,line+1, column+1)] += 1

        if column+1 == size-line+1-1 and line == column:
            db_diff[0] +=1
            db_diff[1] +=1
        else:
            if column == line:
                db_diff[0] += 1
            elif column+1 == size-line+1-1:
                db_diff[1] += 1

        matrix[line][column] = 1
        check_qr_code(line, column + 1,num_black_line_diff,num_black_column_diff,lt_diff,ct_diff,qb_diff,db_diff)
        matrix[line][column] = -1
        num_black_line_diff[line] -= 1
        num_black_column_diff[column] -= 1
        if line +1<= math.floor(size / 2) and column +1> math.floor(size / 2):
            qb_diff[0] -= 1
        elif line +1<= math.floor(size / 2) and column +1<= math.floor(size / 2):
            qb_diff[1] -= 1
        elif line +1> math.floor(size / 2) and column +1<= math.floor(size / 2):
            qb_diff[2] -= 1
        else:
            qb_diff[3] -= 1

        # qb_diff[get_quadrant(size,line+1, column+1)] += 1

        if column +1== size - line+1 - 1 and line == column:
            db_diff[0] -= 1
            db_diff[1] -= 1
        else:
            if column == line:
                db_diff[0] -= 1
            elif column +1== size - line+1 - 1:
                db_diff[1] -= 1
        matrix[line][column] = 0
        check_qr_code(line, column + 1,num_black_line_diff,num_black_column_diff,lt_diff,ct_diff,qb_diff,db_diff)
        matrix[line][column] = -1
        return False

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
    outln(top_row)

    # itera sobre as linhas da matriz e as imprime
    for i in range(rows):
        row_string = border

        for j in range(cols):
            if matrix[i][j] == 1:
                row_string += "#"
            else:
                row_string += empty

        row_string += border
        outln(row_string)

    # cria a linha inferior da matriz
    bottom_row = corner + "-" * cols + corner

    # imprime a linha inferior da matriz
    outln(bottom_row)



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
                    outln("DEFECT: No QR Code generated.")
                else:
                    
                    #print(is_valid_encoding(N, lb, cb, lt, ct, qb, db))
                    qrcode ,n_qr_codes = backtrack_qr_codes(N,0,0, lb, cb,lt,ct,qb,db)
                    if n_qr_codes == 1:
                        outln("VALID: 1 QR Code generated!")
                        print_qr_code(qrcode)
                    elif n_qr_codes > 1:
                        outln(f"INVALID: {n_qr_codes} QR Codes generated!")
                    elif n_qr_codes == 0:
                        outln("DEFECT: No QR Code generated!")



                                     
    except :
        pass



from sys import stdin, stdout
import math

def readln():
    return stdin.readline().rstrip()

def outln(n):
    stdout.write(str(n))
    stdout.write("\n")


def is_valid_encoding(N, lb, cb, lt, ct, qb, db):
    # Check if the encoding is valid and can be decoded into a QR code
    if sum(lb) != sum(cb):
        return False
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
                    print(is_valid_encoding(N, lb, cb, lt, ct, qb, db))
                                     
    except :
        pass
    
        
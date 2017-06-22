def primeno(x) :
 for n in range(2, x):
    for x in range(2, int(n/2)+1):
        if n % x == 0:
            print(n, 'equals', x, '*', int(n/x))
            break
    else:
        print(n, 'is prime no')


if __name__ == "__main__":
    import sys
    primeno(int(sys.argv[1])) 

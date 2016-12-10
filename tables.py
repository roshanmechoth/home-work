def multi (x,y):
    for i in range (1,y+1):
        print("{} * {} = {}".format(x,i,x*i))

def main():
    print "enter a number for multipilication table"
    m=int(raw_input())
    print"enter a limit"
    n=int(raw_input())
    multi(m,n)


if __name__ == "__main__":
    main()

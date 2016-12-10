def multi (x,y):
    for i in range (1,y+1):
        print("{} * {} = {}".format(x,i,x*i))

def main():
    m=int(raw_input("enter a number for multipilication table "))
    n=int(raw_input("enter a limit" ))
    multi(m,n)


if __name__ == "__main__":
    main()

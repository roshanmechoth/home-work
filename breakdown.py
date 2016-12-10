def split(a):
    k=()
    rupees=[10,20,50,100,500,1000]
    for i in rupees:
        x=int(a/i)
        k+=(i,)*x
        a-=(i*x)
        print("{} * {} = {} {}".format(i,x,x*i,k))

def main():
    print"enter a value"
    x=int(raw_input())
    split(x)



if __name__ == '__main__':
    main()
